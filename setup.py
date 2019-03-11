#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.rst') as f:
    desc = f.read()

setup(
    name='corona',
    version='0.1.2',
    description='Website Screenshot Utility',
    long_description=desc,
    url='https://github.com/pyarmory/corona',
    author='John Vrbanac',
    author_email='john.vrbanac@linux.com',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='screenshot website',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    python_requires='>=3.6',
    install_requires=[
        'pyppeteer==0.0.25',
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'corona = corona.__main__:main',
        ],
    },
)
