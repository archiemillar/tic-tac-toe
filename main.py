import pyfiglet
import random
from player import Player


T = "Tic Tac Toe"
available_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gn = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# display grid
def show_grid():
    grid = f" {gn[0]} | {gn[1]} | {gn[2]} \n" \
           f"-----------\n" \
           f" {gn[3]} | {gn[4]} | {gn[5]} \n" \
           f"-----------\n" \
           f" {gn[6]} | {gn[7]} | {gn[8]} \n"
    print(grid)


# Get current player
def current_player():
    if player_x.is_turn:
        return player_x
    else:
        return player_o


# Create Players
player_x = Player()
player_x.name = "X"
player_x.mark = "❌"

player_o = Player()
player_o.name = "O"
player_o.mark = "⭕️"

# show game name and grid
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)
show_grid()

# Ask player to choose a game mode
while True:
    game_type = input("Single Player or Multiplayer?: ").lower()
    if game_type == "single player" or game_type == "multiplayer":
        break
    print("Invalid mode. Please type a valid game mode.\n")

if game_type == "single player":
    while True:
        # user chooses to be X or O
        choice = input("X or O: ").upper()
        # Other player becomes computer
        if choice == "X":
            player_o.is_computer = True
            break
        elif choice == "O":
            player_x.is_computer = True
            break
        print("Invalid player. Please type a valid player.\n")

# Gameplay - Computer chooses a random number from available positions. Human player choose own number.
while True:
    if current_player().is_computer:
        number = random.choice(available_positions)
    else:
        print("Choose a grid number.")
        show_grid()
        number = int(input(f"{current_player().name}: "))

    print(f"{current_player().name} chose {number}.\n")

    # Human player's choice gets validated if within range and position still available
    if number < 1 or number > 9:
        print(f"{number} is out of range. Type a number within 1-9.\n")
    elif number not in available_positions:
        print(f"Grid {number} is already taken. Choose another number.\n")
    # if choice is valid
    else:
        available_positions.remove(number)
        gn[number - 1] = current_player().mark
        show_grid()

        # check if the player won or it's a draw
        if (gn[0] == gn[1] == gn[2] or gn[3] == gn[4] == gn[5] or gn[6] == gn[7] == gn[8] or
                gn[0] == gn[3] == gn[6] or gn[1] == gn[4] == gn[7] or gn[2] == gn[5] == gn[8] or
                gn[0] == gn[4] == gn[8] or gn[2] == gn[4] == gn[6]):
            print(f"{current_player().name} Wins!")
            break
        elif not available_positions:
            print("It's a Draw!")
            break

        # switch player turns
        if current_player() == player_x:
            player_x.is_turn = False
        else:
            player_x.is_turn = True
