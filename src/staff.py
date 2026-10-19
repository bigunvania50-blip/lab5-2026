from .team_member import TeamMember


class Staff(TeamMember):
    def __init__(self, name, age, salary, position):
        super().__init__(name, age, salary)
        self._position = position

    @property
    def position(self):
        return self._position

    def get_role(self):
        return "Персонал"

    def work(self):
        return f"{self.name} працює на посаді: {self.position}"

    def __str__(self):
        return f"{super().__str__()}, посада {self.position}"

    def __repr__(self):
        return f"Staff('{self.name}', {self.age}, {self.salary}, '{self.position}')"