"""This example demonstrates the use of the
[panel-highcharts](https://github.com/marcskovmadsen/panel-highcharts) python package.

The `panel-highcharts` [python package](https://pypi.org/project/panel-highcharts/) and
[repository](https://github.com/marcskovmadsen/panel-highcharts) is open source and free to use
(MIT License), however Highcharts itself requires a license for commercial use.
For more info see the Highcharts license [FAQs](https://shop.highsoft.com/faq).

For a gallery of HighCharts check out the [HighCharts Demo](https://www.highcharts.com/demo).
"""
# pylint: disable=line-too-long
import panel as pn
import panel_highcharts as ph

from awesome_panel import config

MESSAGE = "**Hover a node** to learn about the character"
CONFIG = {
    "chart": {
        "type": "networkgraph",
        "plotBorderWidth": 1,
    },
    "title": {"text": "Panel HighChart - Network Graph Example"},
    "plotOptions": {"networkgraph": {"keys": ["from", "to"]}},
    "series": [
        {
            "layoutAlgorithm": {
                "enableSimulation": True,
                "linkLength": 100,
                "initialPositions": """function () {
                var chart = this.series[0].chart,
                    width = chart.plotWidth,
                    height = chart.plotHeight;

                this.nodes.forEach(function (node) {
                    // If initial positions were set previously, use that
                    // positions. Otherwise use random position:
                    node.plotX = node.plotX === undefined ?
                        Math.random() * width : node.plotX;
                    node.plotY = node.plotY === undefined ?
                        Math.random() * height : node.plotY;
                });
            }""",
            },
            "name": "K8",
            "data": [
                ["A", "B"],
                ["A", "C"],
                ["A", "D"],
                ["A", "E"],
                ["A", "F"],
                ["A", "G"],
                ["B", "C"],
                ["B", "D"],
                ["B", "E"],
                ["B", "F"],
                ["B", "G"],
                ["C", "D"],
                ["C", "E"],
                ["C", "F"],
                ["C", "G"],
                ["D", "E"],
                ["D", "F"],
                ["D", "G"],
                ["E", "F"],
                ["E", "G"],
                ["F", "G"],
            ],
            "point": {
                "events": {
                    "mouseOver": "@",
                }
            },
            "events": {
                "mouseOut": "@",
            },
        }
    ],
}

WIKI = {
    "A": "**A**, or a, is the first letter and the first vowel letter of the modern English alphabet and the ISO basic Latin alphabet. Its name in English is a (pronounced /ˈeɪ/), plural aes. It is similar in shape to the Ancient Greek letter alpha, from which it derives. The uppercase version consists of the two slanting sides of a triangle, crossed in the middle by a horizontal bar. The lowercase version can be written in two forms: the double-storey a and single-storey ɑ. The latter is commonly used in handwriting and fonts based on it, especially fonts intended to be read by children, and is also found in italic type.",
    "B": "**B**, or b, is the second letter of the Latin-script alphabet. Its name in English is bee (pronounced /ˈbiː/), plural bees. It represents the voiced bilabial stop in many languages, including English. In some other languages, it is used to represent other bilabial consonants.",
    "C": "**C**, or c, is the third letter in the English and ISO basic Latin alphabets. Its name in English is cee (pronounced /ˈsiː/), plural cees.",
    "D": "**D**, or d, is the fourth letter of the modern English alphabet and the ISO basic Latin alphabet. Its name in English is dee (pronounced /ˈdiː/), plural dees.",
    "E": "**E**, or e, is the fifth letter and the second vowel letter in the modern English alphabet and the ISO basic Latin alphabet. Its name in English is e (pronounced /ˈiː/), plural ees. It is the most commonly used letter in many languages, including Czech, Danish, Dutch, English, French, German, Hungarian, Latin, Latvian, Norwegian, Spanish, and Swedish",
    "F": "**F**, or f, is the sixth letter in the modern English alphabet and the ISO basic Latin alphabet. Its name in English is ef (pronounced /ˈɛf/), plural efs.",
    "G": "**G**, or g, is the seventh letter of the ISO basic Latin alphabet. Its name in English is gee (pronounced /ˈdʒiː/), plural gees.",
}


def app():
    """Returns the application"""
    chart = ph.HighChart(object=CONFIG, sizing_mode="stretch_both", min_height=400)
    info = pn.pane.Markdown(MESSAGE, min_height=100)

    @pn.depends(event=chart.param.event, watch=True)
    def update_info(event):
        if event["type"] == "mouseOver":
            info.object = WIKI.get(event["target"]["name"])
        else:
            info.object = MESSAGE

    return pn.Column(chart, info, sizing_mode="stretch_both")


if __name__.startswith("bokeh"):
    ph.config.js_files(highcharts_networkgraph=True)

    config.extension("highchart", url="highcharts_network")
    app().servable()
