"""This module contains a CRUD Service for Tags"""
from typing import List, Optional

import param

from awesome_panel.application.models import Tag


class TagService(param.Parameterized):
    """A CRUD Service for Tags

    Notes:

    - The tags list is kept sorted.
    - DON'T change the tags list manually. Use the functions of the service

    """

    tags = param.List(constant=True)

    def __init__(self, **params):
        super().__init__(**params)

        self._tags = {tag.name: tag for tag in self.tags}

    def create(self, tag: Tag):
        """Creates the specified Tag

        Args:
            tag (Tag): A Tag to create
        """
        self._tags[tag.name] = tag
        self._update_tags_list()

    def read(self, name: str) -> Optional[Tag]:
        """Returns the Tag with the given name

        Args:
            name (str): The name of the Tag to return

        Returns:
            Optional[Tag]: The Tag with the given name if it exists. Otherwise None
        """
        if name in self._tags:
            return self._tags[name]
        return None

    def update(self, tag: Tag):
        """Updates the given tag

        Args:
            tag (Tag): A Tag to update
        """
        self.create(tag)

    def delete(self, tag: Tag):
        """Deletes the given tag

        Args:
            tag (Tag): [description]
        """
        if tag.name in self._tags:
            self._tags = {key: value for key, value in self._tags.items() if key != tag.name}
            self._update_tags_list()

    def _update_tags_list(self):
        with param.edit_constant(self):
            self.tags = sorted(list(self._tags.values()))

    def bulk_create(self, tags: List[Tag]):
        """Creates the list of tags

        Args:
            tags (List[Tag]): A list of Tags to create
        """
        old_tags = self._tags
        new_tags = {tag.name: tag for tag in tags}
        self._tags = {**old_tags, **new_tags}
        self._update_tags_list()

