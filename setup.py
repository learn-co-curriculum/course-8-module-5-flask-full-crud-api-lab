from setuptools import setup, find_packages

setup(
    name="event-api",
    version="1.0.0",
    description="Flask Event Management REST API",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0",
    ],
    python_requires=">=3.7",
)
