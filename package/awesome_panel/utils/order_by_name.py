"""In this module we define the OrderByNameMixin.

The OrderByNameMixin adds ordering by the name parameter to a Class"""


class OrderByNameMixin:
    """The OrderByNameMixin adds ordering by the name parameter to a Class"""

    def __lt__(self, other):
        if hasattr(other, "name"):
            return self.name.casefold() < other.name.casefold()
        return True

    def __eq__(self, other):
        if hasattr(other, "name"):
            return self.name == other.name
        return False
