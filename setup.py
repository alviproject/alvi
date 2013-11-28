from setuptools import setup
from setuptools import find_packages


setup(
    name='alvi',
    version='1.1.1',
    packages=find_packages(),
    author='Piotr Lewalski',
    author_email='piotr@lewalski.pl',
    license='MIT',
    url='https://github.com/alviproject/alvi',
    description='Algorithm Visualization framework',
    long_description='Algorithm Visualization framework',
    install_requires=open("requirements.txt").read().split('\n'),
    tests_require=open("requirements_tests.txt").read().split('\n'),
    test_suite='discover_tests',
    include_package_data=True,
    #platform
    #keywords
    #classifiers
)