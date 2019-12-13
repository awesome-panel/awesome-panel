"""This module contains the list of Authors"""
from awesome_panel.shared.models import Author

# Authors
PANEL_AUTHOR = Author(name="panel", url="https://panel.pyviz.org/")
MARC_SKOV_MADSEN = Author(name="Marc Skov Madsen", url="https://datamodelsanalytics.com")
AWESOME_PANEL_ORG = Author(name="awesome-panel.org", url="https://awesome-panel.org",)
AUTHORS = [
    MARC_SKOV_MADSEN,
    PANEL_AUTHOR,
    AWESOME_PANEL_ORG,
]
