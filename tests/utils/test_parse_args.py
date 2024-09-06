import unittest
from ebnp.utils.parse_args import parse_args


class TestParseArgs(unittest.TestCase):

    def test_single_argument(self):
        args_str = "key1:value1"
        expected_output = {"key1": "value1"}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_multiple_arguments(self):
        args_str = "key1:value1,key2:value2,key3:value3"
        expected_output = {"key1": "value1", "key2": "value2", "key3": "value3"}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_empty_string(self):
        args_str = ""
        expected_output = {}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_argument_with_spaces(self):
        args_str = "key1: value1 , key2 :value2"
        expected_output = {"key1": "value1", "key2": "value2"}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_argument_with_tabs(self):
        args_str = "key1:\tvalue1 , key2 :\tvalue2"
        expected_output = {"key1": "value1", "key2": "value2"}

        self.assertEqual(parse_args(args_str), expected_output)

    def test_argument_with_spaces_inside_values(self):
        args_str = "key1: value 1 , key2 :value 2"
        expected_output = {"key1": "value 1", "key2": "value 2"}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_argument_with_spaces_inside_keys(self):
        args_str = "key 1: value1 , key 2 :value2"
        expected_output = {"key 1": "value1", "key 2": "value2"}
        self.assertEqual(parse_args(args_str), expected_output)

    def test_invalid_format(self):
        args_str = "key1:value1,key2value2"
        with self.assertRaises(ValueError):
            parse_args(args_str)


if __name__ == "__main__":
    unittest.main()
