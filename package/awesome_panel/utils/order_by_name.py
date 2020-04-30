class OrderByNameMixin():
    def __lt__(self, other):
        return self.name.casefold() < other.name.casefold()

    def __eq__(self, other):
        return self.name == other.name

