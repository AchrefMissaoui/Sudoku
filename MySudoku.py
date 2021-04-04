import sys


board = []
empties = [[],[],[],[],[],[],[],[],[]]
used_solutions={}



def build_empty_board():
    for i in range(9):
        temp = []
        for j in range(9): temp.append(0)
        board.append(temp)



def check_if_correct(x, y, num):
    x_range = range
    y_range = range
    is_correct = True
    for i in range(9):
        if board[x][i] == num: is_correct = False
        if board[i][y] == num: is_correct = False

    if x % 3 == 0:
        x_range = [1, 2]
    elif x % 3 == 1:
        x_range = [-1, 1]
    elif x % 3 == 2:
        x_range = [-1, -2]
    if y % 3 == 0:
        y_range = [1, 2]
    elif y % 3 == 1:
        y_range = [-1, 1]
    elif y % 3 == 2:
        y_range = [-1, -2]

    for i in x_range:
        for j in y_range:
            if board[x+i][y+j] == num:
                is_correct = False
    return is_correct


def print_board():
    for i in range(9):
        print(board[i])

def find_empties():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0 : empties[i].append(j)




def solve_board():
    i   = 0
    while i < 9 :
        j = 0
        while j < len(empties[i]):
            for solution in range(1,10):
                item_string = i,j
                if used_solutions.__contains__(item_string) == False: used_solutions[item_string] = []
                if used_solutions[item_string].__contains__(solution) == False:
                    if check_if_correct(i,empties[i][j],solution) :
                        board[i][empties[i][j]] = solution
                        used_solutions[item_string].append(solution)
                        break
                else :
                    board[i][empties[i][j]] = 0

            if board[i][empties[i][j]] == 0 :
                if j > 0 :
                    used_solutions.pop(item_string)
                    j -=1
                elif i>0:
                    used_solutions.pop(item_string)
                    i -=1
                    j =len(empties[i])-1
                else :
                    print('error')
                    print_board()
                    sys.exit()

            else :
                j += 1
        i+=1




build_empty_board()
board=[ [0,0,6,0,0,0,8,0,4],
        [9,0,0,3,0,0,0,7,0],
        [0,0,0,0,0,0,0,0,0],
        [5,0,0,8,0,0,2,0,1],
        [0,0,0,0,6,0,0,5,0],
        [0,6,4,9,0,5,0,8,0],
        [0,0,1,0,0,3,0,0,8],
        [0,0,5,0,1,0,0,0,6],
        [4,8,7,2,9,6,0,3,0]]
print_board()
print("###################################")
find_empties()
solve_board()
print('SOLUTION')
print_board()
