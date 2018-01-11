# Fbwall

### Project Description 
- Message Wall like facebook wall
- Two set of users - Admin and normal user
- Both Users should be able to login using unique credentials
- All Users can create a new post like facebook post on the wall. 
- All Users can Like the different posts.
- Likes cannot be more than once for a user for one post
- Admin can delete any post (we need to createsuperuser who can login to admin panel and delete posts)



## Setting up project and initializing data
Make sure you have python-setuptools, virtualenv & pip installed. 

After that run install.sh form the repository.
```
./install.sh
```
Or setup manually

```
# create a virtualenv 
virtualenv env_fbwall
source env_fbwall/bin/activate
pip install -r reuqirements.txt
bower install --allow-root
./manage.py migrate
./manage.py collectstatic
./manage.py createsuperuser
./manage.py runserver 7001
```

check http://127.0.0.1:7001/