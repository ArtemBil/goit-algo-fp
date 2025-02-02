# Завдання 7: Використання методу Монте-Карло

## Опис завдання
Метою завдання було створення програми на Python, яка імітує процес кидання двох шестигранних кубиків. Ми обчислювали суми чисел, що випадали на кубиках, та підраховували частоту кожної можливої суми. Використовуючи ці частоти, ми визначали ймовірності кожної суми і порівнювали їх з аналітичними розрахунками.

## Реалізація методу Монте-Карло
Метод Монте-Карло передбачає багаторазове повторення експерименту для отримання наближених значень ймовірностей. У цьому випадку ми провели велику кількість кидків двох кубиків, підрахували кількість появ кожної суми (від 2 до 12) та обчислили відсоток кожної суми від загальної кількості кидків.

### Аналітичні ймовірності
Відомо, що аналітичні ймовірності випадіння кожної суми при киданні двох шестигранних кубиків такі:

| Сума | Ймовірність (%) | Частота (з 36) |
|------|-----------------|----------------|
| 2    | 2.78%           | 1/36           |
| 3    | 5.56%           | 2/36           |
| 4    | 8.33%           | 3/36           |
| 5    | 11.11%          | 4/36           |
| 6    | 13.89%          | 5/36           |
| 7    | 16.67%          | 6/36           |
| 8    | 13.89%          | 5/36           |
| 9    | 11.11%          | 4/36           |
| 10   | 8.33%           | 3/36           |
| 11   | 5.56%           | 2/36           |
| 12   | 2.78%           | 1/36           |

### Результати симуляції методом Монте-Карло
Ми провели 1000000 кидків кубиків та визначили наступні ймовірності:

| Сума | Ймовірність (%) (Монте-Карло) | Ймовірність (%) (Аналітична) |
|------|-------------------------------|------------------------------|
| 2    | 2.78%                         | 2.78%                        |
| 3    | 5.55%                         | 5.56%                        |
| 4    | 8.35%                         | 8.33%                        |
| 5    | 11.12%                        | 11.11%                       |
| 6    | 13.90%                        | 13.89%                       |
| 7    | 16.65%                        | 16.67%                       |
| 8    | 13.88%                        | 13.89%                       |
| 9    | 11.10%                        | 11.11%                       |
| 10   | 8.32%                         | 8.33%                        |
| 11   | 5.57%                         | 5.56%                        |
| 12   | 2.78%                         | 2.78%                        |

### Висновки
Зроблені висновки вказують на те, що отримані за допомогою методу Монте-Карло результати дуже близькі до аналітичних ймовірностей. Різниця між аналітичними ймовірностями та ймовірностями, отриманими симуляцією, є мінімальною. Це підтверджує, що метод Монте-Карло є ефективним підходом для оцінки ймовірностей, особливо в ситуаціях, де складно виконати точні аналітичні розрахунки.

### Основні висновки:
- **Коректність методу Монте-Карло**: Ймовірності, отримані методом Монте-Карло, наближаються до теоретичних значень, що свідчить про коректність алгоритму.
- **Практична користь**: Метод Монте-Карло може бути використаний для оцінки ймовірностей у складних системах, де аналітичні розрахунки є важкими або неможливими.
- **Відхилення**: Незначні відхилення від аналітичних значень зумовлені випадковістю симуляції, але зі збільшенням кількості симуляцій ці відхилення зменшуються.

Можемо зробити висновок, що метод Монте-Карло забезпечує надійні результати у випадку кидання двох кубиків.
