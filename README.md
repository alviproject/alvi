AlVi: Algorithm Visualization framework
================================

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