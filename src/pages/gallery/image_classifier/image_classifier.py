"""This is an **image classifier app** that enables a user to

- select a classifier model
- upload an image

and get a predicted classification in return.

This app is inspired by the awesome [imageNet](https://github.com/iamatulsingh/imageNet-streamlit)
application developed by [Atul Kumar Singh](https://github.com/iamatulsingh)."""
import io
import os
from base64 import b64encode
from functools import lru_cache
from typing import Callable, List, NamedTuple, Tuple

import altair as alt
import keras.backend.tensorflow_backend as tb
import numpy as np
import pandas as pd
import panel as pn
import param
from keras.applications import (
    densenet,
    imagenet_utils,
    inception_v3,
    mobilenet_v2,
    nasnet,
    resnet,
    vgg19,
    xception,
)
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image

import awesome_panel.express as pnx

pn.extension("vega")
# Hack
# I get a '_thread._local' object has no attribute 'value' error without this
# See https://github.com/keras-team/keras/issues/13353#issuecomment-545459472
tb._SYMBOLIC_SCOPE.value = True  # pylint: disable=protected-access


class KerasApplication(NamedTuple):
    """We wrap a Keras Application into this class for ease of use"""

    name: str
    keras_application: Callable
    input_shape: Tuple[int, int] = (224, 224)
    preprocess_input_func: Callable = imagenet_utils.preprocess_input
    decode_predictions_func: Callable = imagenet_utils.decode_predictions
    url: str = "https://keras.io/applications/"

    def load_image(self, image_path: str) -> Image:
        """Loads the image from file

        Arguments:
            image_path {str} -- The absolute path to the image

        Returns:
            Image -- The image loaded
        """
        return load_img(image_path, target_size=self.input_shape)

    def to_input_shape(self, image: Image) -> Image:
        """Resizes the image to the input_shape

        Arguments:
            image {Image} -- The image to reshape

        Returns:
            Image -- The reshaped image
        """
        return image.resize(self.input_shape)

    @lru_cache(2)
    def get_model(self) -> object:
        """The Keras model with weights="imagenet"

        Returns:
            [object] -- An instance of the keras_application with weights="imagenet"
        """
        return self.keras_application(weights="imagenet")

    def preprocess_input(self, image: Image) -> Image:
        """Prepares the image for classification by the classifier

        Arguments:
            image {Image} -- The image to preprocess

        Returns:
            Image -- The preprocessed image
        """
        # For an explanation see
        # https://stackoverflow.com/questions/47555829/preprocess-input-method-in-keras
        image = self.to_input_shape(image)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = self.preprocess_input_func(image)
        return image

    def get_top_predictions(
        self, image: Image = None, report_progress_func=print
    ) -> List[Tuple[str, str, float]]:
        """[summary]

        Keyword Arguments:
            image {Image} -- An image (default: {None})
            report_progress_func {Callable} -- A function like 'print', 'st.write' or similar
            (default: {print})

        Returns:
            [type] -- The top predictions as a list of 3-tuples on the form
            (id, prediction, probability)
        """
        report_progress_func(
            f"Loading {self.name} model ... (The first time this is done it may take several "
            "minutes)",
            10,
        )
        model = self.get_model()

        report_progress_func(f"Processing image ... ", 67)
        image = self.preprocess_input(image)

        report_progress_func(f"Classifying image with '{self.name}'... ", 85)
        predictions = model.predict(image)  # type: ignore
        top_predictions = self.decode_predictions_func(predictions)

        report_progress_func("", 0)

        return top_predictions[0]

    @staticmethod
    def to_main_prediction_string(predictions) -> str:
        """A pretty string of the main prediction to output to the user"""
        _, prediction, _ = predictions[0]
        prediction_text = prediction.replace("_", " ").capitalize()
        prediction_query = prediction.replace("_", "+")
        prediction_url = f"http://www.image-net.org/search?q={prediction_query}"
        return f"It's a **[{prediction_text}]({prediction_url})**"

    @staticmethod
    def to_predictions_chart(predictions) -> alt.Chart:
        """A pretty chart of the (prediction, probability) to output to the user"""
        dataframe = pd.DataFrame(predictions, columns=["id", "prediction", "probability"])
        dataframe["probability"] = dataframe["probability"].round(2) * 100
        chart = (
            alt.Chart(dataframe)
            .mark_bar()
            .encode(
                x=alt.X("probability:Q", scale=alt.Scale(domain=(0, 100))),
                y=alt.Y(
                    "prediction:N",
                    sort=alt.EncodingSortField(field="probability", order="descending"),
                ),
            )
        )
        return chart


