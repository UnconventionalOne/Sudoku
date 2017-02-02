import random, time

###########Old#Functions#########Old#Functions#########Old#Functions############
def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = '  '+'+---'*(9)+'+'
    HLINE2 = '  '+'+-*-'*(9)+'+' # Alternate HLINE
    line_numbers = '    ' + '   '.join(str(a+1) for a in range(9))
    print line_numbers 
    print HLINE

    for y in range(9):
        print y+1,
        for x in range (9):
            if (x)%3 == 0 and x != 0:# and x+1 != 9:
                print '* %s' % (board[x][y]),
            else:
                print '| %s' % (board[x][y]),
        print '|'
        if (y+1)%3 == 0 and (y+1) != 9:
            print HLINE2
        else:
            print HLINE

            
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


def getPossibles(board, bclist):
    possibles = [[[] for x in range(9)]for y in range(9)]
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

##################getPossibles##########set####version##########################
# Would require changes to rest of script since sets don't support indexing
##def getPossibles(board, bclist):
##    possibles = [[[] for x in range(9)]for y in range(9)]
##    for C, col in enumerate(possibles):
##        column = board[C]
##        for R, place in enumerate(col):
##            for bc in bclist:
##                if [C, R] in bc:
##                    block = (board[x][y] for (x,y) in bc)
##                row = (board[x][R] for x in range(9))
##            if board[C][R] != ' ':
##                possibles[C][R] = set([board[C][R]])
##            else:
####                rang = range(1,10)
##                possibles[C][R] = set(range(1,10)).difference(block, column, row)
##    return possibles
##################getPossibles##########set####version##########################


def getBoardCopy(board):
    # idea from what's his face's python reversi since my simpler
    dupeBoard = [[board[x][y] for y in range(9)] for x in range(9)]
    return dupeBoard


# Combined all since havn't actually used parts individually
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
###########New#Functions#########New#Functions#########New#Functions############
#in case I feel like changing bclist into dictionary...this probably isn't how..
##dict([('b' + str(n+1) + 'c', x) for n, x in enumerate(bclist)])
##########

# Since intended to be able to be used with a partial board, will need
# -dupeBoard

### I guess the main rule should be: if num == 9 and invalid, backstep
##def bruteForceOne(board, bclist):
##    # Takes board passed to it, even an empty board, and tries to solve it
####    candidates = getPossibles(board, bclist)
##    dupeBoard = getBoardCopy(board)
##    solved = False
##    while not solved:
##        C = 0
##        while C < len(dupeBoard):
##            R = 0
##            while R < len(dupeBoard[C]):
##                dval = dupeBoard[C][R]
##                bval = board[C][R]
##                if bval == ' ': #maybe should compile range of all empty?
##                    #check if this value conflicts at all
##                    valid = validateCell(dupeBoard, bclist, C, R)
##                    # go to last value in dupeBoard that's not in board. If
##                    # valid, continue to next position. If not valid, try
##                    # increasing it by 1 unless already 9, in which case back-
##                    # step
##                    if dval == 9: # if == 9 here, then already had to backrack..
##                        dval = ' '
##                        if R != 0: # if not first cell in column, R-1
##                            R -= 1+1
##                        else: # if first cell in column, go back to last column
##                            C -= 1+1 
##                            R = 8-1
##                    elif dval == ' ':
##                        dval = 1
##                    else:
##                        dval += 1
##                        valid = validateCell(dupeBoard, bclist, C, R)
##                        if dval == 9 and dval not valid:
##                            dval = ' '
##                            if R != 0: # if not first cell in column, R-1
##                                R -= 1+1
##                            else: # if first cell in column, go back to last column
##                                C -= 1+1 
##                                R = 8-1
##                        else:
##                            pass
##                    if C == 8 and R == 8:
##                        if dval is valid:
##                            if isBoardValid(board, bclist):
##                                solved = True
##                            else:
##                                print 'Got to the end, so this should be valid'\
##                                      +" but for some reason it's not"
##                                raise Exception
##                        elif dval not valid:
##                            print 'dval not valid. No solution?'
##                            # obviously not how this part should be done but...
##                            raise Exception
##                R += 1
##            C += 1
##    return dupeBoard

