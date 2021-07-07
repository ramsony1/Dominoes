import random

snake, stock, player, computer = [], [], [], []
status = ""


def starter_piece():
    computer_player = computer + player
    doubles = [piece for piece in computer_player if piece[0] == piece[1]]
    if not doubles:
        return False
    snake.append(max(doubles))
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

print("=" * 70)
print(f"Stock size: {len(stock)}")
print(f'Computer size: {len(computer)}\n')
print(snake[0])
print("\nYour pieces:")
n = 1
for i in player:
    print(f'{n}:{i}')
    n += 1
if status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")

