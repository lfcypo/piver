import unittest


class TestAutoFetchConfigFileType(unittest.TestCase):
    def test_auto_fetch_config_file_type_toml(self):
        import piver
        piver.set_config_name("test.toml")
        piver.read_in_config()
        self.assertEqual(piver.get("test.key"), 114514)
        piver.reset()

    def test_auto_fetch_config_file_type_json(self):
        import piver
        piver.set_config_name("test.json")
        piver.read_in_config()
        self.assertEqual(piver.get("test.key"), 114514)
        piver.reset()

    def test_auto_fetch_config_file_type_yaml_1(self):
        import piver
        piver.set_config_name("test.yaml")
        piver.read_in_config()
        self.assertEqual(piver.get("test.key"), 114514)
        piver.reset()

    def test_auto_fetch_config_file_type_yaml_2(self):
        import piver
        piver.set_config_name("test.yml")
        piver.read_in_config()
        self.assertEqual(piver.get("test.key"), 114514)
        piver.reset()

if __name__ == '__main__':
    unittest.main()

