import json
import os
from datetime import datetime

from models import Task, TaskStatus

path = "tasks.json"

def _ensure_json() -> None:
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f, indent=4)


def _convert_status(status_str):
    try:
        return TaskStatus(status_str)
    except ValueError:
        return TaskStatus.TODO  # Default to TODO if the saved status is invalid.



def _dict_to_task(data: dict) -> Task:
    return Task(
        id=data["id"],
        description=data["description"],
        status=_convert_status(data["status"]),
        created_at= datetime.fromisoformat(data["createdAt"]),
        updated_at=datetime.fromisoformat(data["updatedAt"])
    )


def _task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status.value,
        "createdAt": task.created_at.isoformat(),
        "updatedAt": task.updated_at.isoformat()
    }

def load_tasks() -> list[Task] :
    tasks = []
    _ensure_json()

    try:
        with open(path, "r") as f:
            json_data = json.load(f)
    except (OSError, json.JSONDecodeError):
        return tasks

    for item in json_data:
        try:
            tasks.append(_dict_to_task(item))
        except (ValueError, KeyError):
            # Skip invalid saved tasks instead of failing to load the whole file.
            pass
    return tasks


def save_tasks(tasks : list[Task]) -> None:
    _ensure_json()

    dict_list = [_task_to_dict(task) for task in tasks]
    with open(path, "w") as f:
        json.dump(dict_list, f, indent=4)

def save_task(new_task : Task) -> None:
    current_task = load_tasks()
    current_task.append(new_task)
    save_tasks(current_task)