# pylint: enable=line-too-long

# See https://keras.io/applications/
DEFAULT_KERAS_APPLICATION_INDEX = 2
KERAS_APPLICATIONS: List[KerasApplication] = [
    KerasApplication(
        "DenseNet121",
        keras_application=densenet.DenseNet121,
        url="https://keras.io/applications/#densenet",
        preprocess_input_func=densenet.preprocess_input,
        decode_predictions_func=densenet.decode_predictions,
    ),
    KerasApplication(
        "InceptionV3",
        keras_application=inception_v3.InceptionV3,
        input_shape=(299, 299),
        url="https://keras.io/applications/#inceptionv3",
        preprocess_input_func=inception_v3.preprocess_input,
        decode_predictions_func=inception_v3.decode_predictions,
    ),
    KerasApplication(
        "MobileNetV2",
        keras_application=mobilenet_v2.MobileNetV2,
        url="https://keras.io/applications/#mobilenet",
        preprocess_input_func=mobilenet_v2.preprocess_input,
        decode_predictions_func=mobilenet_v2.decode_predictions,
    ),
    KerasApplication(
        "NASNetMobile",
        keras_application=nasnet.NASNetMobile,
        url="https://keras.io/applications/#nasnet",
        preprocess_input_func=nasnet.preprocess_input,
        decode_predictions_func=nasnet.decode_predictions,
    ),
    KerasApplication(
        "NASNetLarge",
        keras_application=nasnet.NASNetLarge,
        input_shape=(331, 331),
        url="https://keras.io/applications/#nasnet",
        preprocess_input_func=nasnet.preprocess_input,
        decode_predictions_func=nasnet.decode_predictions,
    ),
    KerasApplication(
        "ResNet50",
        keras_application=resnet.ResNet50,
        url="https://keras.io/applications/#resnet",
        preprocess_input_func=resnet.preprocess_input,
        decode_predictions_func=resnet.decode_predictions,
    ),
    KerasApplication(
        "VGG19",
        keras_application=vgg19.VGG19,
        url="https://keras.io/applications/#vgg19",
        preprocess_input_func=vgg19.preprocess_input,
        decode_predictions_func=vgg19.decode_predictions,
    ),
    KerasApplication(
        "Xception",
        keras_application=xception.Xception,
        input_shape=(299, 299),
        url="https://keras.io/applications/#inceptionv3",
        preprocess_input_func=xception.preprocess_input,
        decode_predictions_func=xception.decode_predictions,
    ),
]

IMAGE_TYPES = [".jpg"]

# pylint: disable=line-too-long
def get_resources_markdown(model: KerasApplication) -> str:
    """Some info regarding Resources

    Arguments:
        model {KerasApplication} -- The KerasApplication employed

    Returns:
        str -- A Markdown string with links to relevant resources
    """

    return f"""### Resources

- [Keras](https://keras.io/)
    - [Keras Apps](https://keras.io/applications)
        - [{model.name} Docs]({model.url})
- Images
    - [ImageNet](http://www.image-net.org/)
    - [Awesome Images](https://github.com/heyalexej/awesome-images)
    - [Awesome-Streamlit Images](https://github.com/MarcSkovMadsen/awesome-streamlit/tree/master/gallery/image_classifier/images)"""


# pylint: enable=line-too-long


def set_environ():
    """Sets environment variables for logging etc."""
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


