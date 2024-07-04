from setuptools import setup, find_packages

setup(
    name="mkdoc_toy",
    version="0.1",
    package_dir={"": "project"},
    packages=find_packages(where="project"),
)