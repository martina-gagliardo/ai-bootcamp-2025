#Implementclass Entry:
class Entry:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def matches(self, keyword):
        return keyword in self.name or (self.phone and keyword in self.phone)


class Person(Entry):
    def __init__(self, name, surname, phone=None):
        super().__init__(name, phone)
        self.surname = surname

    def matches(self, keyword):
        return super().matches(keyword) or keyword in self.surname


class Business(Entry):
    pass


class Directory:
    def __init__(self):
        self.entries = {}

    def __len__(self):
        return len(self.entries)

    def add(self, entry):
        self.entries[entry.name] = entry

    def query(self, name):
        return [self.entries[name]] if name in self.entries else []

    def find(self, keyword):
        return [entry for entry in self.entries.values() if entry.matches(keyword)]

