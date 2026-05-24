import argparse

from errors import InvalidDescriptionError, InvalidStatusError, TaskNotFoundError
from models import TaskStatus
from task_manager import (
    create_task,
    update_description,
    update_status,
    delete_task,
    list_tasks,
)


def convert_status(arg: str) -> TaskStatus:
    if not arg.strip():
        raise InvalidStatusError("Status cannot be empty")

    name = arg.strip().upper().replace('-', '_').replace(' ', '_')

    if name in TaskStatus.__members__:
        return TaskStatus[name]

    allowed_names = ", ".join(TaskStatus.__members__.keys())
    allowed_values = ", ".join(m.value for m in TaskStatus)
    raise InvalidStatusError(f"{name} is not a valid status. "
        f"Allowed values : {allowed_values} "
        f"Allowed names : {allowed_names}"
                             )


def print_task(task):
    print(f"{task.id},   [{task.status.value}]  {task.description}")

def add_task(args):
    task_id = create_task(args.description)
    print(f"Task added successfully with ID: {task_id}")


def update(args):
    update_description(args.id, args.description)

def mark_task(args):
    update_status(args.id, args.status)


def delete(args):
    delete_task(args.id)

def list(args):

    tasks = list_tasks(args.status)

    if not tasks:
        print("No tasks found")
        return
    
    for task in tasks:
        print_task(task)

def build_parser():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)


    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str)
    add_parser.set_defaults(func=add_task)

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id",type=int)
    update_parser.add_argument("description", type=str)
    update_parser.set_defaults(func=update)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    delete_parser.set_defaults(func=delete)

    mark_parser = subparsers.add_parser("mark")
    mark_parser.add_argument("id", type=int)
    mark_parser.add_argument("status", type=convert_status)
    mark_parser.set_defaults(func=mark_task)

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("status", nargs="?",type=convert_status)
    list_parser.set_defaults(func=list)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    
    try:
        args.func(args)
    except (InvalidDescriptionError, InvalidStatusError, TaskNotFoundError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()




