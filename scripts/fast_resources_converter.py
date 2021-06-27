"""Temporary Script for converting to fast resources"""
from application.config.authors import AUTHORS
from application.config.pages import PAGES
from application.config.resources import RESOURCES


def to_author_name(author):
    return (
        author.name.replace(". ", "_").replace(" ", "_").replace("-", "_").replace(".", "_").upper()
    )


def convert_authors():
    for author in AUTHORS:
        author_name = to_author_name(author)
        text = f"""\
{author_name} = Author(
    name = "{author.name}",
    url = "{author.url}",
    avatar = "{author.github_avatar}",
    github_url = "{author.github_url}",
)"""
        print(text)
        # print(author_name + ',')


def convert_resources():
    for resource in RESOURCES:
        author_name = to_author_name(resource.author)
        text = f"""\
Resource(
    name="{resource.name}",
    url="{resource.url}",
    description="",
    tags=['{"', '".join([tag.name for tag in resource.tags])}'],
    author=authors.{author_name},
),"""
        print(text)
        # print(author_name + ',')


def convert_apps():
    for resource in PAGES:
        author_name = to_author_name(resource.author)
        text = f"""\
Application(
    name="{resource.name}",
    description="",
    url="{resource.url}",
    tags=['{"', '".join([tag.name for tag in resource.tags])}'],
    author=authors.{author_name},
    code_url="",
    thumbnail_url="",
),"""
        print(text)


convert_resources()
convert_authors()
