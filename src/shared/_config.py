"""Provides

- config: An instance of SiteConfig holding the current Site configuration
"""

import pathlib
from typing import Union

import toml

from src.shared.models import Application, Person, SiteConfig


def _create_site_config(config_root: Union[str, pathlib.Path]) -> SiteConfig:
    if isinstance(config_root, str):
        config_root = pathlib.Path(config_root)
    persons_toml = config_root / "persons.toml"
    persons = Person.create_from_toml(persons_toml)

    applications = config_root / "applications.toml"
    applications = Application.create_from_toml(applications, persons=persons)

    site_toml = config_root / "site.toml"
    site = toml.load(site_toml)

    return SiteConfig(**site, persons=persons, applications=applications)
