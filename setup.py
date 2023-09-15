from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="DogSegmentation",
    version="0.0.1",
    author="Paras Kapoor",
    description="Image segmentation of Dogs",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/kapoorparas09/Dog-Segmentation",
    author_email="kapoorparas0001@gmail.com",
    packages=find_packages(),
    install_requires=[
        "ultralytics",
        "from-root",
        "dill",
        "gdown",
        "flask",
        "flask-cors"
    ]
)