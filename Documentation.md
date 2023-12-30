# Python Virtual Environment

Create a python virtual environment:
```shell
python -m venv <name_of_virtual_environment>
```
For 'name_of_virtual_environment', we used 'venv'.

Activate Virtual Environment:
```shell
source venv/bin/activate
```

# Packages to Install

Install the following
```shell
pip install django
pip install -U channels["daphne"]
```

# Create a Django Project

1. Create a new project:
```shell
django-admin startproject <name_of_project> .
```
2. Create an application:
```shell
python manage.py startapp <name_of_app>
```

3. Prepare your django application code.

4. Create requirements.txt file:
```shell
pip freeze > requirements.txt
```
5. Install packages from requirements.txt file:
```shell
pip install -r requirements.txt
```

# GitHub

To initialize git:
```shell
git init
```

Connect with remote repository:
```shell
git remote add origin https://github.com/fabeha-raheel/AEEL-Ros-WebApp-Server-1.0.git
```

Create a branch in remote repository:
```shell
git branch -M master
```
Add modifications:
```shell
git add .
```
Commit changes:
```shell
git commit -m 'comments'
```

Push to remote repo:
```shell
git push -u origin master
```
Pull request from master:
```shell
git pull origin master
```