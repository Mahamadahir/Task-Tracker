from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

@dataclass
class Task:
    id : int
    description : str
    status : TaskStatus = TaskStatus.TODO
    created_at : datetime = field(default_factory=datetime.now)
    updated_at : datetime = field(default_factory=datetime.now)



