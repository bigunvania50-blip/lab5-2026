from .team_member import TeamMember


class Coach(TeamMember):
    def __init__(self, name, age, salary, experience):
        super().__init__(name, age, salary)
        self._experience = experience

    @property
    def experience(self):
        return self._experience

    def get_role(self):
        return "Тренер"

    def work(self):
        return f"{self.name} розбирає ігри та складає тактику"

    def __str__(self):
        return f"{super().__str__()}, досвід {self.experience} р."

    def __repr__(self):
        return f"Coach('{self.name}', {self.age}, {self.salary}, {self.experience})"