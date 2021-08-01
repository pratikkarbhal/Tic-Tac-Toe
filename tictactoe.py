#Python_Tic-Tac-Toe_by_Pratik_Karbhal

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game status
game_still_going = True

# Winner
winner = None

# current player (X first)
current_player = "X"


# ------------- Functions ---------------

# Play
def play_game():

  # Initial game board
  display_board()

  # Loop
  while game_still_going:

    # Each turn
    handle_turn(current_player)

    # Check
    check_if_game_over()

    # Other player
    flip_player()
  
  # Win or Tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle a turn
def handle_turn(player):

  # Get position
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index
    position = int(position) - 1

    # is spot available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put mark
  board[position] = player

  # Show board
  display_board()


# Check
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Check win
def check_for_winner():
  # Global variables
  global winner
  # Check win
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check win rows
def check_rows():
  # Global variables
  global game_still_going
  # Checking if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, its a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 
  # Or tie
  else:
    return None


# Check win column
def check_columns():
  # Global variables
  global game_still_going
  # Checking if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any row does have a match, its a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 
  # Or tie
  else:
    return None


# Check win diagonal
def check_diagonals():
  # Global variables
  global game_still_going
  # Checking if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any row does have a match, its a win
  if diagonal_1 or diagonal_2:
    game_still_going = False
  # Winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]
  # Or tie
  else:
    return None


# Checking if there is a tie
def check_for_tie():
  # Global variables
  global game_still_going
  # Full
  if "-" not in board:
    game_still_going = False
    return True
  # No tie
  else:
    return False


# X to O, or O to X
def flip_player():
  # Global variables we need
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"


# Run
play_game()
