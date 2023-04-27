game_zone = [[" "]*3 for i in range(3)]

def show_zone():
    print(f"  0 1 2")
    for i in range(3):
        info =" ".join(game_zone[i])
        print(f"{i} {info}")

show_zone()
def ask():
    while True:
            coordinates = input("         Ваш ход: ").split()

            if len(coordinates) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = coordinates

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            if 0 > x or x > 2 or 0 > y or y > 2:
                print(" введенные координаты вне диапазона! ")
                continue

            if game_zone[x][y] != " ":
                print(" Клетка занята! ")
                continue

            return x, y

ask()

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(game_zone[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

game_zone = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

check_win()



count = 0
while True:
    count += 1
    show_zone()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        game_zone[x][y] = "X"
    else:
        game_zone[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break