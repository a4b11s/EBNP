from ebnp.enums.methods import METHODS_ENUM
from ebnp.utils.parse_args import parse_args
from ebnp.utils.validate_args_str import validate_args_str


def decode_ebnp_data(data: str) -> dict[str, str]:
    """
    Decode the data from the EBNP protocol.
    :data: str - the data to decode from the EBNP protocol
    """

    if data.count("[") < 3 or data.count("]") < 3:
        raise ValueError("Invalid data")

    method = data[1 : data.index("]")]

    data = data[data.index("]") + 1 :]
    eventid = data[1 : data.index("]")]

    data = data[data.index("]") + 1 :]
    args_str = data[1:-1]

    if not validate_args_str(args_str):
        raise ValueError("Invalid data")

    if method not in METHODS_ENUM.__dict__.values():
        raise ValueError(f"Invalid data")
    
    if not eventid:
        raise ValueError(f"Invalid data")
    
    args = parse_args(args_str)

    data = {"method": method, "eventid": eventid, "args": args}

    return data
