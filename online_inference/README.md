
## MLOps hw02

Artem Tkachenko, MADE 2022 fall

### Инструкции

Создать образ локально:

```
docker build -t aitkachenko/hw02:v1 .
```

Забрать образ с hub.docker.com:

```
docker pull aitkachenko/hw02:v1
```

Запустить контейнер на основе образа:

```
docker run --name hw02x -p 18000:18000 aitkachenko/hw02:v1
```

Health check:

```
curl http://localhost:18000/health
```

Скрипт запросов к сервису:

```
python make_request.py
```

Запуск тестов (изнутри контейнера):
```
docker exec -it hw02x bash
python3 -m pytest make_test.py
```

Дополнительно:

Модели скачиваются со своего virtual private server:

```
wget -q -N http://185.87.50.149:8082/model_knn.pkl
wget -q -N http://185.87.50.149:8082/transformer_knn.pkl
```

### Оптимизация размера образа:

* На основе образа ```python:3.9: 1.36GB Mb```
* На основе образа ```python:3.9-slim: 572Mb```
* На основе образа ```python:3.9-slim-buster: 565MB```

```
[usert@fedora mlopshw02a]$ docker image ls
REPOSITORY                TAG                       IMAGE ID       CREATED          SIZE
aitkachenko/hw02b         v0.1                      f47dd7449990   50 seconds ago   1.36GB <--- python:3.9
aitkachenko/hw02a         v0.2                      e9268f28a42a   3 minutes ago    565MB  <--- python:3.9-slim-buster
aitkachenko/hw02          v0.2                      b10b758d6045   46 minutes ago   572MB  <--- python:3.9-slim

```

### Самооценка:

(3/3) 1) Оберните inference вашей модели в rest сервис на FastAPI, должен быть endpoint /predict 

(1/1) 2) Напишите endpoint /health, который должен возращать 200, если ваша модель готова к работе

(3/3) 3) Напишите unit тест для /predict

(2/2) 4) Напишите скрипт, который будет делать запросы к вашему сервису

(4/4) 5) Напишите Dockerfile, соберите на его основе образ и запустите локально контейнер

(2/2) 6) Опубликуйте образ в https://hub.docker.com/, используя `docker push`

(1/1) 7) Опишите в README.md корректные команды `docker pull/run`

(1/1) 8) Проведите самооценку

Дополнительная часть

(1/2) 1) Ваш сервис скачивает модель из S3 или любого другого хранилища при старте, путь для скачивания передается через переменные окружения

(2/2) 2) Оптимизируйте размер docker image

(0/2) 3) Сделайте валидацию входных данных 

20/23 - Итого

