# Лабораторна робота № 5. Основи ООП в Python

## Варіант №7: Кіберспортивний менеджер

Проста програма для керування кіберспортивною командою.

## Класи

- `TeamMember` — абстрактний базовий клас учасника команди
- `Player`, `Coach`, `Staff` — підкласи (гравець, тренер, персонал)
- `TeamManager` — клас-менеджер, який керує всіма учасниками

## Структура

```
.
├── src/
│   ├── __init__.py
│   ├── team_member.py
│   ├── player.py
│   ├── coach.py
│   ├── staff.py
│   └── team_manager.py
├── tests/
│   ├── __init__.py
│   ├── test_members.py
│   └── test_team_manager.py
├── .gitignore
├── main.py
├── README.md
└── REPORT.md
```

## Запуск

Демонстрація:

```
python main.py
```

Тести:

```
python -m unittest -v
```
