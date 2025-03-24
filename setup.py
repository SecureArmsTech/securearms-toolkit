from setuptools import setup, find_packages

setup(
    name="securearms",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]>=0.7",
    ],
    entry_points={
        "console_scripts": [
            "securearms=securearms.cli:app",
        ],
    },
)
