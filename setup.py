import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Camper-Logger-Exception",
    version="0.2.0",
    author="Abdullah KULCU",
    author_email="abdullahkulcu@outlook.com",
    description="Python logging and exception catcher library for lazy peoples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abdullahkulcu/Camper-Logger-Exception",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorlog',
        "requests",
        "raven"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
