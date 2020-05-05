"""In this module we implement the ThemeService"""
import param


class ThemeService(param.Parameterized):
    """ThemeService"""
    def reset(self):
        """Resets the ThemeService

        Args:
            param ([type]): [description]
        """


theme_service = ThemeService() # pylint: disable=invalid-name
