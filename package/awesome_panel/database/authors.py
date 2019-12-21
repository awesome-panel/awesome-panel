"""This module contains the list of Authors"""
from awesome_panel.shared.models import Author

# Authors
PANEL_AUTHOR = Author(
    name="panel",
    url="https://panel.pyviz.org/",
    github_url="https://github.com/holoviz/",
    github_avatar_url="https://avatars2.githubusercontent.com/u/51678735",
)
MARC_SKOV_MADSEN = Author(
    name="Marc Skov Madsen",
    url="https://datamodelsanalytics.com",
    github_url="https://github.com/marcskovmadsen",
    github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
)
AWESOME_PANEL_ORG = Author(
    name="Awesome-panel.org",
    url="https://awesome-panel.org",
    github_url="https://github.com/marcskovmadsen",
    github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
)
PHILIPP_RUDIGER = Author(
    name="Philipp Rudiger",
    url="http://philippjfr.com/",
    github_url="https://github.com/philippjfr",
    github_avatar_url="https://avatars0.githubusercontent.com/u/1550771",
)
AUTHORS = [
    AWESOME_PANEL_ORG,
    MARC_SKOV_MADSEN,
    PANEL_AUTHOR,
    PHILIPP_RUDIGER,
]
