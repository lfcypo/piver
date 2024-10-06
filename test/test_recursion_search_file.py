import unittest

import piver

piver.set_config_name("hahaha.toml")
piver.add_config_path(".", True)
piver.read_in_config()


class TestRecursionSearchFile(unittest.TestCase):
    def test_recursion_search_file(self):
        self.assertEqual(piver.get("hahaha.msg"), "Congratulations!")

if __name__ == '__main__':
    unittest.main()
