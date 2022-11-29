# YaCut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам

Доступны web и api интерфейсы.

## Технологии
- Python
- Flask
- Jinja2
- SQLAlchemy
### Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/SergeyViskov/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл настроек окружения:
```
touch .env
```
Заполнить его:
```
FLASK_APP=yacut
FLASK_ENV=production
DATABASE_URI=<sqlite:///db.sqlite3>
SECRET_KEY=<Your secret key>
```
Запустить:
```
flask run
```
### Об авторе:
    
    Висков Сергей Николаевич
    Ученик Яндекс-практикума, когорта №9 +