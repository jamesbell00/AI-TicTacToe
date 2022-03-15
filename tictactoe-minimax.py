class TicTacToe:
    def __init__(self):
        self.grid = [['_', '_', '_'],
                     ['_', '_', '_'],
                     ['_', '_', '_']]

        self.player_turn = 'X'

        # iteration counts
        self.c = 0
        self.counter = 0;


    def draw(self):
        print("")

        for i in range(0, 3):
            for j in range(0, 3):
                print("{}|".format(self.grid[i][j]), end="")
            print("")
        print("")

    def valid_coordinates(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.grid[px][py] != '_':
            return False
        else:
            return True

    def game_over(self):
        # horizontal win: X player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self.grid[i] == ['X', 'X', 'X']):
                return 'X'

        # horizontal win: O player wins when ['X', 'X', 'X'] in rows 0 to 2

        for i in range(0, 3):
            if (self.grid[i] == ['O', 'O', 'O']):
                return 'O'

        # vertical win: for i=0 to 2 grid positions [0][i], [1][i], and [2][i] are not '_' and have the same value

        for i in range(0, 3):
            if (self.grid[0][i] != '_' and self.grid[0][i] == self.grid[1][i] and self.grid[1][i] == self.grid[2][i]):
                return self.grid[0][i]

        # main diagonal win: grid positions [0][0], [1][1], and [2][2] have the same value

        if (self.grid[0][0] != '_' and self.grid[0][0] == self.grid[1][1] and self.grid[0][0] == self.grid[2][2]):
            return self.grid[0][0]

        # second diagonal win: grid positions [0][2], [1][1], and [2][0] have the same value

        if (self.grid[0][2] != '_' and self.grid[0][2] == self.grid[1][1] and self.grid[0][2] == self.grid[2][0]):
            return self.grid[0][2]

        # if the grid is full is a forced draw

        for i in range(0, 3):
            for j in range(0, 3):
                # if there is an empty position '_', the game is not over

                if (self.grid[i][j] == '_'):
                    return None

        return '_'

    def play(self):
        while True:
            self.draw()



            winner = self.game_over()

            # if the game is over

            if winner != None:
                if winner == 'X':
                    print("X player wins!")
                elif winner == 'O':
                    print("O player wins!")
                elif winner == '_':
                    print("The game ends with a forced draw!")

                return

            # if it is the X player turn

            if self.player_turn == 'X':
                while True:
                    print("Player X enter coordinates x y: ", end="")

                    px, py = map(int, input().split())

                    if self.valid_coordinates(px, py):
                        self.grid[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print("Coordinates are not valid! Play again")

            # if it is the O player turn

            else:
                while True:
                    print("Player O enter coordinates x y: ", end="")

                    val, px, py = self.max_minimax_tic(-2, 2)
                    print("\nRuns: ", self.c)
                    self.c = 0

                    if self.valid_coordinates(px, py):
                        self.grid[px][py] = 'O'
                        self.player_turn = 'X'
                        break
                    else:
                        print("Coordinates are not valid! Play again")


    def min_minimax_tic(self, alpha, beta):
        self.c += 1
        self.counter += 1
        # the AI player (O) is a max player, possible values for the max
        # player are -1: loss, 0: draw, +1: win, its initial value is -2
        min_value = +2
        # max_px, max_py are the coordinates of the optimal play
        min_px = -1
        min_py = -1

        winner = self.game_over()

        # if the game is over, return -1, 0, +1
        if winner == 'X':
            return (-1, 0, 0)  # X is a Min player, its best play has value -1
        elif winner == 'O':
            return (1, 0, 0)  # O is a Max player, its best play has value +1
        elif winner == '_':
            return (0, 0, 0)  # the game ends with a draw

        # if the game is not over, evaluate all possible plays
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                # if coordinate [i][j] is empty, evaluate the play for the O player
                if self.grid[i][j] == '_':
                    self.grid[i][j] = 'X'
                    # minimax_min returns a tuple with the value of a final state
                    (value, min_i, min_j) = self.max_minimax_tic(alpha, beta)
                    # max_value is updated when a greater value is found
                    if value < min_value:
                        min_value = value
                        min_px = i
                        min_py = j

                        # self.beta = min(self.beta, min_value)

                    # when the recursive calls for the [i][j] play terminate,
                    # the value of [i][j] is restored
                    self.grid[i][j] = '_'

                    if min_value <= alpha:
                        return (min_value, min_px, min_py)

                    if min_value < beta:
                        beta = min_value
        # minimax_max returns the value and the coordinates of the optimal play
        return (min_value, min_px, min_py)

    def max_minimax_tic(self, alpha, beta):
        self.c += 1
        self.counter += 1
        # the AI player (O) is a max player, possible values for the max
        # player are -1: loss, 0: draw, +1: win, its initial value is -2
        max_value = -2
        # max_px, max_py are the coordinates of the optimal play
        max_px = -1
        max_py = -1
        winner = self.game_over()

        # if the game is over, return -1, 0, +1
        if winner == 'X':
            return (-1, 0, 0)  # X is a Min player, its best play has value -1

        elif winner == 'O':
            return (1, 0, 0)  # O is a Max player, its best play has value +1
        elif winner == '_':
            return (0, 0, 0)  # the game ends with a draw

        # if the game is not over, evaluate all possible plays
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                # if coordinate [i][j] is empty, evaluate the play for the O player
                if self.grid[i][j] == '_':
                    self.grid[i][j] = 'O'
                    # minimax_min returns a tuple with the value of a final state
                    (value, min_i, min_j) = self.min_minimax_tic(alpha, beta)
                    # max_value is updated when a greater value is found
                    if value > max_value:
                        max_value = value
                        max_px = i
                        max_py = j

                        # self.alpha = max(self.alpha, max_value)

                    # when the recursive calls for the [i][j] play terminate,
                    # the value of [i][j] is restored
                    self.grid[i][j] = '_'
                    if max_value >= beta:
                        return (max_value, max_px, max_py)

                    if max_value > alpha:
                        alpha = max_value
        # minimax_max returns the value and the coordinates of the optimal play
        return (max_value, max_px, max_py)


if __name__ == "__main__":
    g = TicTacToe()
    g.play()

    print("total runs: ", g.counter)
