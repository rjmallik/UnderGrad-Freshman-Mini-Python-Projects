
import numpy as np
from random import choice, shuffle

class Fifteen():
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1, size**2)] + [0])

    def update(self, move):
        if self.is_valid_move(move):
            self.transpose(move, 0)
    
    def transpose(self, i, j):
        i = np.where(self.tiles == i)[0]
        j = np.where(self.tiles == j)[0]
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    def shuffle(self, steps = 100):
        shuffle(self.tiles)        

    def is_valid_move(self, move):
        if (np.where(self.tiles == move)[0] + 1) % 4 == 0:
            if self.tiles[np.where(self.tiles == move)[0]] == 15:
                if self.tiles[np.where(self.tiles == move)[0] - 1] == 0 or self.tiles[np.where(self.tiles == move)[0] - 4] == 0:
                    return True
            elif self.tiles[np.where(self.tiles == move)[0] - 1] == 0 or self.tiles[np.where(self.tiles == move)[0] + 4] == 0:
                return True
        elif np.where(self.tiles == move)[0] == 0 or np.where(self.tiles == move)[0] % 4 == 0:
            if np.where(self.tiles == move)[0] == 12:
                if self.tiles[np.where(self.tiles == move)[0] + 1] == 0:
                    return True
            if self.tiles[np.where(self.tiles == move)[0] + 1] == 0 or self.tiles[np.where(self.tiles == move)[0] + 4] == 0:
                return True
        elif self.tiles[np.where(self.tiles == move)[0] - 1] == 0 or self.tiles[np.where(self.tiles == move)[0] + 1] == 0:
            return True
        return False

    def is_solved(self):
        for i in range(0, 15):
            if self.tiles[i] != i + 1 or (i == 16 and self.tiles[i] != 0):
                return False
        return True

    def draw(self):
        print('+---+---+---+---+')
        print(f'| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} | {self.tiles[3]} |')
        print('+---+---+---+---+')
        print(f'| {self.tiles[4]} | {self.tiles[5]} | {self.tiles[6]} | {self.tiles[7]} |')
        print('+---+---+---+---+')
        print(f'| {self.tiles[8]} | {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |')
        print('+---+---+---+---+')
        print(f'| {self.tiles[12]} | {self.tiles[13]} | {self.tiles[14]} | {self.tiles[15]} |')
        print('+---+---+---+---+')

    def __str__(self):
        string = ""
        for i in range(len(self.tiles)):
            if self.tiles[i] == 0:
                string += "" + " " + " " + " "
            elif self.tiles[i] <= 9:
                string += "" + " " + str(self.tiles[i]) + " "
            else:
                string += str(self.tiles[i]) + " "
            if i % 4 == 3 and i != 1:
                string += "\n"
        return string

if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False

'''Used my own main-method.'''