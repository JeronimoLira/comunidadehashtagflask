from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
import os

app = Flask(__name__)

# Forma de criar token do python
# ==============================
# (venv) PS C:\Jeronimo\Pessoal\A - Estudos\Hashtag\Python\Hashtag Treinamentos\CursoCompleto\DesenvolvimentoWEB\ComFlask> python
# Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = '96f369e8b9bb70c7170c1cd9aed75df4'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'



database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes
