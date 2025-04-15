# Инструкция по запуску проекта

## Первоначальная настройка (выполняется один раз)

1. Установите Homebrew (если еще не установлен):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Установите Python через Homebrew:
```bash
brew install python@3.9
```

3. Создайте виртуальное окружение (если оно еще не создано):
```bash
python3 -m venv my_env
```

## Запуск проекта

Просто запустите скрипт:
```bash
./start.sh
```

После этого сайт будет доступен по адресу: http://127.0.0.1:8000/

## Важно!
- Не удаляйте папку `my_env`
- Не устанавливайте Python через установщик с сайта python.org
- Используйте только Python, установленный через Homebrew
