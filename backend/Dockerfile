FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
# docker 안에서 vi 설치 안해도됨
RUN apt-get -y install vim
# docker안에 srv/backend 폴더 생성
RUN mkdir /srv/backend

# 현재 디렉토리를 srv/backend 폴더에 복사
ADD . /srv/backend

# 작업 디렉토리 설정
WORKDIR /srv/backend

# pip 업그레이드
RUN pip install --upgrade pip
# 필수 패키지 설치
RUN pip install -r requirements.txt

#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
