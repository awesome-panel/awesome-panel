"""In this module we define Views of the Athlete Model"""

from typing import Optional

import panel as pn

from ..models.athlete import Athlete


class AthleteUpdateView(pn.Column):
    """A View for editing/ updating the Athlete"""

    def __init__(self, athlete: Optional[Athlete] = None, **kwargs):
        if athlete:
            self.athlete = athlete
        else:
            self.athlete = Athlete()

        super().__init__(
            self.athlete.param["name_"],
            pn.Param(
                self.athlete.param["birthday"],
                widgets={"birthday": pn.widgets.DatePicker},
            ),
            self.athlete.param["weight"],
            **kwargs,
        )
