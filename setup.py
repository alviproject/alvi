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
    install_requires=[
        'django==1.6',
        'tornado==3.1.1',
        'sockjs-tornado==1.0.0',
    ],
    tests_require=[
        'selenium==2.37.2',
        'coverage==3.7',
    ],
    test_suite="alvi.tests",
    include_package_data=True,
    #platform
    #keywords
    #classifiers
)