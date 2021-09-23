# react-django-nginx-dockercompose

🎁 Default project template configuring backend and frontend through nginx in AWS EC2



## USED
- aws ec2
- reactjs
- django
- docker
- nginx
- docker-compose

-----

## How to use
1. Get this project for work in your repository space
2. Open the terminal on your laptop.
3. Move your path to where you want.
4. enter command, `git clone https://https://github.com/{Your workspace}/web-service-basic-template`
5. You need to install a few things.
    - python3
    - python3-pip
    - django
    - docker
    - docker-compose
    - nodejs
    - npm, yarn
6. If the installation is finished, type `docker-compose up-d --build` in the terminal.
7. Finally, you can enter the host of the project in your browser.

-----

## Connect DB(Mysql)
### make directory db
```
app$ mkdir db
```

### make file .env
```
app$ vi .env  

# app/.env
MYSQL_ROOT_PASSWORD=password
MYSQL_DATABASE=dbname
MYSQL_ROOT_USER=rootusername
MYSQL_PASSWORD=password
```

### edit file docker-compose.yml 
```
# docker-compose.yml
    backend:
        ...
        depends_on:
            - db
    ...
    db:
        container_name: db
        image: mysql:latest
        restart: always
        ports:
            - "3306:3306"
        env_file: .env
        command:
            - --character-set-server=utf8mb4
            - --collation-server=utf8mb4_unicode_ci
            - --lower_case_table_names=1
        volumes:
            - ./db/data:/var/lib/mysql
```
### make file env.py in config/
```
# app/backend/config$ vi env.py  

SECRET_KEY = 'django secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '0.0.0.0',
        'NAME': 'name',
        'USER': 'username',
        'PASSWORD': 'password',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4'
        }
    }
}

```

### edit backend settings.py
```
from . import env
...
SECRET_KEY = env.SECRET_KEY
...
DATABASES = env.DATABASES
```

-----

## Folder structure

```
└── app/
    ├── frontend/
    │   ├── Dockerfile
    │   └── ...
    ├── nginx/
    │   ├── Dockerfile
    │   ├── nginx-proxy.conf
    │   └── nginx.conf
    └── backend/
    │   ├── Dockerfile
    │   ├── manage.py
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── apps/
    │   │   ├── ...
    │   │   └── items/
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── models.py
    │   │       ├── ...
    │   │       └── migrations/
    │   │           └── ...
    │   ├── config/
    │   │   ├── asgi.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   ├── env.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   └── uwsgi.ini
    ├── README.md
    ├── .env
    ├── .gitignore
    └── docker-compose.yml
```
