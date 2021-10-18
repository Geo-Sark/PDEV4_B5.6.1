from random import randint

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i in range(3):
        print(f"  {i} | {' | '.join(field[i])} | ")
        print("  --------------- ")
    print()


def choise(a):
    ch = input("  Выберите X или 0,\n  или иное для \n  случайного выбора: ").upper()
    if ch == "X" or ch == "Х":
        m = 0
    elif ch == "0" or ch == "O" or ch == "О":
        m = 1
    else:
        m = randint(0, 1)
    print('       Вы Играете ', a[m],'\n')

    return m


def user():
    while True:
        cords = input("     Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты вне диапазона! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def ai():
    print("  Ход противника")
    while True:
        x, y = randint(0,2), randint(0,2)
        if field[x][y] != " ":
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for c in win_cord:
       if field[c[0][0]][c[0][1]] == field[c[1][0]][c[1][1]] == field[c[2][0]][c[2][1]] != " ":
           return True

    return False


greet()
field = [[" "] * 3 for i in range(3)]
a = ['X', '0']
b = ["Вы победили!!!", "Вы проиграли."]
turn = 0
show()
m = choise(a)
while True:
    if m % 2 == 0:
        x, y = user()
    else:
        x, y = ai()

    field[x][y] = a[turn % 2]
    show()
    if check_win():
        print(" Игра окончена.\n", b[m%2])
        break

    m += 1
    turn += 1

    if turn == 9:
        print(" Игра окончена.\n Ничья!")
        break