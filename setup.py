from setuptools import setup, find_packages

setup(
    name="sorting-techniques",
    version="1.0.5",
    author="Hariesh R",
    description="A Python package with modular sorting algorithm implementations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author_email='hariesh28606@gmail.com',
    url='https://github.com/Hariesh28/Sorting-Algorithms-Library',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[],
    keywords='sorting algorithms, python, data structures'
)
