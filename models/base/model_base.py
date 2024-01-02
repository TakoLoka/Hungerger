from flask import Flask
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
import os

app = Flask(__name__, template_folder="../../views", static_folder="../../static")
app.secret_key=os.urandom(24)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'takoloka'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hungerger'
mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = './static/uploads/'
