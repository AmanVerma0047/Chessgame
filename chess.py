
board = [
    [" ","1"," 2"," 3"," 4"," 5"," 6"," 7"],
    ["1","♜","♞","♝","♚","♛","♝","♞","♜"],
    ["2","♟","♟","♟","♟","♟","♟","♟","♟"],
    ["3","."," ."," ."," ."," ."," ."," ."," .","."],
    ["4","."," ."," ."," ."," ."," ."," ."," .","."],
    ["5","."," ."," ."," ."," ."," ."," ."," .","."],
    ["6","."," ."," ."," ."," ."," ."," ."," .","."],
    ["7","♙","♙","♙","♙","♙","♙","♙","♙"],
    ["8","♖","♘","♗","♕","♔","♗","♘","♖"]
         ]

def print_board(get_pos1,get_pos2,get_pos3,get_pos4):
    piece = board[get_pos1][get_pos2]
    board[get_pos3][get_pos4] = piece
    board[get_pos1][get_pos2] = "."
    
    for row in range(0,len(board)-1):
        for col in range(0,len(board)-1):
            if row == 0 or row == 8 and row == 2 or row == 7:
                print(board[row][col],end = "  ")
            else:
                print(board[row][col],end = "  ")
        print("\n")
        

def get_input():
    #for i in range(0,len(board)):
       # print(board[i])
    for row in range(0,len(board)-1):
        for col in range(0,len(board)-1):
            if row == 0 or row == 8 and row == 2 or row == 7:
                print(board[row][col],end = "  ")
            else:
                print(board[row][col],end = "  ")
        print("\n")
    print("{player-1}")
    pos1 = int(input("enter row no.:"))
    pos2 = int(input("enter col no.:"))
    pos3 = int(input("where to move enter row no.:"))
    pos4 = int(input("where to move enter col no.:"))
    print("\n")
    print_board(pos1,pos2,pos3,pos4)
    print("{player-2}")
    pos1 = int(input("enter row no.:"))
    pos2 = int(input("enter col no.:"))
    pos3 = int(input("where to move enter row no.:"))
    pos4 = int(input("where to move enter col no.:"))
    print("\n")
    print_board(pos1,pos2,pos3,pos4)
    print("\n")

choice = "exit"
a = input("enter choice:")
while(a != choice):
    get_input()
