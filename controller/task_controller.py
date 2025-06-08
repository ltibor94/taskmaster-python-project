from flask import Blueprint, redirect, render_template, request
from logger.logger import Logger
from service.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@task_blueprint.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            task_service.create_task(task_content)
            return redirect('/')
        except:
            return 'There was a problem.'
    else:
        try:
            tasks = task_service.get_all_tasks()
            return render_template('index.html', tasks=tasks)
        except Exception as e:
            return render_template('index.html')

@task_blueprint.route('/delete/<int:id>')
def delete(id: int):
    try:
        task_service.delete_task(id)
        return redirect('/')
    except:
        return 'There was a problem deleting that task.'

@task_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    if request.method == 'POST':
        try:
            task_service.update_task(id, request.form['content'])
            return redirect('/')
        except:
            return 'There was a problem updating that task.'
    else:
        return render_template('update.html', task=task_service.get_task(id))
