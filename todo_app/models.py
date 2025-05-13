import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Cria ou conecta ao banco
def conectar():
    return sqlite3.connect("todo.db")

# Cria as tabelas se não existirem
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            titulo TEXT NOT NULL,
            concluida INTEGER DEFAULT 0,
            FOREIGN KEY(usuario) REFERENCES usuarios(nome)
        )
    ''')

    conn.commit()
    conn.close()

# Cadastra novo usuário com senha criptografada
def cadastrar_usuario(nome, senha):
    conn = conectar()
    cursor = conn.cursor()

    hash_senha = generate_password_hash(senha)
    try:
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, hash_senha))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Usuário já existe
    conn.close()

# Verifica login do usuário
def verificar_login(nome, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado and check_password_hash(resultado[0], senha):
        return True
    return False

# Cria uma nova tarefa
def criar_tarefa(usuario, titulo):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tarefas (usuario, titulo) VALUES (?, ?)", (usuario, titulo))
    conn.commit()
    conn.close()

# Busca tarefas do usuário
def get_tarefas(usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, titulo, concluida FROM tarefas WHERE usuario = ?", (usuario,))
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

# Conta as tarefas do usuário
def contar_tarefas(usuario):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tarefas WHERE usuario = ?", (usuario,))
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tarefas WHERE usuario = ? AND concluida = 1", (usuario,))
    concluidas = cursor.fetchone()[0]

    pendentes = total - concluidas

    conn.close()
    return total, concluidas, pendentes


# Marca como concluído as tarefas do usuário
def concluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Deleta as tarefas do usuário
def deletar_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
