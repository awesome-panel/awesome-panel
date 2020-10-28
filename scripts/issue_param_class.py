import param
import pytest

param.String


class DictWithStringKeyAndListOfStringsValues(param.Parameter):
    def __init__(self, default={}, allow_None=False, **kwargs):
        super().__init__(default=default, allow_None=allow_None, **kwargs)

        # I can see that the `Parameter` __init__ does not `_validate` the default
        # This must be a bug
        self._validate(self.default)

    def _validate(self, val):
        if self.allow_None and val is None:
            return

        if not isinstance(val, dict):
            raise ValueError(f"Error. The value {val} is not of type Dict[str, List]!")

        for key in val.keys():
            if not isinstance(key, str):
                raise ValueError(f"Error. The key {key} is not of type str!")
        for value in val.values():
            if not isinstance(value, list):
                raise ValueError(f"Error. The dictionary value {value} is not of type list!")
            for list_val in value:
                if not isinstance(list_val, str):
                    raise ValueError(f"Error. The list value {list_val} is not of type str!")


class UnivariateConfig(param.Parameterized):
    model_types = DictWithStringKeyAndListOfStringsValues(default={})


@pytest.mark.parametrize(
    ["value"],
    [
        ({},),
        ({"a": []},),
        ({"a": ["b"]},),
    ],
)
def test_does_not_raise_error_when_correct_type(value):
    config = UnivariateConfig(model_types=value)
    assert config.model_types == value


@pytest.mark.parametrize(
    ["value"],
    [
        (None,),
        ("str",),
        ({"a": [None]},),
    ],
)
def test_raises_value_error_if_not_correct_type(value):
    with pytest.raises(ValueError):
        UnivariateConfig(model_types=value)
