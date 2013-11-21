ENV=env

rm -rf $ENV
virtualenv --clear -p python3 $ENV
source $ENV/bin/activate
pip install -r requirements.txt
pip install -r requirements_tests.txt

echo
echo Virtualenv was created, run \"source $ENV/bin/activate\" to activate it.