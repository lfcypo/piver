import piver

piver.add_config_path(".")     # add current directory to config path
piver.set_config_type("toml")  # set config file type to toml
piver.set_config_name("example")  # set config file name to example
piver.read_in_config()  # read in config file MUST

print(f"Dsn is: {piver.get('database.dsn')}")  # get value of database.dsn
