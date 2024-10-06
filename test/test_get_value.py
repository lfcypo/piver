import unittest
import piver

piver.add_config_path(".")
piver.set_config_type("toml")
piver.set_config_name("test")
piver.read_in_config()

class TestGetValue(unittest.TestCase):

    def test_get_value_str(self):
        self.assertEqual(piver.get_str("test.a_key_with_str"), "hello world")

    def test_get_value_int(self):
        self.assertEqual(piver.get_int("test.a_key_with_int"), 123456)

    def test_get_value_float(self):
        self.assertEqual(piver.get_float("test.a_key_with_float"), 3.141592653589793)

    def test_get_value_bool(self):
        self.assertEqual(piver.get_bool("test.a_key_with_bool"), True)

    def test_get_value_list(self):
        self.assertEqual(piver.get_list("test.a_key_with_list"), ["apple", "banana", "cherry"])

    def test_get_value_dict(self):
        self.assertEqual(piver.get_dict("test.a_key_with_dict"), {"name": "John", "age": 30, "city": "New York"})

if __name__ == '__main__':
    unittest.main()
    piver.reset()
