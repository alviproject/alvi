ENV=env
virtualenv --clear -p python3 $ENV
source $ENV/bin/activate
pip install -r requirements.txt
