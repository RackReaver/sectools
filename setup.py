from setuptools import setup

# Read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

# Extract description from line three of README.md
description = README.split('\n')[2].strip()


setup(
    name='sectools',
    version='0.0.1',
    url='https://github.com/RackReaver/sectools',
    license='Apache License',
    author='Matt Ferreira',
    author_email='rackreaver@gmail.com',
    description=description,
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    include_package_data=True,
    install_requirements=[]
)