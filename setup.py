from setuptools import setup, find_packages

setup(
    name="demo_project",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "pytest",
    ],
    entry_points={
        'console_scripts': [
            'app= app:add',
        ]
    })
