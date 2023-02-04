## Телеграм-бот для мониторинга курсов валют на сайте bestchange.ru

#### Окружение проекта
- python 3.10.6
- aiogram 2.24
- bestchange-api 3.1.0.0


#### Запуск проекта
1. Склонировать репозиторий

`git clone git@github.com:romses1906/BestChangeBot.git`

2. Перейти в папку:

`cd parser_bestchange`

3. Создать и активировать виртуальное окружение Python:

`python -m venv venv`

`venv\Scripts\activate.bat` - для Windows;

`source venv/bin/activate` - для Linux и MacOS.

4. Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

5. В корне проекте создать `.env` по примеру из `.env.example`. Получить токен от `@BotFather`, вставить в `.env`

6. Запустить бота:

`python main.py`