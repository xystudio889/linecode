from setuptools import setup, find_packages
import sys

data_files = []
if sys.platform == "win32":
    data_files = [('Scripts',[])]

with open("README.md",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name = "linecode",
    version = "0.1.3",
    packages = find_packages(),
    install_requires = [],
    python_requires = ">=3.8",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "A simple python based language.It can be embedded in python projects",
    long_description = long_description,
    license = "MIT",
    url = "https://github.com/xystudio889/linecode",
    data_files = data_files,
    include_package_data = True
)
