from setuptools import setup, find_packages # type: ignore

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="img_pakeage",
    version="0.0.1",
    author="Jonas",
    description="Image processing package using skimage.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jon-nas/package.git", 
    packages=find_packages(),
)