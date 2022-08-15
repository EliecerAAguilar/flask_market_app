from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from market.routes import main# IDK why but DO NOT MOVE THIS LINE
