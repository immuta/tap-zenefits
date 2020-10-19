#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-zenefits",
    version="0.1.0",
    description="Singer.io tap for extracting data from the Zenefits API",
    author="Josh Temple",
    url="https://www.zenefits.com/",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_zenefits"],
    install_requires=[
        "singer-python==5.9.0",
        "requests"
    ],
    entry_points="""
    [console_scripts]
    tap-zenefits=tap_zenefits:main
    """,
    packages=["tap_zenefits"],
    package_data = {
        "schemas": ["tap_zenefits/schemas/*.json"]
    },
    include_package_data=True,
)