import random 
random.seed(1)
import numpy as np

def create_board():
    return np.zeros((3, 3), dtype=int)

def place(board, player , position):
    row, col = position
    
    if board[row, col] == 0:
        board[row, col] = player
    else:
        print(f"Position {position} is already taken!")
        
    return board
    
def possibilities(board):
 
    rows, cols = np.where(board == 0)
    
    return list(zip(rows, cols))

def random_place(board, player):
  
    selection = possibilities(board)
    
    if len(selection) > 0:
        random_position = random.choice(selection)
        board = place(board, player, random_position)
    else:
        print("No empty positions left on the board!")
        
    return board
    
def row_win(board , player):
  for row in board:
        if np.all(row == player):
            return True  
  return False
            
def col_win(board , player):
  for col in board.T:
        if np.all(col == player):
            return True    
  return False 
            
def diag_win(board , player):
    if board[0, 0] == board[1, 1] == board[2, 2] == player:
        return True
    elif board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    else:
        return False    

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board , player):
            winner = player
        if col_win(board , player):
            winner = player
        if diag_win(board , player):
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
    
def play_game():
    board = create_board()
    status = 0
    current_player = 1
    
    while status == 0:
        board = random_place(board, current_player)

        status = evaluate(board)
        
        if status == 0:
            if current_player == 1:
                current_player = 2
            elif current_player == 2:
                current_player = 1
            
    return status

results = []
for i in range(1000):
    results.append(play_game())

print(f"Player 1 Wins: {results.count(1)}")
print(f"Player 2 Wins: {results.count(2)}")




def play_strategic_game():
    board = create_board()
    board = place(board, player=1, position=(1, 1))
    status = evaluate(board)
    
    current_player = 2
    
    while status == 0:
        board = random_place(board, current_player)
        status = evaluate(board)
        
        if status == 0:
            if current_player == 1:
                current_player = 2
            elif current_player == 2:
                current_player = 1
                
    return status
random.seed(1)
results = []
for i in range(1000):
    results.append(play_strategic_game())

print(f"Player 1 Wins: {results.count(1)}")
print(f"Player 2 Wins: {results.count(2)}")
