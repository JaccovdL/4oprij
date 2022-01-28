import random
from re import L

def in_a_row_4_east(ch, r_start, c_start, a, n):
    """Return True if four consecutive chars in direction E
    """
    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])

    if r_start >= rows or r_start <0:
        return False  # buiten de grenzen van de rijen
    #andere grenscontroles...
    if c_start + (n-1) > cols-1 or c_start <0:
        return False  # buiten de grenzen van de kolommen

    # zijn alle gegevenselementen correct?
    for i in range(n):                 # lusindex is i      
        if a[r_start][c_start+i] != ch: # controleer op fouten
            return False                 # fout gevonden; geef False terug
    return True                          # geen fouten gevonden in de lus; geef True terug

def in_a_row_4_south(ch, r_start, c_start, a, n):
    """Return True if four consecutive chars in direction S
    """
    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])   # aantal kolommen is len(a[0])
    if r_start < 0 or r_start + (n-1) > rows - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start > cols - 1:
        return False  # kolom buiten de grenzen

    # zijn alle gegevenselementen correct?
    for i in range(n):                 # lusindex is i      
        if a[r_start+i][c_start] != ch: # controleer op fouten
            return False                 # fout gevonden; geef False terug
    return True    

def in_a_row_4_southeast(ch, r_start, c_start, a,n):
    """Return True if three consecutive chars in direction SE
    """
    rows = len(a)      # aantal rijen is len(a)
    cols = len(a[0])
    if r_start < 0 or r_start + (n-1) > rows - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > cols - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start+i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug

