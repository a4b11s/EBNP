import unittest
from unittest.mock import Mock
from ebnp.modules.event import Event
from ebnp.enums.args_type import TYPES_ENUM

class TestEvent(unittest.TestCase):

    def test_event_initialization(self):
        event = Event(name="test_event")
        self.assertEqual(event.name, "test_event")
        self.assertIsNone(event.args)
        self.assertIsNotNone(event.uuid)
        self.assertEqual(event._handlers, {})

    def test_event_initialization_with_args(self):
        args = {
            "arg1": TYPES_ENUM.STRING,
            "arg2": TYPES_ENUM.NUM,
            "arg3": TYPES_ENUM.DICT,
        }
        event = Event(name="test_event", args=args)
        self.assertEqual(event.name, "test_event")
        self.assertEqual(event.args, args)
        self.assertIsNotNone(event.uuid)
        self.assertEqual(event._handlers, {})

    def test_add_handler(self):
        event = Event(name="test_event")
        handler = Mock()
        handler_id = event.add_handler(handler)
        self.assertIn(handler_id, event._handlers)
        self.assertEqual(event._handlers[handler_id], handler)

    def test_remove_handler(self):
        event = Event(name="test_event")
        handler = Mock()
        handler_id = event.add_handler(handler)
        event.remove_handler(handler_id)
        self.assertNotIn(handler_id, event._handlers)

    def test_emit_event(self):
        event = Event(name="test_event")
        handler = Mock()
        event.add_handler(handler)
        event.emit(arg1="value1")
        handler.assert_called_once_with(arg1="value1")

    def test_check_args_valid(self):
        args = {
            "arg1": TYPES_ENUM.STRING,
            "arg2": TYPES_ENUM.NUM,
        }
        event = Event(name="test_event", args=args)
        valid_args = {
            "arg1": "string_value",
            "arg2": 123,
        }
        self.assertTrue(event._check_args(valid_args))

    def test_check_args_invalid(self):
        args = {
            "arg1": TYPES_ENUM.STRING,
            "arg2": TYPES_ENUM.NUM,
        }
        event = Event(name="test_event", args=args)
        invalid_args = {
            "arg1": 123,
            "arg2": "string_value",
        }
        self.assertFalse(event._check_args(invalid_args))

    def test_validate_args_init_valid(self):
        args = {
            "arg1": TYPES_ENUM.STRING,
            "arg2": TYPES_ENUM.NUM,
        }
        event = Event(name="test_event")
        event._validate_args_init(args)
        self.assertEqual(event.args, args)

    def test_validate_args_init_invalid(self):
        args = {
            "arg1": "INVALID_TYPE",
            "arg2": TYPES_ENUM.NUM,
        }
        event = Event(name="test_event")
        with self.assertRaises(ValueError):
            event._validate_args_init(args)


if __name__ == '__main__':
    unittest.main()