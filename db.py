import model
import storage

class DBException(Exception):
    pass

class FileDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def get_conn(self):
        try:
            return self._file_db.get_conn()
        except Exception as ex:
            raise DBException(f"Ошибка операции подключения, {ex}")

    def upload_db(self):
        try:
            return self._storage.upload_db()
        except Exception as ex:
            raise DBException(f"Ошибка операции загрузки, {ex}")

    def list_db(self):
        try:
            return self._storage.list_db()
        except Exception as ex:
            raise DBException(f"Ошибка операции открытия таблицы, {ex}")

    def get_stats(self):
        try:
            return self._storage.get_stats()
        except Exception as ex:
            raise DBException(f"Ошибка операции анализа, {ex}")

    def clean_data(self):
        try:
            return self._storage.clean_data()
        except Exception as ex:
            raise DBException(f"Ошибка операции очистки, {ex}")