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
git branch -M main
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
git push -u origin main
```
Pull request from master:
```shell
git pull origin main
```

# Tailwind Installation Steps

Install the django-tailwind and browser_reloads package via pip:
```bash
python -m pip install django-tailwind
python -m pip install 'django-tailwind[reload]'
```

Add 'tailwind' to INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
]
```

Create a Tailwind CSS compatible Django app, I like to call it theme:
```bash
python manage.py tailwind init
```

Add your newly created 'theme' app to INSTALLED_APPS in settings.py
```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme'
]
```
Register the generated 'theme' app by adding the following line to settings.py file:
```python
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]
```

Before the next step, make sure you have nodejs and npm installed.

Check nodejs version:
```bash
node -v
```
Upgrade nodejs:
```bash
sudo apt upgrade nodejs
```
Install the latest version:
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

sudo apt install curl

source ~/.bashrc

nvm ls-remote

nvm install node

nvm use node

node -v
```

Check npm version:
```bash
npm -v
```
Install npm latest version:
```bash
npm install -g npm@latest
npm -v
```

Run the next command. Install Tailwind CSS dependencies:
```bash
python manage.py tailwind install
```

add and configure django_browser_reload to list of INSTALLED_APPS in settings.py:
```python
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme',
  'django_browser_reload'
]
```
Add the following in MIDDLEWARE:
```python
MIDDLEWARE = [
  # ...
  "django_browser_reload.middleware.BrowserReloadMiddleware",
  # ...
]
```

Include django_browser_reload URL in your root url.py
```python
from django.urls import include, path
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]
```

Finally, you should be able to use Tailwind CSS classes in HTML. Start the development server by running the following command in your terminal:
```bash
python manage.py tailwind start
```

Ref: https://django-tailwind.readthedocs.io/en/latest/installation.html

