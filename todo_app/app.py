from flask import Flask, render_template, redirect, request, url_for, session, flash
from models import criar_tabelas, verificar_login, cadastrar_usuario, get_tarefas, criar_tarefa, concluir_tarefa, deletar_tarefa, contar_tarefas
import os
from models import contar_tarefas

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Chave secreta para sessão

criar_tabelas()  # Garante que as tabelas do banco estão criadas

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if verificar_login(usuario, senha):
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            flash("Usuário ou senha inválidos")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        cadastrar_usuario(usuario, senha)
        flash("Cadastro realizado com sucesso!")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    usuario = session['usuario']
    tarefas = get_tarefas(usuario)
    total, concluidas, pendentes = contar_tarefas(usuario)
    
    return render_template(
        'dashboard.html',
        tarefas=tarefas,
        usuario=usuario,
        total=total,
        concluidas=concluidas,
        pendentes=pendentes
    )


@app.route('/add', methods=['POST'])
def add():
    if 'usuario' in session:
        titulo = request.form['titulo']
        criar_tarefa(session['usuario'], titulo)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/concluir/<int:id>')
def concluir(id):
    if 'usuario' in session:
        concluir_tarefa(id)
    return redirect(url_for('dashboard'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario' in session:
        deletar_tarefa(id)
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
