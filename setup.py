"""Setup file. The package can be installed for development by running

pip install -e .
"""
import pathlib

from setuptools import find_packages, setup

README_FILE_PATH = pathlib.Path(__file__).parent / "README.md"
with open(README_FILE_PATH, encoding="utf8") as f:
    README = f.read()

s = setup(  # pylint: disable=invalid-name
    name="awesome-panel",
    version="20200512.1",
    license="MIT",
    description="""This package supports the Awesome Panel Project""",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/MarcSkovMadsen/awesome-panel",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    include_package_data=True,
    packages=find_packages(include=["awesome_panel", "awesome_panel.*"]),
    install_requires=["panel>=0.12.6"],
    python_requires=">= 3.7",
    zip_safe=False,
)
