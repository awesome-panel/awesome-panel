class OrderByNameMixin():
    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

