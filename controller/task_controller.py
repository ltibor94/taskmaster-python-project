from typing import Optional
from flask import Blueprint, redirect, render_template, request
from dto.update_task_request_dto import UpdateTaskRequestDto
from logger.logger import Logger
from service.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@task_blueprint.route("/", methods=['GET', 'POST']) # type: ignore
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            task_service.create_task(task_content)
            return redirect('/')
        except Exception as e:
            render_template('error.html', 
                            error_message = f'There was a problem new tasks: {e}')
    else:
        try:
            tasks = task_service.get_all_tasks()
            return render_template('index.html', tasks=tasks)
        except Exception as e:
            return render_template('error.html', 
                            error_message = f'There was a problem retrieving tasks: {e}')

@task_blueprint.route('/delete/<int:id>')
def delete(id: int):
    try:
        task_service.delete_task(id)
        return redirect('/')
    except:
        return render_template('error.html', 
                            error_message = 'There was a problem deleting that task.')

@task_blueprint.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int):
    logger = Logger("TaskController").get_logger()
    logger.info(f"Updating task with ID: {id}")
    if request.method == 'POST':
        try:
            completed = request.form.get('completed') == 'on'
            update_request = UpdateTaskRequestDto(request.form['content'], completed)
            logger.info(f"Update request: {update_request}")
            task_service.update_task(id, update_request)
            return redirect('/')
        except Exception as e:
            logger.error(f"Error updating task with ID {id}: {e}, request: {request.form}")
            return render_template('error.html', 
                                   error_message = 'There was a problem updating that task.')
    else:
        return render_template('update.html', task=task_service.get_task(id))
