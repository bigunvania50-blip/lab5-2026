from .team_member import TeamMember


class TeamManager:
    def __init__(self, team_name):
        self._team_name = team_name
        self._members = []

    @property
    def team_name(self):
        return self._team_name

    @property
    def members(self):
        return list(self._members)

    def add_member(self, member):
        if not isinstance(member, TeamMember):
            raise TypeError("Можна додавати лише об'єкти TeamMember")
        self._members.append(member)

    def remove_member(self, member):
        if member not in self._members:
            raise ValueError("Такого учасника немає в команді")
        self._members.remove(member)

    def find_by_name(self, text):
        return [m for m in self._members if text.lower() in m.name.lower()]

    def filter_by_role(self, role_class):
        return [m for m in self._members if isinstance(m, role_class)]

    def filter_by_min_salary(self, min_salary):
        return [m for m in self._members if m.salary >= min_salary]

    def sort_by_salary(self, reverse=False):
        return sorted(self._members, key=lambda m: m.salary, reverse=reverse)

    def sort_by_age(self, reverse=False):
        return sorted(self._members, key=lambda m: m.age, reverse=reverse)

    def total_salary(self):
        return sum(m.salary for m in self._members)

    def __len__(self):
        return len(self._members)

    def __str__(self):
        return f"Команда '{self.team_name}': {len(self)} учасників, зарплати разом {self.total_salary()}$"

    def __repr__(self):
        return f"TeamManager('{self.team_name}')"