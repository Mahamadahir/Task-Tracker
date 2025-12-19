from errors import InvalidStatusError
from models import TaskStatus



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




