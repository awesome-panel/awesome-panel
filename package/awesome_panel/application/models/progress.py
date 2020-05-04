import param


class Progress(param.Parameterized):
    value = param.Integer(default=0, bounds=(0, None))
    value_max = param.Integer(default=100, bounds=(0, None))
    message = param.String()
    active_count = param.Integer(bounds=(0, None))

    @property
    def active(self):
        return self.value > 0 or self.message!="" or self.active_count > 0
