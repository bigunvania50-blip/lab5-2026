from .team_member import TeamMember


class Player(TeamMember):
    def __init__(self, name, age, salary, nickname, rating):
        super().__init__(name, age, salary)
        self._nickname = nickname
        self.rating = rating

    @property
    def nickname(self):
        return self._nickname

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0 or value > 100:
            raise ValueError("Рейтинг має бути від 0 до 100")
        self._rating = value

    def get_role(self):
        return "Гравець"

    def work(self):
        return f"{self.nickname} тренується та грає матчі"

    def __str__(self):
        return f"{super().__str__()}, нік {self.nickname}, рейтинг {self.rating}"

    def __repr__(self):
        return f"Player('{self.name}', {self.age}, {self.salary}, '{self.nickname}', {self.rating})"