from Database import File, Database


class Editor:
    _instance = None
    file = None
    db = Database().connect()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Editor, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def show_project_settings(self):
        for key in self.file.get_props():
            print(key)

    def save_project(self):
        self.db.save(self.file)

    def load_project(self, file: File):
        self.file = file

    def print_entities(self):
        print('print all entities: ')
        for entity in self.file.get_entities():
            print(entity)

    def render_models(self):
        print(f'rendering models in file {self.file.name}')

    def render_all_models(self):
        print(f'rendering textures in file {self.file.name}')
