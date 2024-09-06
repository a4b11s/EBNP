from ebnp.enums.methods import METHODS_ENUM


def encode_ebnp_data(data: dict[str, any]) -> str:
    """
    Encode the data to the EBNP protocol.
    :data: dict[str, any] - the data to encode to the EBNP protocol
    """

    method = data["method"]
    eventid = data["eventid"]
    args = data["args"]

    if method not in METHODS_ENUM.__dict__.values():
        raise ValueError(f"Invalid method: {method}")

    if not isinstance(eventid, str):
        raise ValueError(f"Invalid eventid: {eventid}")

    if not isinstance(args, dict):
        raise ValueError(f"Invalid arguments: {args}")

    args_str = ",".join([key + ":" + str(value) for key, value in args.items()])
    args_str = args_str

    return f"[{method}][{eventid}][{args_str}]"
