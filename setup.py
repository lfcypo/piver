import setuptools

NAME = "piver"
DESCRIPTION = """
A Python library for reading and managing configuration files.
""".replace("\n", "")

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    LONG_DESCRIPTION.replace(r"*README.md also provides a [Chinese version](./README-zh.md)*", "")

setuptools.setup(
    name=NAME,
    version="0.0.1",
    author="lfcypo",
    author_email="lfcypo@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/lfcypo/piver",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['toml']
)
