import param


class Progress(param.Parameterized):
    value = param.Integer(default=0, bounds=(0, 100))
    active_counts = param.Integer(default=0, bounds=(0, None))

    def is_active(self):
        return self.active_counts > 0

    def increment_active_counts(self):
        self.active_counts += 1

    def decrement_active_counts(self):
        self.active_counts = max(0, self.active_counts - 1)
