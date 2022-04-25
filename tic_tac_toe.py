class BoardState:
    """
    Class BoardState takes current board state of tic-tac-toe game
    as a list of lists of cells.
    and check if:
    - board is empty
    - X wins
    - O wins
    """
    def __init__(self, board=[
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]):
        self.board = board
        self.check_state()

    def check_state(self):
        board_line = [item for row in self.board for item in row]
        if all(' ' == item for item in board_line):
            print('The game board is empty')
            return
        wins = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for cur_player in ['X', 'O']:
            for row in wins:
                if all(cur_player == board_line[item - 1] for item in row):
                    print(f'{cur_player} won')
                    return
        print('The game is on')
