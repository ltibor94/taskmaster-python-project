from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from config import db

from service.task_service import TaskService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_master.db'
db.init_app(app)

task_sertvice = TaskService()


@app.route("/", methods=['GET', 'POST']) # type: ignore
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if not task_content or not task_content.isspace() or len(task_content) != 0:
            try:
                task_sertvice.create_task(task_content)
                return redirect('/')
            except:
                return 'There was a problem.'
    else:
        try:
            tasks = task_sertvice.get_all_tasks()
            return render_template('index.html', tasks=tasks)
        except Exception as e:
            return render_template('index.html')
        
@app.route('/delete/<int:id>')
def delete(id):
    try:
        task_sertvice.delete_task(id)
        return redirect('/')
    except:
        return 'There was a problem deleting that task.'
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    if request.method == 'POST':
        try:
            task_sertvice.update_task(id, request.form['content'])
            return redirect('/')
        except:
            return 'There was a problem updating that task.'
    else:
        return render_template('update.html', task=task_sertvice.get_task(id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
