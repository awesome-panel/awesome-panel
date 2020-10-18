from application.config.authors import AUTHORS
from application.config.resources import RESOURCES

def to_author_name(author):
    return author.name.replace(". ", "_").replace(" ", "_").replace("-", "_").replace(".", "_").upper()

def convert_authors():
    for author in AUTHORS:
        author_name=to_author_name(author)
        text = f"""\
{author_name} = Author(
    name = "{author.name}",
    url = "{author.url}",
    avatar_url = "{author.github_avatar_url}",
    github_url = "{author.github_url}",
)"""
        print(text)
        # print(author_name + ',')

def convert_resources():
    for resource in RESOURCES:
        author_name=to_author_name(resource.author)
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

convert_authors()
# convert_resources()