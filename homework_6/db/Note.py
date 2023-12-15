class Note:

    def __init__(self, title: str, details: str):
        self.title = title
        self.details = details

    def __str__(self):
        return f'Name: {self.title}\n\t Title: {self.details}'
