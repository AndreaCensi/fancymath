import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "fancymath",
    version = "1.0",
    author = "Andrea Censi",
    author_email = "censi@mit.edu",
    description = ("Unicode math for the lazy TeXnician"),
    license = "GPL",
    keywords = "latex math unicode",
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['fancymath'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],

    entry_points={
     'console_scripts': [
        'fancymath = fancymath:fancymath_main',
        ]
    }
)
