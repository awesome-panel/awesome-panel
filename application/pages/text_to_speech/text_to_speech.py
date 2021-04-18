"""The [`TextToSpeech`](https://panel.holoviz.org/reference/widgets/TextToSpeech.html#\
widgets-gallery-texttospeech) Widget provides brings text to speech to Panel. It wraps the wraps
the *HTML5 SpeechSynthesis API*.

The `TextToSpeech` widget was developed and contributed to Panel by `awesome-panel.org`.

Please note that the available voices and languages depend on your browser and os. For the best
experience **use Chrome**.
"""
import panel as pn
from panel.widgets import TextToSpeech

from application.config import site

APPLICATION = site.create_application(
    url="text-to-speech",
    name="Text To Speech",
    author="Marc Skov Madsen",
    introduction="Demonstrates the powerful TextToSpeech widget",
    description=__doc__,
    thumbnail_url="text-to-speech.png",
    documentation_url="",
    code_url="text_to_speech/text_to_speech.py",
    gif_url="text-to-speech.gif",
    mp4_url="text-to-speech.mp4",
    tags=[
        "TextToSpeech",
    ],
)

TEXT = """By Aesop

There was a time, so the story goes, when all the animals lived together in harmony. The lion
didn’t chase the oxen, the wolf didn’t hunt the sheep, and owls didn’t swoop on the mice in the
field.

Once a year they would get together and choose a king, who would then reign over the animal
kingdom for the next twelve months. Those animals who thought they would like a turn at being king
would put themselves forward and would make speeches and give demonstrations of their prowess or
their wisdom. Then all the animals gathered together would vote, and the animal with the most
votes was crowned king. That’s probably where us humans got the idea of elections!

Now, monkey knew very well that he was neither very strong nor very wise, and he was not exactly
a great orator, but, boy, could he dance! So he did what he does best, and he danced acrobatically
and energetically, performing enormous leaps, back somersaults and cartwheels that truly dazzled
his audience. Compared to monkey, the elephant was grave and cumbersome, the lion was powerful and
authoritarian, and the snake was sly and sinister.

Nobody who was there remembers exactly how it happened, but somehow monkey scraped through with a
clear majority of all the votes cast, and he was announced the king of the animal kingdom for the
coming year. Most of the animals seemed quite content with this outcome, because they knew that
monkey would not take his duties too seriously and make all kinds of onerous demands on them, or
demand too much of a formal show of obedience. But there were some who thought that the election
of monkey diminished the stature of the kingship, and one of these was fox; in fact fox was pretty
disgusted, and he didn’t mind who knew it. So he set about concocting a scheme to make monkey look
stupid.

He gathered together some fine fresh fruit from the forest, mangos, figs and dates, and laid them
out on a trap he’d found. He waited for the monkey to pass by, and called out to him: “Sire, look
at these delicious dainty morsels I discovered here by the wayside. I was tempted to gorge myself
on them, but then I remembered fruits are your favourite repast, and I thought I should keep them
for you, our beloved king!”

Monkey could not resist either the flattery or the fruit, and just managed to compose himself long
enough to whisper a hurried “Why, thank you, Mr Fox” and made a beeline for the fruit. “Swish” and
“Clunk” went the trap, and “AAAYYY AAAYYY” went our unfortunate monkey king, the trap firmly
clasped around his paw.

Monkey bitterly reproached fox for leading him into such a dangerous situation, but fox just
laughed and laughed. “You call yourself king of all the animals,” he cried, “and you allow
yourself to be taken in just like that!”

Aesop
"""


@site.add(APPLICATION)
def view():
    """Return the TextToSpeech App.

    Returns:
        FastListTemplate: A template with the app
    """
    pn.config.sizing_mode = "stretch_width"
    template = pn.template.FastListTemplate(title="Text to Speech", main_max_width="768px")
    text_to_speech = TextToSpeech(name="Speaker", value=TEXT, auto_speak=False)
    speaker_settings = pn.Param(
        text_to_speech,
        parameters=[
            "value",
            "speak",
            "paused",
            "speaking",
            "pending",
            "pause",
            "resume",
            "cancel",
            "lang",
            "voice",
            "pitch",
            "rate",
            "volume",
            "speak",
            "value",
        ],
        widgets={
            "speak": {"button_type": "primary"},
            "value": {"widget_type": pn.widgets.TextAreaInput, "height": 300},
        },
        expand_button=False,
        show_name=False,
    )

    component = pn.Row(
        pn.layout.HSpacer(),
        pn.Column(
            text_to_speech,
            speaker_settings,
            width=500,
            sizing_mode="fixed",
        ),
        pn.layout.HSpacer(),
        sizing_mode="stretch_both",
    )
    template.main[:] = [
        APPLICATION.intro_section(),
        component,
    ]
    return template


if __name__.startswith("bokeh"):
    pn.config.sizing_mode = "stretch_width"
    view().servable()
