from awesome_panel.models import Author

def get_default_author():
    return Author(
        name="Marc Skov Madsen",
        url="https://datamodelsanalytics.com",
        github_url="https://github.com/marcskovmadsen",
        github_avatar_url="https://avatars0.githubusercontent.com/u/42288570",
    )