def loadBoard(filename):
    board = []
    file = open(filename, "r")
    
    for line in file:
        row = list(line.strip())
        board.append(row)
        
    file.close()
    return board

        
def switchPlayer(current_player):
    if current_player == "B":
        return "W"
    else:
        return "B"


def find_inside(board):
    rows = len(board)
    cols = len(board[0])
    visited = []

    for i in range(rows):
        for j in range(cols):

            if board[i][j] == "." and (i, j) not in visited:

                stack = [(i, j)]
                region = []
                borders = []

                while len(stack) > 0:
                    x, y = stack.pop()

                    if (x, y) in visited:
                        continue

#didn't know what i was doing


def floodfill(matrix, x, y, color):
    if matrix[x][y] == ".":  
        matrix[x][y] = color 

        if x > 0:
            floodfill(matrix, x-1, y, color)
        if x < len(matrix) - 1:
            floodfill(matrix, x+1, y, color)
        if y > 0:
            floodfill(matrix, x, y-1, color)
        if y < len(matrix[0]) - 1:
            floodfill(matrix, x, y+1, color)


def countScore(board):
    black = 0
    white = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "B":
                black += 1
            elif board[i][j] == "W":
                white += 1

    return black, white


def printBoard(board):
    for row in board:
        print("".join(row))


def main():
    board = [
        list("BBBBB....."),
        list("B...B....."),
        list("B...B....."),
        list("BBBBB....."),
        list(".WWWWW...."),
        list(".W....W..."),
        list(".W.....W.."),
        list(".WWWWWWW.."),
        list(".........."),
        list("..........")
    ]


    print("Original Board:")
    printBoard(board)

    find_inside(board)

    print("Filled Board:")
    printBoard(board)

    black, white = countScore(board)

    print("Black:", black)
    print("White:", white)

    if black > white:
        print("Black wins")
    elif white > black:
        print("White wins")
    else:
        print("Tie")


if __name__ == "__main__":
    main()