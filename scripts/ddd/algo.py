# (Name, Drunkfactor, Subs=[])

from typing import List, Optional, Dict


class Person:
    def __init__(self, name: str, drunk_factor: int, leader_name: Optional[str]):
        self.name = name
        self.drunk_factor = drunk_factor
        self.leader_name = leader_name
        self.subs: List["Person"] = []
        self._max_drunk_factor_tree = None
        self._max_communication_time_tree = None

    @staticmethod
    def create_from_line(line: str) -> "Person":
        split = line.split(" ")
        if len(split) == 2:
            return Person(split[0], int(split[1]), None)
        if len(split) == 3:
            return Person(split[0], int(split[1]), split[2])

    @staticmethod
    def create_from_lines(lines: str) -> Dict[str, "Person"]:
        persons = {}
        for person in (Person.create_from_line(line) for line in lines.splitlines()):
            persons[person.name] = person

        for person in persons.values():
            if person.leader_name:
                persons[person.leader_name].subs.append(person)
        return persons

    @classmethod
    def create_from_input(cls) -> Dict[str, "Person"]:
        n = int(input())
        lines = []
        for _ in range(n):
            lines.append(input())

        return cls.create_from_lines("\n".join(lines))

    @property
    def max_drunk_factor_tree(self) -> int:
        if self._max_drunk_factor_tree:
            return self._max_drunk_factor_tree

        if not self.subs:
            return self.drunk_factor

        self._max_drunk_factor_tree = self.drunk_factor + max(
            (person.max_drunk_factor_tree) for person in self.subs
        )
        return self._max_drunk_factor_tree

    @property
    def max_communication_time_tree(self) -> int:
        if self._max_communication_time_tree:
            return self._max_communication_time_tree

        if not self.subs:
            return 0
        if len(self.subs) == 1:
            if self.subs[0].max_communication_time_tree > 0:
                return self.subs[0].max_communication_time_tree
            return self.max_drunk_factor_tree

        drunk_factor_highest = 0
        drunk_factor_second_highest = 0
        max_communication_time_sub_tree = 0

        for person in self.subs:
            if person.max_drunk_factor_tree > drunk_factor_highest:
                drunk_factor_second_highest = drunk_factor_highest
                drunk_factor_highest = person.max_drunk_factor_tree
            elif person.max_drunk_factor_tree > drunk_factor_second_highest:
                drunk_factor_second_highest = person.max_drunk_factor_tree

            if person.max_communication_time_tree > max_communication_time_sub_tree:
                max_communication_time_sub_tree = person.max_communication_time_tree

        max_communication_time_two_subs = (
            self.drunk_factor + drunk_factor_highest + drunk_factor_second_highest
        )

        self._max_communication_time_tree = max(
            max_communication_time_sub_tree, max_communication_time_two_subs
        )
        return self._max_communication_time_tree

    @property
    def is_leader(self) -> bool:
        return self.leader_name is None

    def __str__(self):
        if self.is_leader:
            return self.name + " " + str(self.drunk_factor)
        return self.name + " " + str(self.drunk_factor) + " " + self.leader_name

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    persons = Person.create_from_input()
    leader_name = list(persons)[0]
    leader = persons[leader_name]
    print(leader.max_communication_time_tree)
