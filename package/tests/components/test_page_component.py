## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.application.components import PageComponent
from awesome_panel.application.models import Page, Progress, Toast
import param
import panel as pn
import pytest


def test_can_construct_page_component(page_component):
    assert isinstance(page_component, PageComponent)
    assert hasattr(page_component, "main")
    assert hasattr(page_component, "sidebar")
    assert isinstance(page_component.progress, Progress)
    assert isinstance(page_component.toast, Toast)
    assert callable(page_component.create)


def test_can_create_page_component_from_page_component(page_component):
    # When
    actual = PageComponent.create(component=page_component)
    # Then
    assert actual == page_component


def test_can_create_page_component_from_page_component_subclass():
    # Given
    class MyClass(PageComponent):
        pass

    component = MyClass
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, MyClass)


def test_can_create_page_component_from_instance_of_page_component_subclass():
    # Given
    class MyClass(PageComponent):
        pass

    component = MyClass()
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert actual == component


def test_can_create_page_component_from_callable():
    # Given
    def my_func():
        return "A"

    component = my_func
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == my_func()


def test_can_create_page_component_from_class_with_view_func():
    # Given
    class MyClass:
        def view(self):
            return "A"

    component = MyClass
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == component().view()


def test_can_create_page_component_from_instance_with_view_func():
    # Given
    class MyClass:
        def view(self):
            return "A"

    component = MyClass()
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == component.view()


def test_can_create_page_component_from_reactive():
    component = pn.Column("A")
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == component


def test_can_create_page_component_from_string():
    component = "A"
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == component


def test_can_create_page_component_from_class_with_main_and_sidebar():
    # Given
    class MyClass(PageComponent):
        def main(self):
            return "A"

        def sidebar(self):
            return "B"

    component = MyClass
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == "A"
    assert actual.sidebar == "B"


def test_can_create_page_component_from_instance_with_main_and_sidebar():
    # Given
    class MyClass(PageComponent):
        def main(self):
            return "A"

        def sidebar(self):
            return "B"

    component = MyClass()
    # When
    actual = PageComponent.create(component=component)
    # Then
    assert isinstance(actual, PageComponent)
    assert actual.main == "A"
    assert actual.sidebar == "B"
