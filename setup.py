# setup.py copied from https://github.com/huggingface/accelerate
from setuptools import find_packages, setup

setup(
    name="accelerate",
    version="0.0.0",
    description="Hugging Face Accelerate",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["accelerate*"]),
    install_requires=[
        "torch>=1.10.0",
        "huggingface-hub>=0.21.0",
        "safetensors",
        "PyYAML",
        "tqdm",
        "numpy>=1.17",
        "packaging>20",
        "psutil",
    ],
    python_requires=">=3.8",
)
