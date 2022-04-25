from tic_tac_toe import BoardState

#empty board
a = BoardState([
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
])

# X won

b = BoardState([
    [' ', 'O', 'O'],
    ['X', 'X', 'X'],
    [' ', 'O', ' ']
])

c = BoardState([
    ['X', 'O', 'O'],
    ['X', ' ', 'X'],
    ['X', 'O', ' ']
])

# O won

d = BoardState([
    ['O', 'O', 'O'],
    ['X', ' ', 'X'],
    ['X', 'O', ' ']
])

e = BoardState([
    ['X', 'X', 'O'],
    ['X', 'O', 'X'],
    ['O', 'O', ' ']
])

# Game isn't ended

f = BoardState([
    ['X', 'O', 'O'],
    ['O', ' ', 'X'],
    ['X', 'O', ' ']
])

g = BoardState([
    ['X', 'O', 'O'],
    ['O', 'X', 'X'],
    ['X', 'O', ' ']
])
