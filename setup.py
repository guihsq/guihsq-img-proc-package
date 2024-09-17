from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img_proc",
    version="0.0.1",
    author="Guilherme Queiroz",
    author_email="guihsq1408@gmail.com",
    description="Image Processing Package - Larning to do packages",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guihsq/guihsq-img-proc-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5"
)
