from setuptools import setup, find_packages

setup(
    name="sorting-techniques",
    version="1.0.2",
    author="Hariesh",
    description="A Python package with modular sorting algorithm implementations.",
    long_description=open("README.md").read(),
    author_email='hariesh28606@gmail.com',
    url='https://github.com/Hariesh28/Sorting-Algorithms-Library',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)
