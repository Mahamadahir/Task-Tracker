from datetime import datetime
from typing import Optional

from errors import TaskNotFoundError, InvalidStatusError, InvalidDescriptionError
from models import Task, TaskStatus
from storage import save_task, load_tasks, save_tasks


def create_task(description : str) -> int:
    tasks = load_tasks()
    if not description.strip():
        raise InvalidDescriptionError("This description is empty")
    if tasks :
        id_num = max(task.id for task in tasks) + 1
    else:
        id_num = 1
    task = Task(id_num, description.strip())
    save_task(task)
    return id_num

def update_description(id_num : int, description : str):
    if description.strip() :
        tasks = load_tasks()
        for task in tasks:
            if task.id == id_num:
                task.description = description.strip()
                task.updated_at = datetime.now()
                save_tasks(tasks)
                return
        raise TaskNotFoundError("This Task does not exist")
    else:
        raise InvalidDescriptionError("This description is empty")

def update_status(id_num : int, status : TaskStatus):
    if not isinstance(status, TaskStatus):
        raise InvalidStatusError("This status does not exist")
    tasks = load_tasks()
    for task in tasks:
        if task.id == id_num:
            task.status = status
            task.updated_at = datetime.now()
            save_tasks(tasks)
            return

    raise TaskNotFoundError("This Task does not exist")

def delete_task(id_num: int):
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            if task.id == id_num:
                tasks.remove(task)
                save_tasks(tasks)
                return
    raise TaskNotFoundError("This Task does not exist")

def list_tasks(status: Optional[TaskStatus] = None):
    tasks = load_tasks()
    if status is None:
        return tasks
    filtered_tasks = []
    for task in tasks:
        if task.status == status:
            filtered_tasks.append(task)
    return filtered_tasks

