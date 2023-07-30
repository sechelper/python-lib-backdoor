import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="backdoor",
    version="1.9.3",
    author="Secself",
    author_email="author@example.com",
    description="Python lib backdoor example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sechelper/python-lib-backdoor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)