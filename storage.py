import json
from datetime import datetime
from pathlib import Path
from typing import List

from models import Task, TaskStatus

path = "tasks.json"

def _ensure_json() -> None:
    Path(path).touch()

def _convert_status(status_str):
    try:
        return TaskStatus(status_str)
    except ValueError:
        return TaskStatus.TODO # default to TO-DO if something is wrong with string.



def _dict_to_task(data: dict) -> Task:
    return Task(
        id=data["id"],
        description=data["description"],
        status=_convert_status(data["status"]),
        created_at=datetime.strptime(data['d'], "%Y-%m-%d %H:%M:%S"),
        updated_at=datetime.strptime(data['u'], "%Y-%m-%d %H:%M:%S")
    )


def _task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "description": task.description,
        "status": task.status.value,
        "d": task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "u": task.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    }


def load_tasks() -> list[Task]:
    tasks = []
    if not Path(path).exists():
        return tasks

    with open(path, "r") as f:
        try:
            json_data = json.load(f)
            return [_dict_to_task(item) for item in json_data]
        except (json.JSONDecodeError, KeyError):
            return tasks

#save to JSON
def save_tasks(tasks : List[Task]) -> None:
    _ensure_json()

    dict_list = [_task_to_dict(task) for task in tasks]
    with open(path, "w") as f:
        json.dump(dict_list, f, indent=4)

def save_task(new_task : Task) -> None:
    current_task = load_tasks()
    current_task.append(new_task)
    save_tasks(current_task)



