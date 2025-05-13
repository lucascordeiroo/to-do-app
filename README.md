# ✅ To-Do App com Login - Flask + SQLite

Projeto desenvolvido com o objetivo de praticar **desenvolvimento web com Python e Flask**, incluindo conceitos de autenticação, rotas, sessões, banco de dados e CRUD completo com interface web.

---

## 📌 Funcionalidades

- ✅ Cadastro de usuários com senha criptografada
- 🔐 Login e autenticação com sessão
- 📝 Cadastro de tarefas por usuário
- ✔️ Marcar tarefas como concluídas
- ❌ Excluir tarefas
- 📊 Contador de tarefas (total, concluídas, pendentes)
- 💅 Interface com Bootstrap 5 (responsiva e amigável)

---

## 🛠 Tecnologias usadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)

---

## 🚀 Como rodar o projeto

1. Clone o repositório

```bash
git clone https://github.com/lucascordeiroo/todo-app.git
cd todo-app

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate    # no Windows
# ou
source venv/bin/activate # no Linux/macOS

3. Instale as dependências
pip install flask

4. Rode o projeto
python app.py

5. Acesse no navegador
http://localhost:5000

📂 Estrutura do projeto
todo-app/
├── app.py
├── models.py
├── todo.db          # Criado automaticamente
├── templates/
│   ├── layout.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── README.md

👨‍💻 Autor
Desenvolvido por Lucas Cordeiro

📫 Entre em contato: lucascordeirooliveira50@gmail.com
