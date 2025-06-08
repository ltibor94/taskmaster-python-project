from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import db
from controller.task_controller import task_blueprint

from service.task_service import TaskService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_master.db'
db.init_app(app)

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
