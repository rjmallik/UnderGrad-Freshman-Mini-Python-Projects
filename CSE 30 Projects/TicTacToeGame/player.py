from random import choice
class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X
    def get_sign(self):
        # return an instance sign
        return self.sign

    def get_name(self):
        # return an instance name
        return self.name
    
    def choose(self, board):
        # prompt the user to choose a cell
        # if the user enters a valid string and the cell on the board is empty, update the board
        # otherwise print a message that the input is wrong and rewrite the prompt
        # use the methods board.isempty(cell), and board.set(cell, sign)
        possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        while True: 
            user_cell = input(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n").upper()
            if user_cell in possible_choices :
                if board.isempty(user_cell):
                    board.set(user_cell, self.sign)
                    break
                else:
                    print("You did not choose correctly.")
                    continue
            else:
                print("You did not choose correctly.")
                continue
            
#create an AI to play the game as Bob that uses random choices
class AI(Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
    def choose(self, board):
        possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        #update possible choices so that only non-empty spaces can be chosen by the AI
        newChoices = [x for x in possible_choices if board.isempty(x)]
        aiChoice = choice(newChoices)
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", aiChoice)
        board.set(aiChoice, self.sign)
        
#create a subclass of AI that uses a min-max algorithm based on recursion 
class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)
        #get opponent sign
        if self.sign == "X":
            self.opponent_sign = "O"
        else:
            self.opponent_sign = "X"
        
            
    #choose the move
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end= " ")
        aiChoice = MiniMax.minimax(self, board, True, True)
        print(aiChoice)
        board.set(aiChoice, self.sign)
        
        
    #calculate what the next best move is using recursion/minimax algorithm
    def minimax(self, board, self_player, start):
        # check base case
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1
            if board.get_winner() == " ":
                return 0
            if board.get_winner() == self.opponent_sign:
                return -1
            
        minimumScore = 1000
        maximumScore = -1000

        #iterate through all possible choices
        possible_choices = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        if self_player:
            for possibility in possible_choices: 
                if board.isempty(possibility):
                    board.set(possibility, self.sign)
                    score = MiniMax.minimax(self, board, False, False)
                    if score > maximumScore:
                        maximumScore = score
                        action = possibility
                    board.set(possibility, " ")
        if not self_player:
            for possibility in possible_choices: 
                if board.isempty(possibility):
                    board.set(possibility, self.opponent_sign)
                    score = MiniMax.minimax(self, board, True, False)
                    if score < minimumScore:
                        minimumScore = score
                        action = possibility
                    board.set(possibility, " ")
                    
        if start:
            return action
        elif self_player:
            return maximumScore
        else:
            return minimumScore
