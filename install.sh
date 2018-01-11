virtualenv env_fbwall
source env_fbwall/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 7001
