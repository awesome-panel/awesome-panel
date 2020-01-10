"""In this module we define a view to report progress

Use the `report` and `increment` methods of `progress` to report your progress

and then include `progress.view` in your app.
"""
from awesome_panel.express import ProgressExt

progress = ProgressExt()  # pylint: disable=invalid-name
