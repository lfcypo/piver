import unittest

import os

os.environ["PIVER_TEST_FOO"] = "bar"
os.environ["PIVER_TEST_BAR"] = "foo"

import piver

piver.set_env_prefix("PIVER_TEST_")

piver.add_config_path(".")
piver.set_config_name("test.yaml")

piver.read_in_config()


class TestGetValueFromEnv(unittest.TestCase):
    def test_get_value_from_env_foo(self):
        self.assertEqual(piver.get("foo"), "bar")

    def test_get_value_from_env_bar(self):
        self.assertEqual(piver.get("bar"), "foo")


if __name__ == '__main__':
    unittest.main()
