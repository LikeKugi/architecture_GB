from .File import File


class Database:
    _instance = None

    files = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        return self._instance

    def load(self, name: str):
        return self.files.get(name)

    def save(self, file: File):
        self.files[file.name] = file

    def view_projects(self) -> list[str]:
        return list(self.files.keys())
