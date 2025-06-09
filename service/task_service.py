from typing import Optional
from dto.update_task_request_dto import UpdateTaskRequestDto
from logger.logger import Logger
from model.task import Task
from config import db

# Business Logic Layer for Task Management
class TaskService:
    
    LOGGER = Logger("TaskService").get_logger()
    
    # Retrieves all tasks ordered by their creation date
    def get_all_tasks(self) -> list[Task]:
        # Logic to retrieve all tasks
        return Task.query.order_by(Task.date_created).all()
    
    # Retrieves all tasks ordered by their creation date
    def get_all_tasks_filtered(self, filter: Optional[str] = None) -> list[Task]:
        # Logic to retrieve all tasks
        if filter == "finished":
            return Task.query.filter_by(completed=True).order_by(Task.date_created).all()
        elif filter == "open":
            return Task.query.filter(Task.completed.is_(False)).order_by(Task.date_created).all()
        elif filter == "all" or filter is None:
            return self.get_all_tasks()
        else:
            raise ValueError(f"Invalid filter value: {filter}. Valid values are 'finished', 'open', 'all' or None.")
    
    # Retrieves a specific task by its ID
    def get_task(self, task_id: int) -> Task:
        # Logic to retrieve a task by its ID
        return Task.query.get_or_404(task_id)
        
    # Creates a new task with the provided content
    def create_task(self, task_content: str) -> Task | None:
        # Logic to create a new task
        if len(task_content.strip()) != 0:
            new_task = Task(content=task_content) # type: ignore
            db.session.add(new_task)
            db.session.commit()
            return new_task
        return None
    
    # Updates an existing task with new content
    def update_task(self, task_id: int, update_request: UpdateTaskRequestDto) -> Task:
        self.LOGGER.info(f"Updating task with ID: {task_id} with content: {update_request.content} and completed status: {update_request.completed}")
        task = self.get_task(task_id)
        task.content = update_request.content
        task.completed = update_request.completed
        db.session.commit()
        return self.get_task(task_id)
    
    # Deletes a task by its ID
    def delete_task(self, task_id: int) -> None:
        task_to_delete = self.get_task(task_id)
        db.session.delete(task_to_delete)
        db.session.commit()
    
        # Deletes a task by its ID
    def complete_task(self, task_id: int) -> None:
        task_to_complate = self.get_task(task_id)
        task_to_complate.completed = True
        db.session.commit()
        
            