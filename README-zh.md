# Piver 📌

一个用于读取和管理配置文件的 Python 库，类似于 Golang 的 [spf13/viper](https://github.com/spf13/viper)。

## 支持的配置文件类型 📝

✅ = 可用，🚧 = 待开发

* ✅ json
* ✅ yaml
* ✅ **toml**
* 🚧 ini
* 🚧 hcl
* 🚧 envfile
* 🚧 java properties
* ✅ *来自环境变量*
* ✅ *来自参数*
* 🚧 *来自网络*
* ......

## 特性 ✨

### 开箱就可以吃

只需简单配置一下即可食用（），免去了手动编写读取配置文件的代码，把时间和精力更加专注的放在项目开发中而不是花费在无聊的地方。

### 自动搜寻本地的配置文件并装载

Piver可以在您配置的目标路径里自动查找需要的配置文件并装载，您在项目里可以很轻松的使用piver来访问配置文件条目。

### 默认值支持

Piver可以在获取配置项无果的时候使用您自定义的默认值。

### 环境变量和命令行参数支持

piver也可以通过读取环境变量和命令行参数装载配置文件。

**优先级：命令行参数 > 环境变量 > 配置文件**

## 安装 🚚

如果您想在 Python 项目中使用 piver，您需要先安装它。

### 使用 pip 安装

```bash
pip install piver
```

### 使用 poetry 安装

```bash
poetry add piver
```

## 使用 🍱

Piver 是全局的。 这意味着您最好在整个项目生命周期的早期加载配置文件，否则在配置文件加载之前尝试获取配置项目将抛出 ConfigNotInitializedError 错误。

### 配置 piver

首先，告诉piver配置文件的基本信息：名称、扫描的位置以及格式。如果告诉了带有后缀名的文件给viper，那么您就不需要显式地告诉piver文件的格式，它会自动推断。

接着使用`read_in_config()`读取配置文件

最后使用`get()`获取内容，参数为目标键的字符串，层级用`.`分割

```python
import piver

piver.add_config_path(".")     # add current directory to config path
piver.set_config_type("toml")  # set config file type to toml
piver.set_config_name("example")  # set config file name to example
piver.read_in_config()  # read in config file MUST

print(f"Dsn is: {piver.get('database.dsn')}")  # get value of database.dsn

```

## 作者

黄子程

lfcypo(Zicheng Huang)
