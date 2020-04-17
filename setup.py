import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-guzi", # Replace with your own username
    version="0.0.1",
    author="Guillaume Dubus",
    author_email="Guillaume1.dubus@gmail.com",
    description="A light library to use Guzi in python application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuziEconomy/python-guzi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# Note : upload command :
#
# $ python3 -m twine upload  --repository-url https://upload.pypi.org/legacy/ dist/*
#
# For mor details, see https://packaging.python.org/tutorials/packaging-projects/