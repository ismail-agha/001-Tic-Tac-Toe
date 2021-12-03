
from IPython.display import clear_output

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def disp_board(board):
    clear_output()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Get Player's Marker (X or O)
def choose_marker():
    marker=''
    while marker not in ['X', 'O']:
        marker = input("Player-1, Please choose the marker (X or O) : ").upper()
        if marker not in ['X', 'O']:
            print(f" '{marker}' , Invalid. Choose either (X or O)")

    if marker=="X":
        return ('X', 'O')
    else:
        return ('O', 'X')

# Players Move
def place_move(board, marker, position):
    board[position] = marker
    disp_board(board)
    return board

# Check Winning Condition
def check_win(board, marker):
    #3-horizontal , 3-vertical, 2-diagonal : 8 conditions in total
    if  (
        board[0] == board[1] == board[2] == marker or
        board[3] == board[4] == board[5] == marker or
        board[6] == board[7] == board[8] == marker or

        board[0] == board[3] == board[6] == marker or
        board[1] == board[4] == board[7] == marker or
        board[2] == board[5] == board[8] == marker or

        board[0] == board[4] == board[8] == marker or
        board[2] == board[4] == board[6] == marker) :
        print(f"Bravo! Player {marker} Won")
        return True
    elif not space_available(board):
        return True

    return False

def space_available(board):
    for i in range(0,9):
        if board[i] not in ['X', 'O']:
            return True  # Space available , Continue

    print("DRAW!!!!!!")
    return False  # Stop

# validation
def validation(board, position):

    # check if out of range
    if position not in range(0,9):
        print(f"You have chosed position {position+1} which is not available. Please pick from 1 to 9")
        return False

    # check if already filled
    if board[position] in ['X', 'O']:
        print("Position already filled with " + board[position] + ". Please select other cell")
        return False
    return True



if __name__ == '__main__':
    board = ['1','2', '3','4','5','6','7','8','9']
    disp_board(board)
    player1_marker, player2_marker = choose_marker()
    #board = place_move(board, player1_marker, 5)

    player='1'
    position=0
    marker=''
    while not check_win(board, marker):
        if player=='1':
            position = int(input(f"Player 1 ({player1_marker}), select the position : ")) - 1
            while  not validation(board, position):
                position = int(input(f"Player 1 ({player1_marker}), select the position : ")) - 1


            place_move(board, player1_marker, position)
            player = '2'
            marker=player1_marker
        else:
            position = int(input(f"Player 2 ({player2_marker}), select the position : ")) - 1
            while not validation(board, position):
                position = int(input(f"Player 2 ({player2_marker}), select the position : ")) - 1
            place_move(board, player2_marker, position)
            player = '1'
            marker = player2_marker
    else:
        print("Game Over ...")