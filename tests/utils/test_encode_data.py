import unittest
from ebnp.utils.encode_data import encode_ebnp_data
from ebnp.enums.methods import METHODS_ENUM


class TestEncodeEbnPData(unittest.TestCase):

    def test_valid_data(self):
        data = {
            "method": METHODS_ENUM.EMIT,
            "eventid": "event123",
            "args": {"arg1": "value1", "arg2": 2},
        }
        expected_output = f"[{METHODS_ENUM.EMIT}][event123][arg1:value1,arg2:2]"
        self.assertEqual(encode_ebnp_data(data), expected_output)

    def test_invalid_method(self):
        data = {
            "method": "INVALID_METHOD",
            "eventid": "event123",
            "args": {"arg1": "value1", "arg2": 2},
        }
        with self.assertRaises(ValueError) as context:
            encode_ebnp_data(data)
        self.assertEqual(str(context.exception), "Invalid method: INVALID_METHOD")

    def test_invalid_eventid(self):
        data = {
            "method": METHODS_ENUM.EMIT,
            "eventid": 123,
            "args": {"arg1": "value1", "arg2": 2},
        }
        with self.assertRaises(ValueError) as context:
            encode_ebnp_data(data)
        self.assertEqual(str(context.exception), "Invalid eventid: 123")

    def test_invalid_args(self):
        data = {
            "method": METHODS_ENUM.EMIT,
            "eventid": "event123",
            "args": ["arg1", "value1"],
        }
        with self.assertRaises(ValueError) as context:
            encode_ebnp_data(data)
        self.assertEqual(
            str(context.exception), "Invalid arguments: ['arg1', 'value1']"
        )


if __name__ == "__main__":
    unittest.main()