# Maybe I should use the possibles from the board, not dupeBoard, for all of it
# then: if get to the end of possibles for a cell and not valid, backtrack...
# Not thinking at the moment how I should catch that the board has no solutions
##############Take 2

# Incomplete: don't run this function
##def bruteForceOne(board, bclist):
##    bCans = getPossibles(board, bclist)
##    dupeBoard = getBoardCopy(board)
####    solved = False
####    while not solved:
##    tic = 0
##    C = 0
##    while C < 9:
##        R = 0
##        while R < 9:
##            dval = dupeBoard[C][R]
##            bval = board[C][R]
##            candidates = bCans[C][R]
##            if bval == ' ':
##                if dval != ' ':
##                    if dval == candidates[-1]: #if dval == last candidate
##                        dval = ' '
##                        if R != 0: # if not first cell in column, R-1
##                            R -= 2
##                        else: # if first cell in column, go back a column
##                            C -= 1
##                            R = 7
##                    else: #if not last candidate
##                        indx = candidates.index(dval)
##                        dval = candidates[indx+1]
##                        valid = validateCell(dupeBoard, bclist, C, R)
##                        if not valid:
##                            R -= 1 #return to 
##                        else:
##                            pass#probably nothing
##                else: #if dval == ' '
##                    dval = candidates[0]
##            dupeBoard[C][R] = dval
##            R += 1
##        C += 1
##    return dupeBoard
####    if solved:
####        print 'tic =', tic
####        return dupeBoard
####    else:
####        print 'tic =', tic
####        return board


############## ^^^^bruteForceOne^^^^take 2^^^^^###########
###################bruteForceTwo####take 1################

### bFTWo is for partially completed boards...
### Incomplete but usable
##def bruteForceTwo(board, bclist):
##    start = time.time()
##    tic = 0 # try to see how many cylces it runs
##    bCans = getPossibles(board, bclist)
##    # empties gives the positions on the board that need to be filled in
##    empties = [[x, y] for x, col in enumerate(board) for y, cell in enumerate(col) if cell == ' ']
##    dupeBoard = getBoardCopy(board)
##    i = 0
##    while i < len(empties):
##        x, y = empties[i]
##        dval = dupeBoard[x][y]
##        candidates = bCans[x][y]
##        if dval != ' ':
##            if dval == candidates[-1]: #if dval == last candidate
##                dupeBoard[x][y] = ' '
##                i -= 2
##            else: #if not last candidate
##                indx = candidates.index(dval)
##                dupeBoard[x][y] = candidates[indx+1]
##                valid = validateCell(dupeBoard, bclist, x, y)
##                if not valid:
##                    i -= 1
##        else: # if dval == ' '
##            dupeBoard[x][y] = candidates[0]
##            valid = validateCell(dupeBoard, bclist, x, y)
##            if not valid:
##                i -= 1
####        dupeBoard[x][y] = dval
##        i += 1
##        tic += 1
##    end = time.time()
##    print 'elapsed time =', end - start
##    print 'tic =', tic
##    return dupeBoard

# Once update version is complete, can update possibles while moving forward,
# but would have to use the original method when going backword or no options
# would be available

###################bruteForceTwo####take 1################
###################bruteForceTwo####take 2################

# Try updating possibles every time. Speed problem because I don't yet have a way
# to update and can only create anew each time...

# Doesn't work lol. Stepping through the number of candidates as if immutable
# doesn't work so well when I change them....

##def bruteForceTwo(board, bclist):
##    tic = 0 # try to see how many cylces it runs
####    bCans = getPossibles(board, bclist)
##    empties = [[x, y] for x, col in enumerate(board) for y, cell in enumerate(col) if cell == ' ']
##    dupeBoard = getBoardCopy(board)
##    i = 0
##    while 0 <= i < len(empties):
##        x, y = empties[i]
##        dval = dupeBoard[x][y]
##        bCans = getPossibles(dupeBoard, bclist)
##        candidates = bCans[x][y]
##        if candidates == []:
##            dupeBoard[x][y] = ' '
##            i -= 2
##        elif dval != ' ':
##            if dval == candidates[-1]: #if dval == last candidate
##                dupeBoard[x][y] = ' '
##                i -= 2
##            else: #if not last candidate
##                indx = candidates.index(dval)
##                dupeBoard[x][y] = candidates[indx+1]
##                valid = validateCell(dupeBoard, bclist, x, y)
##                if not valid:
##                    i -= 1
##        else: # if dval == ' '
##            dupeBoard[x][y] = candidates[0]
##            valid = validateCell(dupeBoard, bclist, x, y)
##            if not valid:
##                i -= 1
####        dupeBoard[x][y] = dval
##        i += 1
##        tic += 1
##    print 'tic =', tic
##    return dupeBoard

