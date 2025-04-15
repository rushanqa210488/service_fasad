#!/bin/bash

# Переходим в директорию проекта
cd "$(dirname "$0")"

# Активируем виртуальное окружение
source my_env/bin/activate

# Переходим в директорию с manage.py
cd fasad

# Запускаем сервер
python3 manage.py runserver 