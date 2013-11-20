AlVi: Algorithm Visualization framework
================================

## Requirements:
* Linux
* Python 3.2
* virtualenv

## Setting up development version:
```bash
git clone https://github.com/alviproject/alvi.git
cd alvi
virtualenv --clear -p python3 env   # setup virtualenv, install requirements
source env/bin/activate             # activate virtualenv
python setup.py develop             # install required packages
python -m alvi.server               # run the server (by default listens at http://locahost:8000)
```

## Screens:
![Insertion Sort](https://raw.github.com/alviproject/alvi/master/screens/insertion_sort.png)

![Tree](https://raw.github.com/alviproject/alvi/master/screens/tree.png)

![Graph](https://raw.github.com/alviproject/alvi/master/screens/graph.png)