class ImageClassifierApp(param.Parameterized):
    """The Image Classifier App

    We define the parameters, views and depencies of the app
    """

    model = param.ObjectSelector(
        default=KERAS_APPLICATIONS[DEFAULT_KERAS_APPLICATION_INDEX], objects=KERAS_APPLICATIONS,
    )
    image_file = param.FileSelector()
    top_predictions = param.ClassSelector(class_=list)
    progress_value = param.Integer()
    progress_message = param.String()

    @param.depends("model")
    def resources_view(self):
        """A view of a section with links to resources"""
        if self.model:
            return pn.pane.Markdown(get_resources_markdown(self.model))
        return pn.pane.HTML()

    # @param.depends("image_file", watch=True)
    # def set_image(self):
    #     self.image = Image.open(io.BytesIO(self.image_file))

    @param.depends("image_file")
    def image_view(self):
        """A view of the image_file"""
        if self.image_file:
            bytes_io = io.BytesIO(self.image_file)
            return pn.pane.HTML(
                '<img src="data:image/jpg;base64,{0}" style="height:400px;min-width:600px;"/>'.format(
                    b64encode(bytes_io.getvalue()).decode("utf-8")
                )
            )
        return pnx.InfoAlert("Upload an image in .jpg format", height=400, min_width=600)

    def report_progress(self, message: str = "", value: int = 0):
        """Update the progress message and value

        Args:
            message (str, optional): A message to convery to the user. Defaults to "".
            value (int, optional): A progress value between 0 and 100. Defaults to 0.
        """
        self.progress_message = message
        self.progress_value = value

    @param.depends("image_file", "model", watch=True)
    def set_top_predictions(self):
        """Updates the top_predictions"""
        self.top_predictions = None

        if self.image_file and self.model:
            self.report_progress("Prediction Started", 1)
            bytes_io = io.BytesIO(self.image_file)
            pil_image = Image.open(bytes_io)
            # pylint: disable=no-member
            self.top_predictions = self.model.get_top_predictions(
                image=pil_image, report_progress_func=self.report_progress,
            )
            # pylint: enable=no-member

    @param.depends("top_predictions")
    def main_prediction_view(self):
        """A pretty string of the main prediction to output to the user"""
        if self.model and self.top_predictions:
            # pylint: disable=no-member
            main_prediction_string = self.model.to_main_prediction_string(self.top_predictions)
            # pylint: enable=no-member
            return pn.pane.Markdown(main_prediction_string)

        return pn.pane.Str("Not Available")

    @param.depends("top_predictions")
    def predictions_chart_view(self):
        """A view of a chart showing the top predictions and their probabilities"""
        if self.model and self.top_predictions:
            # pylint: disable=no-member
            chart = self.model.to_predictions_chart(self.top_predictions)
            # pylint: enable=no-member
            chart = chart.properties(height=200, width=400,)
            return pn.pane.Vega(chart)

        return pn.pane.Str("Not Available")

    @param.depends("progress_value", "top_predictions")
    def predictions_view(self):
        """A view showing the predictions or the progress of the predictions"""
        if self.progress_value:
            return pn.Column(
                pnx.SubHeader("Prediction"),
                pn.widgets.Progress(value=self.progress_value, width=200),
                pn.pane.Str(self.progress_message),
                sizing_mode="stretch_width",
            )
        if self.top_predictions:
            return pn.Column(
                pnx.SubHeader("Prediction"),
                self.main_prediction_view,
                pnx.SubHeader("Alternative Predictions"),
                self.predictions_chart_view,
                sizing_mode="stretch_width",
            )
        return pn.pane.HTML()


def view():
    """Run this to run the application"""
    set_environ()

    image_classifier_app = ImageClassifierApp()

    app = pn.Column(
        pnx.Header("Image Classification with Keras and Tensorflow.", height=40),
        pnx.Markdown(__doc__),
        image_classifier_app.resources_view,
        pnx.SubHeader("Classifier"),
        pn.Param(
            image_classifier_app.param["model"],
            widgets={"model": {"type": pn.widgets.RadioButtonGroup, "button_type": "primary"}},
        ),
        pnx.SubHeader("Image"),
        pn.Param(
            image_classifier_app.param["image_file"],
            widgets={"image_file": {"type": pn.widgets.FileInput, "accept": ".jpg"}},
        ),
        image_classifier_app.image_view,
        image_classifier_app.predictions_view,
        sizing_mode="stretch_width",
    )
    return app


if __name__.startswith("bk"):
    view().servable()

