import model

class StorageException(Exception):
    pass

class LocalStorage:
    def __init__(self):
        self.id_counter = 0
        self._storage = {}

    def upload_db(self, file: model.DF) -> str:
        self.id_counter += 1
        file.id = str(self.id_counter)
        self._storage[file.id] = file
        return file.id

    def list_db(self):
        return list(self._storage.values())

    def get_stats(self):
        if self.id_counter == 0:
            raise StorageException("Ошибка хранилища")
        return list(self._storage.values())

    def clean_data(self):
        if self.id_counter == 0:
            raise StorageException("Ошибка хранилища")
        return list(self._storage.values())



























    def upload(self, file: model.DF) -> str:
        file.id = str(self._id_counter)
        self._storage[file.id] = file
        return file.id

    def list(self) -> List[model.DF]:
        return list(self._storage.values())

    def get_stats(self) -> List[model.DF]:
        return self._storage[_id]

    def clean_data(self) -> List[model.DF]:
        file.id = _id
        self._storage[file.id] = file