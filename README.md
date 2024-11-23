# Валентинки
Сайт для создания анонимных валентинок.

## Настройка
Перед настройкой необходимо сгенерировать `API HASH` и `API_ID`.
Это можно сделать в [my.telegram.org](https://my.telegram.org/) (раздел API development tools).

Далее:
```sh
$ git clone https://github.com/Fazzyt/valentine-sait.git valentine-sait
$ cd valentine-sait
$ cp config_example.json config.json
$ # Отредактируйте config.json
$ python3 -m venv .env
$ . .env/bin/activate  # Каждый раз перед запуском
$ pip install -r requirements.txt
$ python3 -m backend
```
