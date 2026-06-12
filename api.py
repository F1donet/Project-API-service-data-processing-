from flask import Flask
from logic import DBLogic

_file_logic = DBLogic()

class ApiException(Exception):
    pass

_file_logic.get_conn()
app = Flask(__name__)
API_ROOT = '/api/v1'
DB_API_ROOT = API_ROOT + '/db'

@app.route(DB_API_ROOT + '/upload/', methods=['POST'])
def upload_db():
    try:
        _file_logic.upload_db()
        return f" Файл загружен в базу", 201
    except Exception as ex:
        return f"Ошибка загрузки файла: {ex}. Проверьте,корректно ли указано имя файла", 404

@app.route(DB_API_ROOT + '/', methods=['GET'])
def list_db():
    try:
        _file_logic.list_db()
        return f"Отображение данных", 200
    except Exception as ex:
        return f"Ошибка отображения файлов: {ex}", 404

@app.route(DB_API_ROOT + '/data/stats/', methods=['GET'])
def get_stats():
    try:
        _file_logic.get_stats()
        return f"Аналитика по загруженным данным", 200
    except Exception as ex:
        return f"Ошибка в анализе данных: {ex}", 404

@app.route(DB_API_ROOT + '/data/clean/', methods=['GET'])
def clean_data():
    try:
        _file_logic.clean_data()
        return f" Таблица очищена от дубликатов и заполнены пустые ячейки", 200
    except Exception as ex:
        return f"Ошибка при очистке таблицы: {ex}", 404