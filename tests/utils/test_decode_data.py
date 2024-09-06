import unittest
from ebnp.utils.decode_data import decode_ebnp_data
from ebnp.enums.methods import METHODS_ENUM


class TestDecodeEBNPData(unittest.TestCase):

    def test_decode_ebnp_data_valid(self):
        data = f"[{list(METHODS_ENUM.__dict__.values())[0]}][eventid][arg1:value1,arg2:value2]"
        expected_output = {
            "method": list(METHODS_ENUM.__dict__.values())[0],
            "eventid": "eventid",
            "args": {"arg1": "value1", "arg2": "value2"},
        }
        self.assertEqual(decode_ebnp_data(data), expected_output)

    def test_decode_ebnp_data_invalid_format(self):
        data = "[method][eventid][arg1:value1,arg2]"
        with self.assertRaises(ValueError):
            decode_ebnp_data(data)

    def test_decode_ebnp_data_missing_brackets(self):
        data = "[method][eventid[arg1:value1,arg2:value2]"
        with self.assertRaises(ValueError):
            decode_ebnp_data(data)

    def test_decode_ebnp_data_invalid_method(self):
        data = "[invalid_method][eventid][arg1:value1,arg2:value2]"
        with self.assertRaises(ValueError):
            decode_ebnp_data(data)

    def test_decode_ebnp_data_invalid_eventid(self):
        data = "[method][][arg1:value1,arg2:value2]"
        with self.assertRaises(ValueError):
            decode_ebnp_data(data)

    def test_decode_ebnp_data_invalid_args(self):
        data = "[method][eventid][arg1:value1,arg2]"
        with self.assertRaises(ValueError):
            decode_ebnp_data(data)


if __name__ == "__main__":
    unittest.main()
