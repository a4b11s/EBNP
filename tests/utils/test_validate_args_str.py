import unittest
from ebnp.utils.validate_args_str import validate_args_str

class TestValidateArgsStr(unittest.TestCase):

    def test_valid_args(self):
        self.assertTrue(validate_args_str("key1:value1"))
        self.assertTrue(validate_args_str("key1:value1,key2:value2"))
        self.assertTrue(validate_args_str("key1:value1,key2:value2,key3:value3"))

    def test_invalid_args(self):
        self.assertFalse(validate_args_str("key1:value1,"))
        self.assertFalse(validate_args_str(":value1"))
        self.assertFalse(validate_args_str("key1:"))
        self.assertFalse(validate_args_str("key1:value1,key2"))
        self.assertFalse(validate_args_str("key1:value1,key2:value2,"))
        self.assertFalse(validate_args_str("key1:value1,key2:value2,key3:"))

    def test_empty_string(self):
        self.assertFalse(validate_args_str(""))

if __name__ == '__main__':
    unittest.main()