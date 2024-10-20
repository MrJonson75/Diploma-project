Чтобы установить эти библиотеки, введите

pip install -r requirements.txt

в своем терминале

После установки Alembic мы можем перейти в корневую папку,
где находится файл main.py, и выполнить команду


alembic init alembic

alembic будет создавать пустые файлы миграции при выполнении команды:


alembic revision --autogenerate -m «первый коммит»

Вы можете найти сгенерированный файл в alembic/versions/

alembic revision --autogenerate -m "create user and blog table migrations"
alembic upgrade head


Панель навигации · Bootstrap v5.3 (getbootstrap.com)


https://getbootstrap.com/docs/5.3/components/navbar/