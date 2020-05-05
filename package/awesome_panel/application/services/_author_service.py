"""This module contains a CRUD Service for Authors"""
from typing import List, Optional

import param

from awesome_panel.application.models import Author


class AuthorService(param.Parameterized):
    """A CRUD Service for Authors

    Notes:

    - The authors list is kept sorted.
    - DON'T change the authors list manually. Use the functions of the service

    """

    authors = param.List(constant=True)
    default_author = param.ClassSelector(class_=Author, constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        self._authors = {author.name: author for author in self.authors}
        if not self.default_author:
            self._set_default_author_to_application_author()

    def create(self, author: Author):
        """Creates the specified Author

        Args:
            author (Author): A Author to create
        """
        self._authors[author.name] = author
        self._update_authors_list()

    def read(self, name: str) -> Optional[Author]:
        """Returns the Author with the given name

        Args:
            name (str): The name of the Author to return

        Returns:
            Optional[Author]: The Author with the given name if it exists. Otherwise None
        """
        if name in self._authors:
            return self._authors[name]
        return None

    def update(self, author: Author):
        """Updates the given author

        Args:
            author (Author): A Author to update
        """
        self.create(author)

    def delete(self, author: Author):
        """Deletes the given author

        Args:
            author (Author): [description]
        """
        if author.name in self._authors:
            self._authors = {
                key: value for key, value in self._authors.items() if key != author.name
            }
            self._update_authors_list()

    def _update_authors_list(self):
        with param.edit_constant(self):
            self.authors = sorted(list(self._authors.values()))

    def bulk_create(self, authors: List[Author]):
        """Creates the list of authors

        Args:
            authors (List[Author]): A list of Authors to create
        """
        old_authors = self._authors
        new_authors = {author.name: author for author in authors}
        self._authors = {**old_authors, **new_authors}
        self._update_authors_list()

    def _set_default_author_to_application_author(self):
        author = Author(
            name="Marc Skov Madsen",
            url="https://datamodelsanalytics.com",
            github_url="https://github.com/marcskovmadsen",
            github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
        )
        self.set_default_author(author)

    def set_default_author(self, author: Author):
        """Change the default_author to the specified author

        Args:
            author (Author): The new default_author
        """

        if not author in self.authors:
            self.create(author)
        with param.edit_constant(self):
            self.default_author = author


author_service = AuthorService() # pylint: disable=invalid-name
