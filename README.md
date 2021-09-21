# react-django-nginx-dockercompose

🎁 Default project template configuring backend and frontend through nginx in AWS EC2



## USED
- aws ec2
- reactjs
- django
- docker
- nginx
- docker-compose



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
    │   ├── backend/
    │   │   ├── asgi.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   └── uwsgi.ini
    ├── README.md
    ├── .gitignore
    └── docker-compose.yml
```
