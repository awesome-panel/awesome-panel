## # pylint: disable=redefined-outer-name,protected-access, missing-function-docstring
from awesome_panel.application.models import Author


def test_can_construct_author(author):

    assert isinstance(author.name, str)
    assert isinstance(author.url, str)
    assert isinstance(author.github_url, str)
    assert isinstance(author.github_avatar_url, str)
    assert str(author) == author.name
    assert repr(author) == author.name
    assert author._repr_html_(width="21x", height="22px") == '<a href="https://github.com/holoviz/" title="Author: panel" target="_blank"><img application="https://avatars2.githubusercontent.com/u/51678735" alt="panel" style="border-radius: 50%;width: 21x;height: 22px;vertical-align: text-bottom;"></img></a>'
