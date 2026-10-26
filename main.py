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


def has_won(board, player):
    lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    return any(all(board[index] == player for index in line) for line in lines)


def is_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    player = "X"
    show_board(board)
    for _ in range(9):
        index = read_move(board, player)
        board[index] = player
        show_board(board)
        if has_won(board, player):
            print(f"Победил {player}!")
            return
        if is_draw(board):
            print("Ничья!")
            return
        player = "O" if player == "X" else "X"


def main():
    while True:
        play_game()
        while True:
            answer = input("Сыграть ещё раз? (д/н): ").strip().lower()
            if answer in ("д", "да", "y", "yes"):
                break
            if answer in ("н", "нет", "n", "no"):
                print("До встречи!")
                return
            print("Введи д или н.")


if __name__ == "__main__":
    main()
