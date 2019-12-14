"""Export of paths and urls of images"""
import pathlib

ROOT_PATH = pathlib.Path(__file__).parent
ABOUT_IMAGE_ERROR_PATH = ROOT_PATH / "about_image_error.png"
ABOUT_IMAGE_NO_ERROR_PATH = ROOT_PATH / "about_image_no_error.png"
INFO_ALERT_SCROLLBAR_PROBLEM = ROOT_PATH / "info_alert_scrollbar_problem.png"

ROOT_URL = (
    "https://github.com/MarcSkovMadsen/awesome-panel/blob/master/"
    "gallery/bootstrap_dashboard/assets/images/"
)
ABOUT_IMAGE_ERROR_URL = ROOT_URL + "about_image_error.png?raw=true"
ABOUT_IMAGE_NO_ERROR_URL = ROOT_URL + "about_image_no_error.png?raw=true"
INFO_ALERT_SCROLLBAR_PROBLEM_URL = ROOT_URL + "info_alert_scrollbar_problem.png?raw=true"
