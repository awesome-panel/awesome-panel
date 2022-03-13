"""We test that urls included in selected files are valid."""
import re

import pytest
import requests

from awesome_panel.assets.yaml import APPLICATIONS_CONFIG_PATH

# pylint: disable=redefined-outer-name

URLS_TO_SKIP = ["https://www.linkedin.com/in/stephen-kilcommins/"]


def _extract_url_from_file(path):
    with open(path) as file:
        text = file.read()
    
    urls = re.findall('(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', text)
    links = [item[0]+"://"+item[1]+item[2] for item in urls]
    return list(set(links))


@pytest.fixture()
def urls():
    """Returns a list of urls to check"""
    return _extract_url_from_file(APPLICATIONS_CONFIG_PATH)


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
    breakpoint()
