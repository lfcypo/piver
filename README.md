# Piver 📌

A Python library for reading and managing configuration files, similar to Golang's [spf13/viper](https://github.com/spf13/viper).

*README.md also provides a [Chinese version](./README-zh.md)*

## Supported Configuration File Types 📝

✅ = Available, 🚧 = Under Development

* ✅ json
* ✅ yaml
* ✅ **toml**
* 🚧 ini
* 🚧 hcl
* 🚧 envfile
* 🚧 java properties
* ✅ *from environment variables*
* ✅ *from parameters*
* 🚧 *from network*
* ......

## Features ✨

### Ready to Use Out of the Box

Just a simple configuration is needed to get started, eliminating the need to manually write code to read configuration files, allowing you to focus more on project development rather than spending time on tedious tasks.

### Automatic Local Configuration File Search and Load

Piver can automatically search for and load the required configuration files in the target path you configure, making it easy to access configuration entries in your project.

### Default Value Support

Piver can use your custom default values when a configuration item cannot be retrieved.

### Environment Variables and Command Line Parameters Support

Piver can also load configuration files by reading environment variables and command line parameters.

**Priority: Command Line Parameters > Environment Variables > Configuration Files**

## Installation 🚚

If you want to use Piver in your Python project, you need to install it first.

### Install using pip

```bash
pip install piver
```
### Install using poetry
```bash
poetry add piver
```
## Usage 🍱
Piver is global, meaning it's best to load the configuration file early in the project's lifecycle; otherwise, trying to access configuration items before loading the configuration file will raise a `ConfigNotInitializedError`.

### Configure Piver
First, tell Piver the basic information of the configuration file: name, scan location, and format. If you provide a file with an extension to Piver, you do not need to explicitly tell it the file format; it will automatically infer it.

Next, use read_in_config() to read the configuration file.

Finally, use get() to retrieve content, with the target key as a string, using . to separate levels.

```python
import piver

piver.add_config_path(".")     # add current directory to config path
piver.set_config_type("toml")  # set config file type to toml
piver.set_config_name("example")  # set config file name to example
piver.read_in_config()  # read in config file MUST

print(f"Dsn is: {piver.get('database.dsn')}")  # get value of database.dsn

```
## Author
ZichengHuang 黄子程

lfcypo (Zicheng Huang)

