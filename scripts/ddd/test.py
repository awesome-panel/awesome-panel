import pytest

from .algo import Person

INPUT0 = """\
Mirko 6
Mortin 3 Mirko
Josefine 5 Mirko"""

OUTPUT0 = 14

INPUT1 = """\
Mirko 6
Mortin 3 Mirko
Josefine 5 Mirko
John 17 Mirko
Gustav 12 Josefine
Sarah 7 Josefine"""
OUTPUT1 = 40

INPUT2 = """\
Maria 10
Peter 5 Maria
Christian 6 Peter
Kirsten 13 Peter
Tina 21 Christian
Mads 31 Christian"""

OUTPUT2 = 58


def test_create_from_line_leader():
    line = "Mirko 6"
    person = Person.create_from_line(line)
    assert person.name == "Mirko"
    assert person.drunk_factor == 6
    assert person.leader_name is None
    assert line == str(person)


def test_create_from_line_non_leader():
    line = "Mortin 3 Mirko"
    person = Person.create_from_line(line)
    assert person.name == "Mortin"
    assert person.drunk_factor == 3
    assert person.leader_name == "Mirko"
    assert line == str(person)


def test_create_from_lines_1():
    actual = Person.create_from_lines(INPUT1)
    assert "\n".join([str(person) for person in actual.values()]) == INPUT1
    assert len(actual["Mirko"].subs) == 3
    assert len(actual["Josefine"].subs) == 2


def test_drunk_factor_no_subs():
    # Given: person with no subs
    person = Person("A", 2, "B")
    # When
    actual = person.max_drunk_factor_tree
    # Then
    assert actual == 2


def test_drunk_factor_one_subs():
    # Given: person with no subs
    person1 = Person("A", 2, "B")
    person2 = Person("C", 3, "D")
    person1.subs.append(person2)
    # When
    actual = person1.max_drunk_factor_tree
    # Then
    assert actual == 5


def test_drunk_factor_two_subs():
    # Given: person with no subs
    person1 = Person("A", 2, "B")
    person2 = Person("C", 3, "D")
    person3 = Person("E", 4, "F")
    person1.subs.append(person2)
    person1.subs.append(person3)
    # When
    actual = person1.max_drunk_factor_tree
    # Then
    assert actual == 6


def test_drunk_factor_three_subs():
    # Given: person with no subs
    person1 = Person("A", 2, "B")
    person2 = Person("C", 3, "D")
    person3 = Person("E", 4, "F")
    person4 = Person("G", 5, "H")
    person1.subs.append(person2)
    person1.subs.append(person3)
    person1.subs.append(person4)
    # When
    actual = person1.max_drunk_factor_tree
    # Then
    assert actual == 7


@pytest.mark.parametrize(
    ["input", "expected"], [(INPUT0, OUTPUT0), (INPUT1, OUTPUT1), (INPUT2, OUTPUT2),]
)
def test_max_communication_time_tree_0(input, expected):
    persons = Person.create_from_lines(input)
    leader_name = list(persons)[0]
    leader = persons[leader_name]
    assert leader.max_communication_time_tree == expected


def test_max_communication_time_tree_1():
    persons = Person.create_from_lines(INPUT1)

    assert persons["Josefine"].max_drunk_factor_tree == 12 + 5
    assert persons["Josefine"].max_communication_time_tree == 12 + 5 + 7

    assert persons["Mirko"].max_drunk_factor_tree == 12 + 5 + 6
    assert persons["Mirko"].max_communication_time_tree == (12 + 5) + 6 + (17)


def test_max_communication_time_tree_2():
    persons = Person.create_from_lines(INPUT2)

    assert persons["Tina"].max_drunk_factor_tree == 21
    assert persons["Tina"].max_communication_time_tree == 0

    assert persons["Mads"].max_drunk_factor_tree == 31
    assert persons["Mads"].max_communication_time_tree == 0

    assert persons["Christian"].max_drunk_factor_tree == 6 + 31
    assert persons["Christian"].max_communication_time_tree == 21 + 6 + 31

    assert persons["Kirsten"].max_drunk_factor_tree == 13
    assert persons["Kirsten"].max_communication_time_tree == 0

    assert persons["Peter"].max_drunk_factor_tree == 31 + 6 + 5
    assert persons["Peter"].max_communication_time_tree == 21 + 6 + 31

    assert persons["Maria"].max_drunk_factor_tree == 31 + 6 + 5 + 10
    assert persons["Maria"].max_communication_time_tree == 21 + 6 + 31

