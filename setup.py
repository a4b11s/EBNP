from io import open
from setuptools import setup, find_packages

"""
This is the setup script for the package.
:author: 2024 by Artem Bazyl
:license: MIT
"""

version = "0.0.1"

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ebnp",
    version=version,
    packages=find_packages(),
    url="",  # URL to the package's web page
    license="MIT",
    author="Artem Bazyl",
    description="Event Based Network Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={"ebnp": ["py.typed"]},
    package_dir={"ebnp": "ebnp"},
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
