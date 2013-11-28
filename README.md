AlVi: Algorithm Visualization framework
================================
[![Build Status](https://travis-ci.org/alviproject/alvi.png?branch=master)](https://travis-ci.org/alviproject/alvi)
[![Coverage Status](https://coveralls.io/repos/alviproject/alvi/badge.png)](https://coveralls.io/r/alviproject/alvi)

## Requirements:
* Linux/MacOS
* Python 3.2
* virtualenv

## Setting up a development version:
```bash
git clone https://github.com/alviproject/alvi.git
cd alvi
./create_dev_env.sh     # setup virtualenv, install requirements
source env/bin/activate # activate virtualenv
python setup.py test    # run tests (optional)
python -m alvi.server   # run the server
```

## Screens:
![Insertion Sort](https://raw.github.com/alviproject/alvi/master/screens/insertion_sort.png)

![Tree](https://raw.github.com/alviproject/alvi/master/screens/tree.png)

![Graph](https://raw.github.com/alviproject/alvi/master/screens/graph.png)