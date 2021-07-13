import itertools
import random

snake, stock, player, computer = [], [], [], []
status = ""


def starter_piece():
    computer_player = computer + player
    double_piece = [piece for piece in computer_player if piece[0] == piece[1]]
    if not double_piece:
        return False
    snake.append(max(double_piece))
    if snake[0] in computer:
        computer.remove(snake[0])
        return "player"
    player.remove(snake[0])
    return "computer"


while not status:
    domino_pieces = [[i, j] for i in range(7) for j in range(i, 7)]
    random.shuffle(domino_pieces)
    computer, player, stock = domino_pieces[:7], domino_pieces[7:14], domino_pieces[14:]
    status = starter_piece()


def display_output():
    global n, i
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f'Computer piece: {len(computer)}\n')
    print({True: f"{snake[:3]}...{snake[-3:]}", False: snake}[len(snake) > 6])

    print("\nYour pieces:")
    n = 1
    for i in player:
        print(f'{n}:{i}')
        n += 1


display_output()

while True:
    if status == "player":
        move = input("Status: It's your turn to make a move. Enter your command.")
        try:
            move_digit = int(move)
        except ValueError:
            while True:
                move = input("Invalid input. Please try again.")
                try:
                    move_digit = int(move)
                    break
                except ValueError:
                    pass
        if move_digit < 0:
            snake = [player[abs(move_digit) - 1]] + snake
            player.remove(player[abs(move_digit) - 1])
            display_output()
            status = "computer"
        elif move_digit == 0:
            player = player + [stock[0]]
            stock.remove(stock[0])
            display_output()
            status = "computer"
        else:
            snake = snake + [player[move_digit - 1]]
            player.remove(player[move_digit - 1])
            display_output()
            status = "computer"

    else:
        move = input("Status: Computer is about to make a move. Press Enter to continue...")
        display_output()
        status = "player"
