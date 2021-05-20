def greet():
    print("_______________")
    print(" Приветствуем\n    В игре \nКрестики-Нолики")
    print("Формат ввода: x y\nx - номер строки \ny - номер столбца")


field = [[" "] * 3 for i in range(3)]


def view():
    print()
    print(f"   | 0 | 1 | 2 |")
    print(" ---------------")
    for i, row in enumerate(field):
        row_ = f" {i} | {' | '.join(row)} | "
        print(row_)
        print(" ---------------")
    print()


def ask():
    while True:
        cords = input("Сделайте ход: ").split()
        if len(cords) != 2:
            print('Введите 2 координаты')
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа")
            continue
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] != " ":
                print(" Занято! ")
                continue
        else:
            print(" Введите координаты от 0 до 2 ")
            continue
        return x, y


def battle():
    greet()
    num = 0
    while True:
        num += 1
        view()
        if num % 2 == 1:
            print("Ходит крестик")
        else:
            print("Ходит нолик")

        x, y = ask()

        if num % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"
        if win():
            break
        if num == 9:
            print("Ничья")
            break


def win():
    win_cords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cords:
        symbols = []
        for i in cord:
            symbols.append(field[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print("!Выиграл X!")
            return True
        if symbols == ["0", "0", "0"]:
            print("!Выиграл 0!")
            return True


battle()
