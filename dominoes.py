import random

snake, stock, player, computer = [], [], [], []
status = ""
count_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


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
        print('\n', *snake[0:3], '...', *snake[-3:], sep='')

    print("\nYour pieces:")
    n = 1
    for i in player:
        print(f'{n}:{i}')
        n += 1


def check_input(move_input):
    while True:
        try:
            if abs(int(move_input)) > len(player):
                move_input = int(input("Invalid input. Please try again."))
            return move_input
        except ValueError:
            move_input = input("Invalid input. Please try again.")


def left_rules(list_1, list_2):
    if list_1[0][0] == list_2[1]:
        return True, list_2[1]
    list_2.reverse()
    if list_1[0][0] == list_2[1]:
        return True, list_2[1]


def right_rule(list_1, list_2):
    if list_1[-1][1] == list_2[0]:
        return True, list_2[0]
    list_2.reverse()
    if list_1[-1][1] == list_2[0]:
        return True, list_2[0]
    return False


def check_illegal_move():
    global move, player_digit, player_move_val
    move = input("Illegal move. Please try again.")
    player_digit = int(check_input(move))


def count_comp_val(computer_, snakes, count_):
    for i in snakes:
        for j in i:
            if j in count_:
                count_[j] += 1
    for i in computer_:
        for j in i:
            if j in count_:
                count_[j] += 1


while True:
    display_output()
    if (snake[0][0] == snake[-1][1] and sum(x.count(snake[0][0]) for x in snake) == 8) or len(stock) == 0:
        print("Status: The game is over. It's a draw!")
        break
    if len(player) == 0:
        print("Status: The game is over. You won!")
        break
    if len(computer) == 0:
        print("Status: The game is over. The computer won!")
        break
    elif status == "player":
        move = input("Status: It's your turn to make a move. Enter your command.")
        player_digit = int(check_input(move))
        while True:
            player_move_val = player[abs(player_digit) - 1]
            if player_digit < 0:
                if left_rules(snake, player_move_val):
                    snake = [player_move_val] + snake
                    player.remove(player_move_val)
                    break
                check_illegal_move()
            elif player_digit == 0:
                player = player + [stock[0]]
                stock.remove(stock[0])
                break
            else:
                if right_rule(snake, player_move_val):
                    snake = snake + [player_move_val]
                    player.remove(player_move_val)
                    break
                check_illegal_move()
        status = "computer"

    else:
        move = input("Status: Computer is about to make a move. Press Enter to continue...")
        count_comp_val(computer, snake, count_dict)
        score = {}
        max_ = []
        for x in range(len(computer)):
            score.update({count_dict[computer[x][0]] + count_dict[computer[x][1]]: computer[x]})
        while True:
            max_score = score.pop(max(score))
            if left_rules(snake, max_score):
                snake = [max_score] + snake
                computer.remove(max_score)
                break
            if right_rule(snake, max_score):
                snake = snake + [max_score]
                computer.remove(max_score)
                break
            if not score:
                computer = computer + [stock[0]]
                stock.remove(stock[0])
                break
        status = "player"
