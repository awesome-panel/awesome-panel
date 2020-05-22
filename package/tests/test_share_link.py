"""Test of functionality in the share_link module"""
# pylint: disable=redefined-outer-name,protected-access
from awesome_panel.express.fontawesome import share_link


def test_base():
    """Test that the ShareOnBase link works"""
    # Given
    url = "http://google.com"

    class ShareOnTest(share_link.ShareOnBase):
        "Helper Test Class"

        @property
        def href(self,):
            return "test"

    base = ShareOnTest(url=url)
    # Then
    assert base.url == url
    assert base._url_parsed == "http%3A%2F%2Fgoogle.com"
    assert base.href == "test"
    assert base.__html__() == (
        '<a href="test" '
        'class="button-share-link">'
        '<i class="fas fa-external-link-alt"></i></a>'
    )


def test_facebook():
    """Test that the ShareOnFacebook link works"""
    # Given
    url = "https://awesome-panel.org"
    facebook = share_link.ShareOnFacebook(url=url)
    # Then
    assert facebook.url == url
    assert facebook._url_parsed == "https%3A%2F%2Fawesome-panel.org"
    assert (
        facebook.href
        == "https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fawesome-panel.org"
    )
    assert facebook.__html__() == (
        '<a href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fawesome-panel.org" '
        'class="button-share-link">'
        '<i class="fab fa-facebook-f"></i></a>'
    )


def test_linked_in():
    """Test that the ShareOnLinkedIn link works"""
    # Given
    url = "https://awesome-panel.org"
    linkedin = share_link.ShareOnLinkedIn(url=url)
    # Then
    assert linkedin.url == url
    assert linkedin._url_parsed == "https%3A%2F%2Fawesome-panel.org"
    assert linkedin.href == (
        "http://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fawesome-panel.org&"
        "title=Checkout"
    )
    assert linkedin.__html__() == (
        '<a href="http://www.linkedin.com/shareArticle?mini=true&'
        'url=https%3A%2F%2Fawesome-panel.org&title=Checkout" '
        'class="button-share-link">'
        '<i class="fab fa-linkedin-in"></i></a>'
    )


def test_twitter():
    """Test that the ShareOnLinkedIn link works"""
    # Given
    twitter = share_link.ShareOnTwitter()
    assert twitter.href == (
        "https://twitter.com/intent/tweet?url=https%3A%2F%2Fawesome-panel.org&text=Checkout"
    )


def test_reddit():
    """Test that the ShareOnReddit link works"""
    # Given
    twitter = share_link.ShareOnReddit()
    assert twitter.href == (
        "https://reddit.com/submit?url=https%3A%2F%2Fawesome-panel.org&amp;title=Checkout"
    )
