# setup.py copied from https://github.com/facebookresearch/llama
from pathlib import Path
from setuptools import find_packages, setup

readme_path = Path(__file__).parent / "README.md"

setup(
    name="llama",
    version="0.1.0",
    description="LLM",
    long_description=readme_path.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "torch==2.4.0",
        "tiktoken<0.8",
        "tqdm",
    ],
    python_requires=">=3.9",
)
