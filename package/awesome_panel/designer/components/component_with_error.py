# pylint: disable=redefined-outer-name,protected-access
# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring
# pylint: disable=too-few-public-methods
class ComponentWithError:
    def __init__(self):
        raise NotImplementedError()
