import os
from flask import Flask
from cartoes import database
from cartoes import init_app
from cartoes.database import db

def create_aap():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'api-cartoes::andrequeiroz2/api-cartoes:latest'
    basedir = os.path.abspath(os.path.dirname('cartoes/database/'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db') 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    database.init_app(app)

    init_app(app)
    
    with app.app_context():
        db.create_all()

    return app

