# 폴더구조

```
└── app/
    ├── frontend/
    │   ├── Dockerfile
    │   └── 
    ├── docker-compose.yml
    ├── nginx/
    │   ├── Dockerfile
    │   ├── nginx-proxy.conf
    │   └── nginx.conf
    └── backend/
        ├── Dockerfile
        ├── manage.py
        ├── README.md
        ├── requirements.txt
        ├── apps/
        │   ├── ...
        │   └── items/
        │       ├── __init__.py
        │       ├── admin.py
        │       ├── apps.py
        │       ├── models.py
        │       ├── ...
        │       └── migrations/
        │           └── ...
        ├── config/
        │   ├── asgi.py
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── uwsgi.ini
```