def in_a_row_4_northeast(ch, r_start, c_start, a,n):
    """Return True if three consecutive chars in direction SE
    """
    rows = len(a)
    cols = len(a[0])
    if r_start - (n-1) < 0 or r_start > rows - 1:
        return False  # rij buiten de grenzen
    if c_start < 0 or c_start + (n-1) > cols - 1:
        return False  # kolom buiten de grenzen
    # lus over elke _offset_ i van de locatie
    for i in range(n):
        if a[r_start-i][c_start+i] != ch:  # klopt niet!
            return False
    return True  # alle offsets kloppen, dus we geven True terug

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We hoeven niets terug te geven vanuit een constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # de string om terug te geven
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord

        # hier moeten de nummers nog onder gezet worden
        s += '\n'
        for col in range(0, self.width):
            s += ' ' + str(col%10)

        return s       # het bord is compleet, geef het terug

    def add_move(self, col, ox):
        """Add a move of (chars 'O' or 'X') your choice on the board
        Choice selected by choosing the specific col
        """
        for row in range(self.height-1, -1, -1):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                break

    def clear(self):
        """"Clear bord from OX
        """
        self.data = [[' ']*self.width for row in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.

        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.

        move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'
        
    def allows_move(self, col):
        """Check if given move is possible
        1. Given col is a correct col for board
        2. Space in given col
        Return True if possible move
        """
        if col > self.width-1 or col < 0:
            return False
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                return False
            else:
                return True
    
    def is_full(self):
        """Return True if board is full
        """
        for col in range(0, self.width):
            return self.allows_move(col) == False
    
    def del_move(self, col):
        """Delete top value (X/O) of column
        """
        for row in range(0, self.height):
            if self.data[row][col] in 'XO':
                self.data[row][col] = ' '
                break

    #def wins_for(self, row, col, ox):
    def wins_for(self, ox):
        """ wins_for code """
        # dit is pseudocode
        for row in range(0, self.height):
            for col in range(0, self.width):
                if in_a_row_4_east(ox, row, col, self.data, 4) == True or in_a_row_4_northeast(ox, row, col, self.data, 4) == True or\
                    in_a_row_4_south(ox, row, col, self.data, 4) == True or in_a_row_4_southeast(ox, row, col, self.data, 4) == True:
                    return True
        return False
                # controleer of je in één van de vier richtingen wint
    
    def host_game(self):
        """Create a running game"""

        print('Welkom bij Vier op een rij! \n')
        print(b)
        while True:
            col = -1
            while not self.allows_move(col):
                col = int(input('Keuze van X: '))
                print()
            self.add_move(col, 'X')
            if self.wins_for('X') == True:
                print('X wint -- Gefeliciteerd!')
                print(b)
                break
            print(b)
            print()
            col = -1
            while not self.allows_move(col):
                col = int(input('Keuze van O: '))
                print()
            self.add_move(col, 'O')
            if self.wins_for('O') == True:
                print('O wint -- Gefeliciteerd!\n')
                print(b)
                break
            print(b)
            print()

class Player:
    """An AI player for Connect Four."""

    def __init__(self, ox, tbt, ply):
        """Construct a player for a given checker, tie-breaking type,
           and ply."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        """Create a string represenation of the player."""
        s = "Player: ox = " + self.ox + ", "
        s += "tbt = " + self.tbt + ", "
        s += "ply = " + str(self.ply)
        return s

    def opp_ch(self):
        """Give the opposite char of players use"""
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'
    
    def score_board(self, b):
        """Return score (float) of given input b"""
        if b.wins_for(self.ox) == True:
            return 100.0
        elif b.wins_for(self.opp_ch()) == True:
            return 0.0
        elif b.is_full() == True:
            return -1.0
        else:
            return 50.0

    def tiebreak_move(self, scores):
        """Scores will be a list of floiting-points
        If only one highest number in list return column of this score
        Otherwise choose the colomn of highest score depending on strategy"""
        options = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                options += [i]
        if len(options) == 1:
            return options[0]
        elif self.tbt == 'LEFT':
            return options[0]
        elif self.tbt == 'RIGHT':
            return options[-1]
        elif self.tbt == 'RANDOM':
            return random.choice(options)
        else:
            return 'FOUT!'

    def scores_for(self, b):
        """Return list of index values with best possible moves (after self.ply amount of moves)"""
        scores = [50.0] *b.width

        # if b.allows_move(scores[0]) == False:
        #     scores[0] = -1.0
        # return p.scores_for(b, scores[1:])
        
        for i in range(len(scores)):
            if b.allows_move(i) == False:
                scores[i] = -1.0
            elif b.wins_for(self.ox):
                scores[i] = 100.0
            elif b.wins_for(self.opp_ch()):
                scores[i] = 0.0
        print(b.wins_for(p.ox))
        print(p.ox)
        print(scores)
        




p = Player('X', 'LEFT', 2)
assert repr(p) == 'Player: ox = X, tbt = LEFT, ply = 2'
p = Player('O', 'RANDOM', 0)
assert repr(p) == 'Player: ox = O, tbt = RANDOM, ply = 0'

p = Player('X', 'LEFT', 3)
assert p.opp_ch() == 'O'
assert Player('O', 'LEFT', 0).opp_ch() == 'X'

b = Board(7, 6)
b.set_board('01020305')
#print(b)
p = Player('X', 'LEFT', 0)
assert p.score_board(b) == 100.0
assert Player('O', 'LEFT', 0).score_board(b) == 0.0
assert Player('O', 'LEFT', 0).score_board(Board(7, 6)) == 50.0
b = Board(7, 6)
b.set_board('000000111111222223423333344444555555666666')
#print(b)
assert Player('X', 'LEFT', 0).score_board(b) == -1.0
assert Player('O', 'LEFT', 0).score_board(b) == -1.0
assert Player('X', 'LEFT', 0).score_board(Board(7, 6)) == 50.0

scores = [0, 0, 50, 0, 0, 0, 0]
p = Player('X', 'LEFT', 1)
assert p.tiebreak_move(scores) == 2
scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
assert p.tiebreak_move(scores) == 2
assert p2.tiebreak_move(scores) == 5
scores = [0,50,50,50,50,0,50]
p = Player('X', 'LEFT', 5)
p2 = Player('X', 'RANDOM', 1)
assert p.tiebreak_move(scores) == 1
assert p2.tiebreak_move(scores) == 1 or 2 or 3 or 4 or 5 or 7

b = Board(7, 6)
b.set_board('11111112323232')

p.scores_for(b)