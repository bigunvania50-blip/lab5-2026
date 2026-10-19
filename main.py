from src.team_manager import TeamManager
from src.player import Player
from src.coach import Coach
from src.staff import Staff


def main():
    team = TeamManager("Cyber Eagles")

    team.add_member(Player("Олег Коваль", 21, 3000, "Falcon", 90))
    team.add_member(Player("Іван Мельник", 19, 2500, "Storm", 82))
    team.add_member(Player("Андрій Шевчук", 23, 3500, "Ghost", 95))
    team.add_member(Coach("Максим Бондар", 35, 4000, 10))
    team.add_member(Staff("Марія Ткач", 28, 2000, "Аналітик"))

    print(team)
    print()

    print("Усі учасники команди:")
    for member in team.members:
        print(member)
    print()

    print("Що робить кожен (поліморфізм):")
    for member in team.members:
        print(member.work())
    print()

    print("Пошук за іменем 'Іван':")
    for member in team.find_by_name("Іван"):
        print(member)
    print()

    print("Тільки гравці:")
    for member in team.filter_by_role(Player):
        print(member)
    print()

    print("Зарплата від 3000$:")
    for member in team.filter_by_min_salary(3000):
        print(member)
    print()

    print("Сортування за зарплатою (від більшої до меншої):")
    for member in team.sort_by_salary(reverse=True):
        print(member)
    print()

    print("Сортування за віком:")
    for member in team.sort_by_age():
        print(member)
    print()

    print("Приклад repr:")
    print(repr(team.members[0]))
    print()

    print("Видаляємо Марію Ткач")
    team.remove_member(team.find_by_name("Марія")[0])
    print(team)
    print()

    print("Спроба додати неправильний об'єкт:")
    try:
        team.add_member("Не учасник")
    except TypeError as error:
        print(f"Помилка: {error}")

    print("Спроба створити гравця з рейтингом 150:")
    try:
        Player("Тест", 20, 1000, "Test", 150)
    except ValueError as error:
        print(f"Помилка: {error}")


if __name__ == "__main__":
    main()