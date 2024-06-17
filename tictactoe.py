import random

# Define the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check for a win
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to make a move
def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Function to get available moves
def get_available_moves(board):
    return [i for i, x in enumerate(board) if x == ' ']

# Minimax algorithm to choose the best move
def minimax(board, depth, is_maximizing, player, opponent):
    if check_winner(board, opponent):
        return -10 + depth
    elif check_winner(board, player):
        return 10 - depth
    elif is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move] = player
            score = minimax(board, depth + 1, False, player, opponent)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            board[move] = opponent
            score = minimax(board, depth + 1, True, player, opponent)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

# Function to determine the AI move
def ai_move(board, player, opponent):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = player
        score = minimax(board, 0, False, player, opponent)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def main():
    player = 'X'
    ai = 'O'
    current_player = player if random.choice([True, False]) else ai

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        if current_player == player:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in get_available_moves(board):
                print("Invalid move. Try again.")
                continue
        else:
            move = ai_move(board, ai, player)
            print(f"AI chose position {move + 1}")

        make_move(board, move, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        current_player = ai if current_player == player else player

if __name__ == "__main__":
    main()
