"""How do I use static typing tools like pylint and VS Code language server intellisense with param
and panel?"""
import param


class Child(param.Parameterized):
    "Example Class"


class Parent(param.Parameterized):
    "Example Class"
    child = param.ClassSelector(class_=Child)
    lst = param.List()


def main():
    child = Child()
    parent = Parent(child=child)

    parent.child.name = "I'm a child"
    parent.lst = ["a", "b", "c"]
    print(parent.list[1])

main()