###################bruteForceTwo####take 2################
###################bruteForceTwo####take 1.1################
# Just added simple ability to recognize when board is invalid, compared to take 1...

def bruteForceTwo(board, bclist):
    start = time.time()
    tic = 0 # try to see how many cylces it runs
    bCans = getPossibles(board, bclist)
    for Cans in bCans:
        if [] in Cans:
            print "No solution. Puzzle invalid. Didn't even need to run algorithm."
            return board
    # empties gives the positions on the board that need to be filled in
    empties = [[x, y] for x, col in enumerate(board) for y, cell in enumerate(col) if cell == ' ']
    dupeBoard = getBoardCopy(board)
    i = 0
    while i < len(empties):
        x, y = empties[i]
        dval = dupeBoard[x][y]
        candidates = bCans[x][y]
        if dval != ' ':
            if dval == candidates[-1]: #if dval == last candidate
                if i == 0:
                    print "No solution. Puzzle invalid."
                    end = time.time()
                    print 'elapsed time =', end - start
                    print 'tic =', tic
                    return board
                else:
                    dupeBoard[x][y] = ' '
                    i -= 2
            else: #if not last candidate
                indx = candidates.index(dval)
                dupeBoard[x][y] = candidates[indx+1]
                valid = validateCell(dupeBoard, bclist, x, y)
                if not valid:
                    i -= 1
        else: # if dval == ' '
            dupeBoard[x][y] = candidates[0]
            valid = validateCell(dupeBoard, bclist, x, y)
            if not valid:
                i -= 1
##        dupeBoard[x][y] = dval
        i += 1
        tic += 1
    end = time.time()
    print 'elapsed time =', end - start
    print 'tic =', tic
    return dupeBoard

###################bruteForceTwo####take 1.1################
###################validateCell#####take 1################

##def validateCell(board, bclist, C, R):
##    val = board[C][R]
##    # since they are only going to be used once, I'll try using generator objs
##    for bc in bclist:
##        if [C, R] in bc:
##            block = (board[x][y] for (x,y) in bc if (x,y) != (C,R))
##    row = (board[x][R] for x in range(9) if x != C)
##    column = (cval for c, cval in enumerate(board[C]) if c != R)
##    if val not in block and val not in row and val not in column:
##        return True
##    else:
##        return False
###################validateCell#####take 1################
###################validateCell#####take 2################

# Remake of validateCell so it doesn't go though all options each time unless it has to...
# Seems to be a little bit faster...maybe...at least for the harder cases
def validateCell(board, bclist, C, R):
    val = board[C][R]
    for bc in bclist:
        if [C, R] in bc:
            block = (board[x][y] for (x,y) in bc if (x,y) != (C,R))
    if val in block:
        return False
    row = (board[x][R] for x in range(9) if x != C)
    if val in row:
        return False
    column = (cval for c, cval in enumerate(board[C]) if c != R)
    if val in column:
        return False
    return True

###################validateCell#####take 2################
##############line_to_board#####and#####board_to_line####take 1#################

# Takes line of text and converts to board format. Allows "0" or "." for empty
# and ignores everythin else besides digits.
def line_to_board(line): # absurdly long implementation, I know...
    lst = [[' ']*9 for x in range(9)] # board format currenlty used
    digits = '123456789'
    bloop = -1
    for char in line:
        if char in digits:
            bloop += 1
            x = bloop % 9
            y = bloop / 9
            lst[x][y] = int(char)
        elif char in '0.':
            bloop += 1
    return lst


# Takes a board in the native format and converts it to a sting using .s for empties
def board_to_line(board): # possibly even more absurd than the above, but it works :)
    strrows = [[str(board[x][y]) if board[x][y] != ' ' else '.' for x in range(9)] for y in range(9)]
    temp = []
    for row in strrows:
        temp.append("".join(row))
    return ''.join(temp)

