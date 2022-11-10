# MLOps Course. Homework 1 #

## MADE 2022, fall ##
- - -

[Artem Tkachenko](https://data.mail.ru/profile/art.tkachenko)

## Краткое описание проекта: основные "архитектурные" и тактические решения ##

Для конфигурации используется hydra. Для обучения и предсказания используются модели knn и logistic regression.

### Загрузка данных ###

* Вариант 1. С виртуального сервера (vds):

```mkdir -p data/raw && wget --output-document=data/raw/heart_cleveland_upload.csv http://185.87.50.149:8082/heart_cleveland_upload.csv```

* Вариант 2. С kaggle:

[https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)

```mkdir -p data/raw && unzip archive.zip -d data/raw```

### Предусловия ###

* `Python 3` (`python -V`)
* `venv` (`python -m pip install venv`)

##### Отдельное окружение: #####

```
python -m venv hw01env
source hw01env/bin/activate
```

##### Зависимости: #####

```
python -m pip install -r requirements.txt
pip install -e .
```

### Инструкция ###

##### Установка #####

```
chmod u+x *.sh
```

##### EDA #####

Ноутбук и он же, сохраненный как HTML для удобства:

```
./notebooks/mlops_hw01_eda.ipynb
./notebooks/mlops_hw01_eda.html
```

##### Обучение модели #####

Настройки обучения находятся в файлах ./config/mode/train_knn.yaml и train_logreg.yaml

Скрипты для запуска:
```
./train_logreg.sh
./train_knn.sh
``` 
Результат сохраняется в папку ./models

##### Predict #####

Настройки предиктов находятся в файлах ./config/mode/predict_knn.yaml и predict_logreg.yaml

Скрипты для запуска:
```
./predict_logreg.sh
./predict_knn.sh
```
Результат сохраняется в папку ./predictions

##### Генерация данных ######

```
python ./datagen/data_generator.py
```

### Самооценка ###

0.В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. (1/1)

1.В пулл-реквесте проведена самооценка(1/1)

2.Выполнено EDA (1/1) Скрипт, который сгенерит отчет, закоммитьте и скрипт и отчет (0/1)

3.Написана функция/класс для тренировки модели, вызов оформлен как утилита командной строки, записана в readme инструкцию по запуску (3/3)

4.Написана функция/класс predict (вызов оформлен как утилита командной строки), которая примет на вход артефакт/ы от обучения, тестовую выборку (без меток) и запишет предикт по заданному пути, инструкция по вызову записана в readme (3/3)

5.Проект имеет модульную структуру (2/2)

6.Использованы логгеры (2/2)

7.Написаны тесты на отдельные модули и на прогон обучения и predict (0/3)

8.Для тестов генерируются синтетические данные, приближенные к реальным (2/2)

9.Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3/3)

10.Используются датаклассы для сущностей из конфига, а не голые dict (2/2)

11.Напишите кастомный трансформер и протестируйте его (0/3)

12.В проекте зафиксированы все зависимости (1/1)

13.Настроен CI для прогона тестов, линтера на основе github actions (0/3)

Дополнительные баллы:
* Используйте hydra для конфигурирования - (3/3)
* Mlflow (0/3)
* DVC (0/3)

overall: 1+1+1+3+3+2+2+0+2+3+2+0+1+0+3+0+0 = 24

- - -

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── config             <- configs
    │   ├── dataloader     <- config for dataloader
    │   ├── logging        <- config for logger
    │   └── mode           <- config for train and predict
    │
    ├── data
    │   ├── generated      <- Generated data
    │   └── raw            <- The original, immutable data dump.
    │
    ├── datagen            <- Data generation class
    │
    ├── logs               <- Logs
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks and reports
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data
    │   │   └── dataloader.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predictor.py
    │   │   └── trainer.py


- - -

Настройки на стороне http-сервера, с которого можно скачать датасет:
* Скрипт для запуска сервере: `python3.9 -m http.server 8082`
* Открыть порт: `sudo firewall-cmd --zone=public --add-port=8082/tcp --permanent
`sudo firewall-cmd --reload`
* Добавить скрипт в systemd

