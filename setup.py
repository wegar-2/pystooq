from setuptools import setup, find_packages
import os
import io
import pathlib


setup(
    name="pystooq",
    version="1.0.2",
    description="Package for fetching of data from Stooq.com",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
    author="Artur Wegrzyn",
    packages=find_packages(),
    install_requires=[
        "coloredlogs>=15.0.1",
        "humanfriendly>=10.0",
        "numpy>=1.23.0",
        "pandas>=2.0.3",
        "python-dateutil>=2.8.2",
        "pytz>=2023.3",
        "six>=1.16.0",
        "tzdata>=2023.3"
    ]
)
