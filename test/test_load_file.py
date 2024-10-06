import unittest


class TestLoadFile(unittest.TestCase):

    def test_load_file_toml(self):
        import piver
        piver.set_config_type("toml")
        piver.set_config_name("test")
        piver.add_config_path(".")
        piver.read_in_config()

        self.assertEqual(piver.get("test.key"), 114514)

        piver.reset()

    def test_load_file_yaml(self):
        import piver
        piver.set_config_name("test")
        piver.set_config_type("toml")
        piver.add_config_path(".")
        piver.read_in_config()

        self.assertEqual(piver.get("test.key"), 114514)

        piver.reset()

    def test_load_file_json(self):
        import piver
        piver.set_config_name("test")
        piver.set_config_type("json")
        piver.add_config_path(".")
        piver.read_in_config()

        self.assertEqual(piver.get("test.key"), 114514)

        piver.reset()


if __name__ == '__main__':
    unittest.main()
