def print_board(board):
    print(board[0], '|', board[1], '|', board[2])
    print('--|---|--')
    print(board[3], '|', board[4], '|', board[5])
    print('--|---|--')
    print(board[6], '|', board[7], '|', board[8])

def check_winner(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Цикл игры
    while True:
        # Ход игрока 1
        player1_move = int(input('Ход игрока 1 (введите число от 1 до 9): '))
        if player1_move > 9 or player1_move <= 0:
            print("Ошибочный ввод, повторите(введите число от 1 до 9):")
            continue
        if str(board[player1_move - 1]) in 'XO':
            print("Клетка уже занята, выбириате другую")
            continue
        board[player1_move - 1] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print('Игрок 1 выиграл!')
            break
        # Ход игрока 2
        player2_move = int(input('Ход игрока 2 (введите число от 1 до 9): '))
        if player2_move > 9 or player2_move <= 0:
            print("Ошибочный ввод, повторите(введите число от 1 до 9):")
            continue
        if str(board[player2_move - 1]) in 'XO':
            print("Клетка уже занята, выбирите другую")
            continue
        board[player2_move - 1] = '0'
        print_board(board)
        if check_winner(board, '0'):
            print('Игрок 2 выиграл!')
            break


if __name__ == "__main__":
    main()