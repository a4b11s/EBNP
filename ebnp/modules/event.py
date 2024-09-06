import uuid

from ebnp.enums.args_type import TYPES_ENUM


class Event(object):
    def __init__(self, name: str, args: dict = None):
        """
        Create a new event
        :param name: str - name of the event
        :param args: dict - arguments the event should have {arg_name: arg_type}
        arg_type should be a type from the TYPES_ENUM
        args example:

        {
            "arg1": TYPES_ENUM.STRING,
            "arg2": TYPES_ENUM.NUM,
            "arg3": TYPES_ENUM.DICT,
        }

        """

        self.name = name
        self.args = args
        self.uuid = uuid.uuid4()

        self._handlers = dict({})

    def add_handler(self, handler: callable) -> str:
        """
        Add a handler to the event
        :param handler: callable - the handler to add
        :return: str - id of the handler
        """

        id = hash(handler)
        self._handlers.update({id: handler})

        return id

    def remove_handler(self, id: str) -> None:
        """
        Remove a handler from the event
        :param id: str - id of the handler to remove
        :return: None
        """
        self._handlers.pop(id)

    def emit(self, **kwargs) -> None:
        """
        Emit the event
        :param kwargs: dict - arguments to pass to the handlers
        :return: None
        """
        for handler in self._handlers.values():
            handler(**kwargs)

    def _check_args(self, args: dict) -> bool:
        """
        Check if the arguments are valid
        :param args: dict - arguments to check
        :return: bool - whether the arguments are valid
        """
        if self.args is None:
            return True

        for key, value in self.args.items():
            if key not in args:
                return False

            # if not isinstance(args[key], TYPES_ENUM.get_type(value)):
            #     return False

            if not type(args[key]) == TYPES_ENUM.get_type(value):
                return False
            
        return True

    def _validate_args_init(self, args: dict) -> None:
        """
        Validate the arguments passed to the event constructor
        :param args: dict - arguments to validate
        :return: None
        """
        for _, value in args.items():
            if value not in TYPES_ENUM.__dict__.values():
                raise ValueError(f"Invalid argument type: {value}")

        self.args = args

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
