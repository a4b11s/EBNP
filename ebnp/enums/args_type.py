class TYPES_ENUM(object):
    STRING = "string"
    NUM = "num"
    BOOL = "bool"
    DICT = "dict"
    LIST = "list"
    TUPLE = "tuple"
    SET = "set"
    BYTES = "bytes"
    BYTEARRAY = "bytearray"
    NONE = "None"

    types_dict = {
        "string": str,
        "num": int,
        "bool": bool,
        "dict": dict,
        "list": list,
        "tuple": tuple,
        "set": set,
        "bytes": bytes,
        "bytearray": bytearray,
        "None": None
    }
    
    @staticmethod
    def get_type(type: str):
        """
        Get the type from the type string
        :param type: str - the type string
        :return: type - the type
        """
        return TYPES_ENUM.types_dict[type]