import re


def parse_args(args_str: str) -> dict[str, str]:
    """
    Parse the arguments from the string.
    :args_str: str - the arguments string
    :return: dict[str, str] - the parsed arguments
    """

    args = args_str.split(",")
    parsed_args = {}

    if re.sub(r"\s+", "", args_str) == "":
        return parsed_args

    for arg in args:
        key, value = arg.split(":")
        parsed_args[key.strip()] = value.strip()

    return parsed_args
