# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
def test_can_construct_resource(resource):
    assert hasattr(resource, "name")
    assert hasattr(resource, "url")
    assert hasattr(resource, "thumbnail_png_path")
    assert hasattr(resource, "is_awesome")
    assert hasattr(resource, "tags")
    assert hasattr(resource, "author")
    assert hasattr(resource, "description")

    assert callable(resource.to_markdown_bullet)
    assert isinstance(type(resource).screenshot_file, property)

    assert (
        resource.to_markdown_bullet()
        == "- [Panel](https://panel.pyviz.org/) by [panel](https://panel.pyviz.org/) (#Panel)"
    )
    assert resource.screenshot_file == "panel.png"
