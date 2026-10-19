from abc import ABC, abstractmethod


class TeamMember(ABC):
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self.salary = salary

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не може бути від'ємною")
        self._salary = value

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def work(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name}, {self.age} р., зарплата {self.salary}$"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.age}, {self.salary})"