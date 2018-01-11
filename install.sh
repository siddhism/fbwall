virtualenv env_fbwall
source env_fbwall/bin/activate
pip install -r requirements.txt
bower install --allow-root
./manage.py migrate
./manage.py createsuperuser
./manage.py collectstatic --no-input
./manage.py runserver 7001
