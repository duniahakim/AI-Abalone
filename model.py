
from copy import deepcopy
from collections import defaultdict
import time


class AbaloneGame(object):
    def __init__(self, max_num_rounds, boardSize = 4):
        self.max_num_rounds = max_num_rounds # maximum number of allowed rounds in game (game ends if exceeded)
        self.black = 1 # integer to represent a black marble
        self.white = -1 #integer to represent a white marblee
        self.empty = 0 #integer to represent an empty space on board
        self.directions = [(+1, -1, 0), (+1,0,-1), (0, +1, -1), (-1, +1, 0), (-1, 0, +1), (0, -1, +1)] # possible directions from every space on board (x,y,z)
        self.boardSize = boardSize
        if boardSize == 4:
            self.numToWin = 6
            self.numMarblesPerPlayer = 14
            self.numRows = 9
            self.lowerBound = -4
            self.upperBound = 4
        if boardSize == 3:
            self.numToWin = 5
            self.numMarblesPerPlayer = 11
            self.numRows = 7
            self.lowerBound = -3
            self.upperBound = 3
        if boardSize == 2:
            self.numToWin = 2
            self.numMarblesPerPlayer = 5
            self.numRows = 5
            self.lowerBound = -2
            self.upperBound = 2


    def features(self, state):
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state

        black_on_grid = self.numMarblesPerPlayer-num_black_Off_grid
        white_on_grid = self.numMarblesPerPlayer-num_white_Off_grid
        num_black_on_edge = 0
        black_average_pos = 0
        num_white_on_edge = 0
        white_average_pos = 0
        black_coherence = 0
        white_coherence = 0
        BONUS_FOR_3_CONSECUTIVE = 0
        black_break = 0
        white_break = 0

        for pos in dict_pos:
            if dict_pos[pos] == self.black:
                black_average_pos += sum([abs(i) for i in pos])
                if self.upperBound in pos or self.lowerBound in pos:
                    num_black_on_edge += 1

                for direction in self.directions:
                    nextPos = self.addition(pos, direction)
                    if nextPos not in dict_pos:
                        continue

                    #coherence
                    if dict_pos[nextPos] == self.black:
                        black_coherence += 1
                        nextNextPos = self.addition(nextPos, direction)
                        if nextNextPos in dict_pos and dict_pos[nextNextPos] == self.black:
                            black_coherence += BONUS_FOR_3_CONSECUTIVE

                    #formation break
                    elif dict_pos[nextPos] == self.white:
                        black_break += 1
            elif dict_pos[pos] == self.white:
                white_average_pos += sum([abs(i) for i in pos])
                if self.upperBound in pos or self.lowerBound in pos:
                    num_white_on_edge += 1

                    #single marble capture danger


                for direction in self.directions:
                    nextPos = self.addition(pos, direction)
                    if nextPos not in dict_pos:
                        continue

                    #coherence
                    if dict_pos[nextPos] == self.white:
                        white_coherence += 1
                        nextNextPos = self.addition(nextPos, direction)
                        if nextNextPos in dict_pos and dict_pos[nextNextPos] == self.white:
                            white_coherence += BONUS_FOR_3_CONSECUTIVE

                    #formation break
                    elif dict_pos[nextPos] == self.black:
                        white_break += 1


        black_average_pos /= float(black_on_grid)
        white_average_pos /= float(white_on_grid)


        black_coherence /= float(black_on_grid)
        white_coherence /= float(white_on_grid)

        black_break /= float(black_on_grid)
        white_break /= float(white_on_grid)

        if player == self.white:
            num_black_Off_grid = num_black_Off_grid ** 2
            num_white_Off_grid = num_white_Off_grid ** 2

        f = {
            "num_black_Off_grid": num_black_Off_grid ,
            'num_white_Off_grid': num_white_Off_grid,
            'num_black_on_edge': num_black_on_edge,
            'num_white_on_edge': num_white_on_edge,
            'black_average_pos': black_average_pos,
            'white_average_pos': white_average_pos,
            'black_coherence': black_coherence,
            'white_coherence': white_coherence,
            'black_break': black_break,
            'white_break': white_break
        }


        return f

    def eval(self, state, w):
        features = self.features(state)
        evaluation = 0.0
        for key in w:
            if key in features:
                evaluation += w[key] * features[key]
        return evaluation

    def startState(self):
        num_round = 0
        player = self.black
        num_black_Off_grid = 0
        num_white_Off_grid = 0

        # a dictionary with position of space on board as key (a tuple (x,y,z) representing the position on each of the x, y, and z-axieses respectively) and with integer representing the occupation of that space (1 for black (self.black), -1 for white (self.white), and 0 for empty (self.empty))
        dict_pos = {}
        if self.boardSize == 4:
            for x in range(self.lowerBound, self.upperBound + 1):
                for y in range(self.lowerBound, self.upperBound + 1):
                    z = 0 - x - y
                    if z not in range(self.lowerBound, self.upperBound + 1):
                        continue
                    if (z == -4 or z == -3) or (z == -2 and y in range(0, 3)):
                        dict_pos[(x,y,z)] = self.white
                    elif (z == 4 or z == 3) or (z == 2 and y in range(-2, 1)):
                        dict_pos[(x,y,z)] = self.black
                    else:
                        dict_pos[(x, y, z)] = self.empty
            return (dict_pos, num_black_Off_grid, num_white_Off_grid, player, num_round)
        elif self.boardSize == 3:
            for x in range(-3, 4):
                for y in range(-3, 4):
                    z = 0 - x - y
                    if z not in range(-3, 4):
                        continue
                    if (z == -3 or z == -2) or (z == -1 and y in range(0, 2)):
                        dict_pos[(x,y,z)] = self.white
                    elif (z == 3 or z == 2) or (z == 1 and y in range(-1, 1)):
                        dict_pos[(x,y,z)] = self.black
                    else:
                        dict_pos[(x, y, z)] = self.empty
            return (dict_pos, num_black_Off_grid, num_white_Off_grid, player, num_round)
        elif self.boardSize == 2:
            for x in range(-2, 3):
                for y in range(-2, 3):
                    z = 0 - x - y
                    if z not in range(-2, 3):
                        continue
                    if z == -2 or (z == -1 and y in range(0, 2)):
                        dict_pos[(x,y,z)] = self.white
                    elif z == 2  or (z == 1 and y in range(-1, 1)):
                        dict_pos[(x,y,z)] = self.black
                    else:
                        dict_pos[(x, y, z)] = self.empty
            return (dict_pos, num_black_Off_grid, num_white_Off_grid, player, num_round)

    def player(self, state):
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, num_round = state
        return player

    def isEnd(self, state):
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, num_round = state
        if num_white_Off_grid == self.numToWin or num_black_Off_grid == self.numToWin or num_round > self.max_num_rounds:
            return True
        return False

    def actions(self, state):
        possible_actions = []
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        for key, val in dict_pos.items():
            if val == player:
                for direction in self.directions:
                    possible_actions.append((key, direction))
        return possible_actions

    def addition(self, marble, direction, scale = 1):
        xm, ym, zm = marble
        xd, yd, zd = direction
        return (xm + scale * xd, ym + scale * yd, zm + scale * zd)

    def push(self, state, marble_pos, direction):
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        pushOff = False
        numOwn = 1 # number of current player's marbles in attempted push
        numOpp = 0 # number of opponent's marbles in attempted push


        currPos = marble_pos
        #counting marbles on the player's side
        while(True):
            if numOwn > 3:
                return None
            nextPos = self.addition(currPos, direction)
            if nextPos in dict_pos and dict_pos[nextPos] == player:
                numOwn += 1
                currPos = nextPos
            else:
                break

        #counting marbles on the opponent's side
        while(True):
            nextPos = self.addition(currPos, direction)
            if numOpp >= numOwn:
                return None
            if nextPos not in dict_pos:
                currPos = nextPos
                pushOff = True
                break
                #encountered the boundary

            if dict_pos[nextPos] == player:
                return None
            elif dict_pos[nextPos] == self.empty:
                currPos = nextPos
                break
            else:
                numOpp += 1
                currPos = nextPos

        newDict = deepcopy(dict_pos)
        new_num_black_Off_grid = num_black_Off_grid
        new_num_white_Off_grid = num_white_Off_grid
        new_numRound = numRound + 1

        while (numOpp != 0):
           if pushOff:
               if player == self.black:
                   new_num_white_Off_grid += 1
               elif player == self.white:
                   new_num_black_Off_grid += 1
               pushOff = False
           else:
               newDict[currPos] = -player
           currPos = self.addition(currPos, direction, scale = -1)
           numOpp -= 1

        while (numOwn != 0):
           if pushOff:
               if player == self.black:
                   new_num_black_Off_grid += 1
               elif player == self.white:
                   new_num_white_Off_grid += 1
               pushOff = False
           else:
               newDict[currPos] = player
           currPos = self.addition(currPos, direction, scale = -1)
           numOwn -= 1

        newDict[currPos] = self.empty

        return (newDict, new_num_black_Off_grid, new_num_white_Off_grid, -player, new_numRound)

    def succ(self, state, action):

        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        marble_pos, direction = action
        newState = self.push(state, marble_pos, direction)
        if newState is None:
            return None
        _, new_black_Off, new_white_Off, _, _ = newState

        if self.isEnd(newState):
            if new_black_Off > new_white_Off:
                return newState
            elif new_black_Off < new_white_Off:
                return newState

        return newState

    def utility(self, state):
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        # if num_black_Off_grid >= 6:
        #     return -1 * float('inf')
        # if num_white_Off_grid >= 6:
        #     return float('inf')
        return num_white_Off_grid**2 * 20 - num_black_Off_grid**2 * 20

    def visualization(self, d):
        print(len(d))

    	def getValue(i):
    		if i < 0:
    			return "W"
    		elif i > 0:
    			return "B"
    		else:
    			return "O"

    	rows = []
    	for z in range(self.lowerBound, self.upperBound + 1):
    		row = []
    		for y in range(-self.lowerBound, -self.upperBound -1, -1):
    			x = 0-z-y
    			if x in range(self.lowerBound, self.upperBound + 1):
    				row.append(getValue(d[(x,y,z)]))
    		rows.append(row)
    	for row in rows:
    		result = ""

    		makeup = self.numRows - len(row)
    		for i in range(makeup):
    			result += " "
    		result += " ".join(row)
    		print result
