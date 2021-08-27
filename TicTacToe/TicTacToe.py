class TicTacToe():
    def __init__(self) -> None:
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'
        self.winner = None
        self.game_over = False
        self.turn = 0
        self.game_over = False
        self.winner = None
        self.game_over = False
        self.turn = 0
                
    def draw_board(self):
        print('\n  {} | {} | {}'.format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print('  {} | {} | {}'.format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print('  {} | {} | {}\n'.format(self.board[2][0], self.board[2][1], self.board[2][2]))
        
    def check_win(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != ' ':
            self.game_over = True
            self.winner = self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2] != ' ':
            self.game_over = True
            self.winner = self.board[1][0]
        if self.board[2][0] == self.board[2][1] == self.board[2][2] != ' ':
            self.game_over = True
            self.winner = self.board[2][0]
        if self.board[0][0] == self.board[1][0] == self.board[2][0] != ' ':
            self.game_over = True
            self.winner = self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1] != ' ':
            self.game_over = True
            self.winner = self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2] != ' ':
            self.game_over = True
            self.winner = self.board[0][2]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.game_over = True
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.game_over = True
            self.winner = self.board[0][2]
    def check_tie(self):
        if self.turn == 9:
            self.game_over = True
            self.winner = 'Tie'
    def play_game(self):
        self.draw_board()
        while not self.game_over:
            self.turn += 1
            if self.turn % 2 == 1:
                self.player = 'X'
            else:
                self.player = 'O'
            self.get_move()
            self.draw_board()
            self.check_win()
            self.check_tie()
            if self.game_over:
                print('Game Over!')
                print('The winner is {}'.format(self.winner))
                self.draw_board()
                break
    def get_move(self):
        move = input('Player {}, please enter your move: '.format(self.player))
        if move == '1':
            self.board[0][0] = self.player
        elif move == '2':
            self.board[0][1] = self.player
        elif move == '3':
            self.board[0][2] = self.player
        elif move == '4':
            self.board[1][0] = self.player
        elif move == '5':
            self.board[1][1] = self.player
        elif move == '6':
            self.board[1][2] = self.player
        elif move == '7':
            self.board[2][0] = self.player
        elif move == '8':
            self.board[2][1] = self.player
        elif move == '9':
            self.board[2][2] = self.player
        else:
            print('Invalid move')
            self.get_move()
TicTacToe().play_game()
