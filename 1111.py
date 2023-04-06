board = list(range(1, 10))

wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw():
    print(f"-------------")
    for i in range(3):
        print(f"|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print(f"-------------")


def inp(player):
    while True:
        val = input("Куда поставить крестик " + player + "? ")
        if not (val in '123456789'):
            print("Ошибочный ввод, повторите")
            continue
        val = int(val)
        if str(board[val - 1]) in 'XO':
            print("Клетка занята")
            continue
        board[val - 1] = player
        break


def chek():
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    count = 0
    while True:
        draw()
        if count % 2 == 0:
            inp('X')
        else:
            inp('O')
        if count > 3:
            winner = chek()
            if winner:
                draw()
                print(winner, "Выиграл")
                break
        count += 1
        if count > 8:
            draw()
            print("ничья")
            break


main()