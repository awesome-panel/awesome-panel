"""In this module we define views of the Athlete Model"""

from typing import Optional

import panel as pn

from ..models.athlete import Athlete

pn.extension()


class AthleteUpdateView(pn.Column):
    """A View for editing/ updating the Athlete"""

    def __init__(self, athlete: Optional[Athlete] = None, **kwargs):
        if athlete:
            self.athlete = athlete
        else:
            self.athlete = Athlete()

        super().__init__(
            pn.Param(self.athlete.param, widgets={"birthday": pn.widgets.DatePicker}),
            pn.widgets.DatePicker(),
            **kwargs,
        )
