class File:

    def __init__(self, name, /, *args, **kwargs):
        self._name = name
        self.props = {'entities': [*args], **kwargs}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str)
        self._name = value

    def get_props(self):
        return list(self.props.keys())

    def get_entities(self):
        return self.props.get('entities')

