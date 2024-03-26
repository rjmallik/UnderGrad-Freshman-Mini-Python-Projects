class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = " "
    def get_size(self): 
        # optional, return the board size (an instance size)
        return (self.size)
    def get_winner(self):
        # return the winner's sign O or X (an instance winner)
        # case 1: win by columns  
        if (self.board[0] == self.board[1] == self.board[2] != self.sign): 
            self.winner = self.board[0]
        if (self.board[3] == self.board[4] == self.board[5] != self.sign):
            self.winner = self.board[3]
        if (self.board[6] == self.board[7] == self.board[8]!= self.sign):
            self.winner = self.board[6]
        #case 2: win by row
        if (self.board[0] == self.board[3] == self.board[6]!= self.sign):
            self.winner = self.board[0]
        if (self.board[1] == self.board[4] == self.board[7]!= self.sign):
            self.winner = self.board[1]
        if (self.board[2] == self.board[5] == self.board[8]!= self.sign):
            self.winner = self.board[2]
        #case 3: win by diagonal
        if (self.board[0] == self.board[4] == self.board[8]!= self.sign):
            self.winner = self.board[0]
        if (self.board[2] == self.board[4] == self.board[6]!= self.sign):
            self.winner = self.board[2]    

        return (self.winner)
    
    def set(self, cell, sign):
        # mark the cell on the board with the sign X or O
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # you can use a tuple ("A1", "B1",...) to obtain indexes 
        # this implementation is up to you 
        possible_choices = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"]
        location = possible_choices.index(cell)
        self.board[location] = sign
            
    def isempty(self, cell):
        # return True if the cell is empty (not marked with X or O)
        # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
        # return True if the cell is empty (not marked with X or O)
        cells = {"A1":0, "B1":1, "C1":2, "A2":3, "B2":4, "C2":5, "A3":6, "B3":7, "C3":8 }
        place = cells[cell]
        if self.board[place] == " ":
            return (True)
        return False
    def isdone(self):
        check = False
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        
        # case 1: win by columns  
        if (self.board[0] == self.board[1] == self.board[2] != " ") or (self.board[3] == self.board[4] == self.board[5] != " ") or (self.board[6] == self.board[7] == self.board[8] != " "):      
            check = True
        if check == True:
            return check
        
        #case 2: win by row
        if (self.board[0] == self.board[3] == self.board[6] != " ") or (self.board[1] == self.board[4] == self.board[7] != " ") or (self.board[2] == self.board[5] == self.board[8] != " "):
            check = True
        if check == True:
            return check
        
        #case 3: win by diagonal
        if (self.board[0] == self.board[4] == self.board[8] != " ") or (self.board[2] == self.board[4] == self.board[6] != " "):
            check = True
        if check == True:
            return check
        
        #case 4: board is full
        for element in self.board:
            if element == ' ':
                check = False
                break
            else:
                check = True
        return check
    
    def show(self):
        # draw the board
        print("   A   B   C  ") 
        print(" +---+---+---+")
        print("1| {} | {} | {} |".format(self.board[0], self.board[1], self.board[2]))
        print(" +---+---+---+")
        print("2| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
        print(" +---+---+---+")
        print("3| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
        print(" +---+---+---+")