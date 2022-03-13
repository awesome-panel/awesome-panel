"""We test that urls included in selected files are valid."""
import re

import pytest
import requests

from awesome_panel.assets.yaml import APPLICATIONS_CONFIG_PATH, AWESOME_CONFIG_PATH

# pylint: disable=redefined-outer-name

URLS_TO_SKIP = [
    "https://fr.linkedin.com/in/hyamanieu",
    "https://miro.medium.com/fit/c/262/262/1",
    "https://miro.medium.com/fit/c/96/96/1",
    "https://www.linkedin.com/in/minhnguyen001/",
    "https://www.linkedin.com/in/stephen-kilcommins/",
    "https://miro.medium.com/fit/c/262/262/2",
    "https://miro.medium.com/max/1400/1",
    "https://www.linkedin.com/in/lukas-mosser",
    "https://www.linkedin.com/in/pierreoliviersimonard/?originalSubdomain=fr",
    "https://www.linkedin.com/in/sophiamyang/",
]


def _extract_url_from_file(path):
    with open(path, encoding="utf-8") as file:
        text = file.read()

    urls = re.findall(
        r"(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])",
        text,
    )
    links = [item[0] + "://" + item[1] + item[2] for item in urls]
    return list(set(links))


@pytest.fixture()
def urls():
    """Returns a list of urls to check"""
    links = []
    for path in [AWESOME_CONFIG_PATH, APPLICATIONS_CONFIG_PATH][0:1]:
        links.extend(_extract_url_from_file(path))

    return list(set(list(links)))


@pytest.mark.skip(reason="This test is slow and we run it manually sometimes")
def test_urls(urls):
    """Tests a list of urls"""
    # When
    invalid_urls = []
    for url in urls:
        if url in URLS_TO_SKIP:
            continue

        try:
            response = requests.get(url, verify=False)

            if response.status_code != 200:
                invalid_urls.append(url)
        except requests.exceptions.ConnectionError:
            invalid_urls.append(url)

    # Then
    assert not invalid_urls