##############line_to_board#####and#####board_to_line####take 1#################

                        
##########
# Some example boards for testing:

InvalidLOL = [[' ', ' ', 2, ' ', ' ', ' ', ' ', ' ', ' '], [' ', 5, ' ', 4, ' ', ' ', ' ', ' ', ' '], [' ', 9, ' ', 5, 3, 6, ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 3, ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 2, ' ', ' '], [6, ' ', 8, ' ', ' ', 3, 5, ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 5, ' ', ' ', ' '], [' ', 8, ' ', ' ', ' ', 4, 6, ' ', ' ']]
# found a solution in 741 tics, and 0.012 sec.

OtherArto = [[' ', 8, ' ', 4, ' ', ' ', ' ', ' ', ' '], [' ', ' ', 7, ' ', 1, ' ', 6, ' ', ' '], [5, ' ', ' ', ' ', ' ', 3, ' ', 4, ' '], [3, ' ', ' ', ' ', ' ', 2, 5, ' ', ' '], [' ', ' ', 1, ' ', 7, ' ', ' ', ' ', ' '], [' ', ' ', ' ', 5, ' ', ' ', ' ', ' ', 9], [' ', ' ', 5, 3, ' ', ' ', ' ', ' ', 7], [' ', 2, ' ', ' ', ' ', 8, ' ', 3, ' '], [' ', ' ', ' ', ' ', 6, ' ', 9, ' ', ' ']]
# tics to beat = 127225 (0.802 sec). Norvig took 0.01 sec...

# Below are from http://www.sudokuwiki.org/sudoku.htm

Easiest = [[' ', 1, ' ', ' ', 9, ' ', ' ', ' ', ' '], [' ', 4, 8, 6, ' ', 1, ' ', 2, ' '], [' ', ' ', ' ', 3, ' ', ' ', 7, 6, ' '], [1, ' ', ' ', ' ', ' ', ' ', 2, ' ', 4], [' ', ' ', ' ', 7, ' ', 9, ' ', ' ', ' '], [5, ' ', 2, ' ', ' ', ' ', ' ', ' ', 9], [' ', 6, 4, ' ', ' ', 5, ' ', ' ', ' '], [' ', 7, ' ', 1, ' ', 2, 8, 3, ' '], [' ', ' ', ' ', ' ', 3, ' ', ' ', 5, ' ']]
# 28 clues. tics to beat = 5344 (0.035 sec). Andrew Stuart's only took 832

Tough = [[3, 2, ' ', 7, 6, ' ', ' ', ' ', ' '], [' ', ' ', 8, 5, ' ', 2, ' ', ' ', ' '], [9, ' ', 7, ' ', ' ', 8, ' ', ' ', 6], [' ', 7, ' ', ' ', 9, ' ', ' ', 1, ' '], [' ', ' ', ' ', 6, ' ', 5, ' ', ' ', ' '], [' ', 9, ' ', ' ', 4, ' ', ' ', 6, ' '], [4, ' ', ' ', 2, ' ', ' ', 5, ' ', 1], [' ', ' ', ' ', 3, ' ', 4, 9, ' ', ' '], [' ', ' ', ' ', ' ', 8, 1, ' ', 7, 4]]
# 30 clues. tics to beat = 8886 (0.053 sec). Andrew Stuart's only took 2970

Escargot = [[1, ' ', ' ', ' ', ' ', 6, 3, ' ', ' '], [' ', 3, ' ', ' ', 1, ' ', ' ', 4, ' '], [' ', ' ', 9, 5, ' ', ' ', ' ', 1, 7], [' ', ' ', 6, 3, ' ', ' ', ' ', ' ', ' '], [' ', 2, ' ', ' ', 8, ' ', ' ', ' ', ' '], [7, ' ', ' ', ' ', ' ', 4, ' ', ' ', ' '], [' ', ' ', 5, 9, ' ', ' ', ' ', ' ', 3], [9, ' ', ' ', ' ', ' ', ' ', 1, ' ', ' '], [' ', 8, ' ', ' ', 2, ' ', ' ', 7, ' ']]
# 24 clues. tics to beat = 351207 (2.108 sec). Andrew Stuart's only took 18755

