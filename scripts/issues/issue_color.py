import panel as pn
from typing import NamedTuple, List
import param


class KerasApplication(NamedTuple):
    name: str


KERAS_APPLICATIONS: List[KerasApplication] = [
    KerasApplication("DenseNet121",),
    KerasApplication("InceptionV3",),
    KerasApplication("MobileNetV2",),
    KerasApplication("NASNetMobile",),
    KerasApplication("NASNetLarge",),
    KerasApplication("ResNet50",),
    KerasApplication("VGG19",),
    KerasApplication("Xception",),
]


class ImageClassifierApp(param.Parameterized):
    model = param.ObjectSelector(objects=KERAS_APPLICATIONS,)


def view():
    image_classifier_app = ImageClassifierApp()
    app = pn.Column(
        pn.Param(
            image_classifier_app.param["model"],
            widgets={"model": {"type": pn.widgets.RadioButtonGroup, "button_type": "primary"}},
        ),
    )
    return app


if __name__.startswith("bk"):
    view().servable()

