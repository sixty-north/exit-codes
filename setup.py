import io
import os
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.rst', mode='rt')

setup(
    name='exit_codes',
    version=find_version('exit_codes/version.py'),
    packages=find_packages(exclude=['tests']),

    author='Sixty North AS',
    author_email='austin@sixty-north.com',
    description='Platform-independent exit codes.',
    license='MIT',
    keywords='',
    url='http://github.com/sixty-north/exit-codes',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    platforms='any',
    include_package_data=True,
    install_requires=[],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        'test': ['pytest', 'tox'],
    },
    long_description=long_description,
)
