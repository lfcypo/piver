import unittest

import piver

piver.add_config_path(".")
piver.set_config_name("test.toml")
piver.load_config()

class TestDefaultValue(unittest.TestCase):
    def test_default_value(self):
        self.assertEqual(piver.get("test.undefined_key", "value1"), "value1")


if __name__ == '__main__':
    unittest.main()
