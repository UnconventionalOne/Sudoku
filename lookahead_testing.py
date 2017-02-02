import random

def drawBoard(board):
    # Prints the list from board in a legible way
    horiz = '  '+'+---'*(9)+'+'
    horiz2 = '  '+'+-*-'*(9)+'+' # Alternate horiz
    line_numbers = '    ' + '   '.join(str(a+1) for a in range(9))
    print line_numbers 
    print horiz

    for y in range(9):
        print y+1,
        for x in range (9):
            if (x)%3 == 0 and x != 0:# and x+1 != 9:
                print '* %s' % (board[x][y]),
            else:
                print '| %s' % (board[x][y]),
        print '|'
        if (y+1)%3 == 0 and (y+1) != 9:
            print horiz2
        else:
            print horiz

b1c = [[x,y] for x in range(0,3) for y in range(0,3)]
b4c = [[x,y] for x in range(0,3) for y in range(3,6)]
b7c = [[x,y] for x in range(0,3) for y in range(6,9)]
b2c = [[x,y] for x in range(3,6) for y in range(0,3)]
b5c = [[x,y] for x in range(3,6) for y in range(3,6)]
b8c = [[x,y] for x in range(3,6) for y in range(6,9)]
b3c = [[x,y] for x in range(6,9) for y in range(0,3)]
b6c = [[x,y] for x in range(6,9) for y in range(3,6)]
b9c = [[x,y] for x in range(6,9) for y in range(6,9)]
bclist = [b1c, b2c, b3c, b4c, b5c, b6c, b7c, b8c, b9c]
####[set(x) for x in bclist]

##################################################
def isBoardValid(board, bclist):
    blocks = [[board[x][y] for (x,y) in bc] for bc in bclist]
    rows = [[board[x][y] for x in range(9)] for y in range(9)]
    columns = board
    tfblocks = [sorted(x) == range(1, 10) for x in blocks]
    tfrows = [sorted(x) == range(1, 10) for x in rows]
    tfcolumns = [sorted(x) == range(1, 10) for x in columns]
    if False not in tfblocks and False not in tfrows and False not in tfcolumns:
        return True
    else:
        return False
##################################################


# Below returns the list of all candidates for every cell                    
def getPossibles(board, bclist):
    possibles = [[[] * 9 for x in range(9)]for y in range(9)]
    for C, col in enumerate(possibles):
        column = board[C]
        for R, place in enumerate(col):
            for bc in bclist:
                if [C, R] in bc:
                    block = [board[x][y] for (x,y) in bc]
                row = [board[x][R] for x in range(9)]
            if board[C][R] != ' ':
                possibles[C][R] = [board[C][R]]
            else:
                possibles[C][R] = [d for d in range(1,10) if d not in row and d not in column and d not in block]
    return possibles


# Below implements the two simplest logical solving methods (the only ones currently included)
def testPossibles(board, bclist):#rlist, blist):
    # Guess I can call it as: board = testPossibles()
    possibles = getPossibles(board, bclist)
    dupeBoard = getBoardCopy(board)
    h = 0
    changed = False
    while True:
        h += 1
        for C in range(9):
            for R in range(9):
                cell = possibles[C][R]
##                possibles = getPossibles(dupeBoard, bclist)
                nakedSingle = getNakedSingle(dupeBoard, C, R, cell)
                if nakedSingle:
                    val = nakedSingle
                    print 'naked single', val, 'at', C+1, R+1
                else:
                    val = getHiddenSingle(dupeBoard, possibles, bclist, C, R, cell)
                    if val:
                        print 'hidden single', val, 'at', C+1, R+1
                if val:
                    h = 0
##                    dupeBoard[C][R] = val
                    makeMove(dupeBoard, C, R, val)
                    possibles = getPossibles(dupeBoard, bclist)
                    changed = True
                elif cell == []: #have to backtrack maybe I should have a backtrack func or something
                    print 'testPossibles ran into empty candidate list. Maybe implement'\
                          + ' backtracking,? Or just discard current board and try again?'
                    raise Exception
        if h == 1:
            break
    if changed:
        return dupeBoard
    else:
        return board


def getNakedSingle(board, C, R, cell):
    # cell reffers to cell specific candidates
    if len(cell) == 1 and board[C][R] == ' ':
        return cell[0]

    
# Below checks if any of the candidates in a cell are actually hidden singles.
# Edited to be called under testPossibles.
def getHiddenSingle(board, possibles, bclist, C, R, cell):
    if board[C][R] == ' ':
        # List of all possibles in row, column, block of a cell, except possibles of that cell
        for bc in bclist:
            if [C, R] in bc:
                pblock = [possibles[x][y] for (x,y) in bc if (x,y) != (C,R)]# and board[x][y] == ' '
        prow = [possibles[x][R] for x in range(9) if x != C]# and board[x][R] == ' '
        pcolumn = [pvals for p, pvals in enumerate(possibles[C]) if p != R]# and board[C][p] == ' '

        rset = set(x for y in prow for x in y)
        cset = set(x for y in pcolumn for x in y)
        bset = set(x for y in pblock for x in y)

        for pval in cell:
            # If only instance of that possible value in c,r, or b, then has to be that value
            if pval not in bset or pval not in rset or pval not in cset:
##                print pval, 'seems to be a single at x =', C, 'and y =', R
                return pval


# lookAhead trial
# Cycles through available possible moves at a cell, trying them on a duplicate
# board to see if placing that move results in a spot on the board without any
# possibles. If none of the possibles work, this function fails.
def lookAhead(board, possibles, bclist, rang, i, j):
    for move in rang:
        if move in possibles[i][j]: 
            dupeBoard = getBoardCopy(board)
            dupeBoard[i][j] = move
            dupePossibles = getPossibles(dupeBoard, bclist)
            dupe = True
            for co in dupePossibles:
                for ro in co:
                    if ro == []:
                        dupe = False
                        break
            if dupe == True:
                return move
            elif move == possibles[i][j][len(possibles[i][j])-1] and dupe == False:
                # not set up to deal with this yet
                print 'Lookahead failure. Need backtracking?'
                raise Exception


def getBoardCopy(board):
    # Duplicate board for looking ahead
    dupeBoard = [[board[x][y] for y in range(9)] for x in range(9)]
    return dupeBoard


# This function is probably unneccesary, but I was having problems and thought
# this might help......
def makeMove(board, x, y, val):
    board[x][y] = val
    return True

##############################

board = [[' '] * 9 for x in range(9)]
i = 0
while i < 9:
    # Don't even remember why I originally had column, row and board here...
    # but it't not being used for anything now, lol
##    column = board[i]
    j = 0
    rang = range(1,9+1)
    random.shuffle(rang)
    while j < 9:
        if board[i][j] == ' ': #think I need to include this or something like it
            print ' i =',i, 'j =', j
##            for bc in bclist:
##                if [i,j] in bc:
##                    block = [board[x][y] for (x,y) in bc]
##            row = [board[x][j] for x in range(9)]
##            possibles = getPossibles(board, bclist)
            board = testPossibles(board, bclist)
            if board[i][j] == ' ':
                possibles = getPossibles(board, bclist)
                move = lookAhead(board, possibles, bclist, rang, i, j)
                print 'move =', move
                makeMove(board, i, j, move)
        j+=1
    i+=1

# For simple testing
valid = isBoardValid(board, bclist)
print 'valid =', valid
if valid: drawBoard(board)
