"""This module defines the Progress Model"""
import param


class Progress(param.Parameterized):
    """The Progress model is used to communicate the Progress of the Application,
    the active PageComponent etc."""
    value = param.Integer(default=0, bounds=(0, None))
    value_max = param.Integer(default=100, bounds=(0, None))
    message = param.String()
    active_count = param.Integer(bounds=(0, None))

    @property
    def active(self) -> bool:
        """Returns True if there is activity like ETL or Plotting.

        Returns:
            bool: True if there is activity. Otherwise False is returned.
        """
        return self.value > 0 or self.message != "" or self.active_count > 0