RiddleOfSho = [[' ', ' ', ' ', ' ', ' ', ' ', 9, ' ', 5], [' ', ' ', 8, 4, ' ', 3, ' ', 1, ' '], [' ', ' ', ' ', ' ', ' ', 1, ' ', ' ', 4], [' ', 3, ' ', ' ', ' ', ' ', 6, ' ', ' '], [' ', ' ', ' ', 2, ' ', 8, ' ', ' ', ' '], [' ', ' ', 4, ' ', ' ', ' ', ' ', 7, ' '], [6, ' ', ' ', 9, ' ', ' ', ' ', ' ', ' '], [' ', 9, ' ', 7, ' ', 6, 2, ' ', ' '], [5, ' ', 1, ' ', ' ', ' ', ' ', ' ', ' ']]
# 22 clues. tics to beat = 197324(1.28 sec). Andrew Stuart's only took 85579

Exocet = [[' ', ' ', 6, ' ', ' ', ' ', ' ', 5, ' '], [' ', ' ', 8, ' ', ' ', 4, ' ', ' ', ' '], [' ', 7, ' ', 1, ' ', ' ', 8, ' ', ' '], [' ', 1, ' ', ' ', 3, ' ', ' ', ' ', ' '], [' ', ' ', 7, 9, ' ', ' ', 6, ' ', ' '], [' ', 9, ' ', ' ', ' ', ' ', ' ', ' ', 2], [7, ' ', ' ', 6, ' ', ' ', 1, ' ', ' '], [' ', ' ', 1, ' ', 2, ' ', ' ', 4, ' '], [' ', ' ', ' ', ' ', ' ', 3, ' ', ' ', 5]]
# 22 clues. tics to beat = 12276442 (74.529 sec). Andrew Stuart's only took 1422145 (his returned 804847 once...???)

ArtoInkala = [[8, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 7, 5, ' ', ' ', ' ', ' ', 9], [' ', 3, ' ', ' ', ' ', ' ', 1, 8, ' '], [' ', 6, ' ', ' ', ' ', 1, ' ', 5, ' '], [' ', ' ', 9, ' ', 4, ' ', ' ', ' ', ' '], [' ', ' ', ' ', 7, 5, ' ', ' ', ' ', ' '], [' ', ' ', 2, ' ', 7, ' ', ' ', ' ', 4], [' ', ' ', ' ', ' ', ' ', 3, 6, 1, ' '], [' ', ' ', ' ', ' ', ' ', ' ', 8, ' ', ' ']]
# 21 clues. tics to beat = 8977537 (52.759 sec). Andrew Stuart's only took 2068781

Easy17 = [[' ', ' ', ' ', 3, ' ', 7, ' ', ' ', 5], [' ', 6, ' ', 2, ' ', ' ', ' ', 4, ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 8, 1], [' ', ' ', ' ', 6, ' ', ' ', 2, ' ', ' '], [4, ' ', ' ', ' ', 5, ' ', ' ', ' ', ' '], [1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', 2, ' ', ' ', ' ', ' ', 3, ' ', ' '], [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 1, ' ', ' ', ' ', ' ']]
# 17 clues. tics to beat = 263585 (1.71 sec). 

Hard17 = [[' ', 8, 1, ' ', ' ', ' ', ' ', 3, ' '], [' ', ' ', ' ', 9, ' ', ' ', 7, ' ', ' '], [2, 5, ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', 5, 1], [9, ' ', ' ', 6, ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [3, ' ', ' ', ' ', ' ', ' ', 2, ' ', ' '], [' ', ' ', ' ', 4, 5, ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 8, 1, ' ', ' ', ' ']]
# 17 clues. tics to beat = 33500180 (229.28 sec).

"""
'...1.5...14....67..8...24...63.7..1.9.......3.1..9.52...72...8..26....35...4.9...'
'3.9...4..2..7.9....87......75..6.23.6..9.4..8.28.5..41......59....1.6..7..6...1.4'
'1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..41.....7..7...3..'
'......6.5...3...9..8...4..1.4..2.97...........31.8..6.9..6...2..1...7...5.4......'
'......7....71.9...68..7..1...1.9.6.....3...2..4......3..8.6.1..5......4......2..5'
'8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..'
'....41....6....2...........32.6.........5..417...........2..3...48......5.1......'
'..2.9.3..8.5......1.........9..6..4........58........1.7....2..3..5........1.....'
"""

