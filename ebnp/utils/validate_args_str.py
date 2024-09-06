import re


def validate_args_str(args_str: str) -> bool:
    if not re.match(r"^(\w+:\w+)(,\w+:\w+)*$", args_str):
        return False

    return True
