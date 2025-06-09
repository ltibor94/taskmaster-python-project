from typing import Optional
from flask import Blueprint, redirect, render_template, request
from dto.update_task_request_dto import UpdateTaskRequestDto
from logger.logger import Logger
from service.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@task_blueprint.route("/", methods=['GET', 'POST'])
@task_blueprint.route("/<string:filter>", methods=['GET', 'POST'])
def index(filter: Optional[str] = None):
    Logger("TaskController").get_logger().info(f"Accessing task index with filter: {filter}")
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            task_service.create_task(task_content)
            return redirect('/')
        except Exception as e:
            return render_template('error.html', 
                            error_message = f'There was a problem new tasks: {e}')
    else:
        try:
            tasks = task_service.get_all_tasks_filtered(filter)
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
    
@task_blueprint.route('/complete/<int:id>', methods=['GET'])
def complete(id: int):
    logger = Logger("TaskController").get_logger()
    logger.info(f"Completing task with ID: {id}")
    try:
        task_service.complete_task(id)
        logger.info(f"Task with ID {id} completed successfully.")
        return redirect('/')
    except Exception as e:
        logger.error(f"Error completing task with ID {id}: {e}")
        return render_template('error.html', 
                               error_message = 'There was a problem completing that task.')
