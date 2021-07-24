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
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f'Computer piece: {len(computer)}\n')

    if len(snake) <= 6:
        for i in snake:
            print(i, end='')
    else:
        print(*snake[0:3], '...', *snake[-3:], sep='')

    print("\nYour pieces:")
    n = 1
    for i in player:
        print(f'{n}:{i}')
        n += 1


while True:
    display_output()
    if status == "player":
        move = input("Status: It's your turn to make a move. Enter your command.")
        try:
            player_digit = int(move)
            while abs(player_digit) > len(player):
                player_digit = int(input("Number too high. Enter your command."))
        except ValueError:
            while True:
                move = input("Invalid input. Please try again.")
                try:
                    player_digit = int(move)
                    while abs(player_digit) > len(player):
                        player_digit = int(input("Number too high. Enter your command."))
                    break
                except ValueError:
                    pass
        if player_digit < 0:
            snake = [player[abs(player_digit) - 1]] + snake
            player.remove(player[abs(player_digit) - 1])
            status = "computer"
        elif player_digit == 0:
            player = player + [stock[0]]
            stock.remove(stock[0])
            status = "computer"
        else:
            snake = snake + [player[player_digit - 1]]
            player.remove(player[player_digit - 1])
            if len(player) == 0:
                display_output()
                print("Status: The game is over. You won!")
                break
            status = "computer"

    else:
        move = input("Status: Computer is about to make a move. Press Enter to continue...")
        computer_digit = random.choice(range(-len(computer), len(computer)))
        if computer_digit < 0:
            snake = [computer[abs(computer_digit) - 1]] + snake
            computer.remove(computer[abs(computer_digit) - 1])
            status = "player"
        elif computer_digit == 0:
            computer = computer + [stock[0]]
            stock.remove(stock[0])
            status = "player"
        else:
            snake = snake + [computer[computer_digit - 1]]
            computer.remove(computer[computer_digit - 1])
            if len(computer) == 0:
                display_output()
                print("Status: The game is over. You won!")
                break
            status = "player"
