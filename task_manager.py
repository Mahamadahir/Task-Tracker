from datetime import datetime
from typing import Optional
from xml.dom import NO_MODIFICATION_ALLOWED_ERR

from models import Task, TaskStatus
from storage import save_task, load_tasks, save_tasks


def create_task(description : str):
    tasks = load_tasks()
    if len(tasks) > 0:
        id_num = max(task.id for task in tasks) + 1
    else:
        id_num = 1
    task = Task(id_num, description)
    save_task(task)

def update_description(id_num : int, description : str):
    if len(description) > 0:
        tasks = load_tasks()
        for task in tasks:
            if task.id == id_num:
                task.description = description
                task.updated_at = datetime.now()
        save_tasks(tasks)
    else:
        raise Exception("Task description not found")

def update_status(id_num : int, status : TaskStatus):
    if status in TaskStatus:
        tasks = load_tasks()
        for task in tasks:
            if task.id == id_num:
                task.status = status
                task.updated_at = datetime.now()
        save_tasks(tasks)

def delete_task(id_num: int):
    tasks = load_tasks()
    if len(tasks) > 0:
        for task in tasks:
            if task.id == id_num:
                tasks.remove(task)
                break
    save_tasks(tasks)

def list_tasks(status: Optional[TaskStatus] = None):
    tasks = load_tasks()
    if status is None:
        return tasks
    filtered_tasks = []
    for task in tasks:
        if task.status == status:
            filtered_tasks.append(task)
    return filtered_tasks

