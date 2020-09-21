from os import name
from application.config.pages import GALLERY_PAGES

for page in GALLERY_PAGES:
    tags = ""
    for tag in page.tags:
        tags += f"'{tag.name}',"


    text = f"""\
ApplicationMetaData(
    name="{page.name}",
    description="{page.description}",
    url="https://awesome-panel.org",
    thumbnail_url="{page.thumbnail_png_url}",
    source_url="{page.source_code_url}",
    author_name="{page.author.name}",
    author_url="{page.author.url}",
    author_avatar_url="{page.author.github_avatar_url}",
    tags=[{tags}],
),"""
    print(text)