"""Крестики-нолики. Запуск: python main.py"""


def show_board(board):
    print()
    for row in range(3):
        cells = [board[i] if board[i] != " " else str(i + 1)
                 for i in range(row * 3, row * 3 + 3)]
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def read_move(board, player):
    while True:
        value = input(f"Ход {player}. Введи номер клетки (1–9): ").strip()
        if value not in [str(number) for number in range(1, 10)]:
            print("Нужно ввести целое число от 1 до 9.")
            continue
        index = int(value) - 1
        if board[index] != " ":
            print("Эта клетка уже занята. Выбери другую.")
            continue
        return index


def play_game():
    board = [" "] * 9
    player = "X"
    show_board(board)
    for _ in range(9):
        index = read_move(board, player)
        board[index] = player
        show_board(board)
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_game()
