import model
import random
import time
import math
from tkinter import *
import tkinter as tk
# import tkMessageBox

class getReturn:
    def __init__(self):
        self.direction = ""
        self.value = ""


def display(game, pos, rtrn):
    top = tk.Tk()
    top.configure(background='#8A4B35')

    def helloCallBack(rtrn, xyz):
        rtrn.value = xyz


    top.geometry("800x400")

    def sel(direction):
        rtrn.direction = direction
        for widget in top.winfo_children():
            widget.destroy()
        top.destroy()

    var = IntVar()
    R1 = Radiobutton(top, text="Right", variable=var, command=lambda: sel(game.directions[0]))
    R1.pack(anchor = W)
    R2 = Radiobutton(top, text="Right Up", variable=var, command=lambda: sel(game.directions[1]))
    R2.pack(anchor=W)
    R3 = Radiobutton(top, text="Left Up", variable=var, command=lambda: sel(game.directions[2]))
    R3.pack(anchor=W)
    R4 = Radiobutton(top, text="Left", variable=var, command=lambda: sel(game.directions[3]))
    R4.pack(anchor=W)
    R5 = Radiobutton(top, text="Left Down", variable=var, command=lambda: sel(game.directions[4]))
    R5.pack(anchor=W)
    R6 = Radiobutton(top, text="Right Down", variable=var, command=lambda: sel(game.directions[5]))
    R6.pack(anchor=W)

    space = 32
    maxcoord = game.boardSize

    buttons = {}
    rows = []
    for z in range(-maxcoord, maxcoord + 1):
        row = []
        for y in range(maxcoord, -maxcoord - 1, -1):
            x = 0 - z - y
            if x in range(- maxcoord, maxcoord + 1):
                row.append((x, y, z))
                text = "B" if pos[(x,y,z)] == game.black else ("W" if pos[(x,y,z)] == game.white else "")
                position = (x, y, z)
                buttons[(x, y, z)] = tk.Button(top, command=lambda p = position: helloCallBack(rtrn, p), text = text)
                buttons[(x, y, z)].pack()
        rows.append(row)

    for row in rows:
        makeup = maxcoord * 2 + 1 - len(row)
        for i in range(len(row)):
            x, y, z = row[i]
            buttons[row[i]].place(bordermode=OUTSIDE, height=space, width=space,
                                  x=space * 6 + makeup * (space + 2) / 2 + (space + 2) * i,
                                  y=space * 6 + (space + 2) * z)
    top.mainloop()


def humanPolicy(game, state, side = 1):
    while True:
        rtrn = getReturn()
        display(game, state[0], rtrn)
        marble = rtrn.value
        direction = rtrn.direction
        if (marble, direction) in game.actions(state) and game.succ(state, (marble, direction)):
            return (marble, direction)


def normalize(w):
    denominator = 0.0
    for val in w.values():
        denominator += abs(val) #**2
    # denominator = math.sqrt(denominator)

    for key, val in w.items():
        w[key] = val / denominator

    return w


def getBlackWeights():
    w = {'num_black_Off_grid': -10.0, 'num_white_Off_grid': 12.0, 'num_black_on_edge': -1.4220548966813016, 'num_white_on_edge': 1.0906714795992967, 'black_average_pos': -1.4156226804858798, 'white_average_pos': 1.3894678700263614, 'black_coherence': 1.7941345394011496, 'white_coherence': -0.8928301228450835, 'black_break': 1.849963784226139, 'white_break': -0.15003621577402654}

    # w = {'num_white_Off_grid': 12.619348456190396, 'num_white_on_edge': 3.1488994429705066, 'black_break': 2.857962452598955, 'num_black_Off_grid': -10.0, 'black_coherence': 2.8637717236477016, 'white_coherence': -0.4740966727316621, 'white_break': 1.042129028946902, 'white_average_pos': 3.918577000282171, 'num_black_on_edge': 0.33348825286889183, 'black_average_pos': 0.5794191606665251}
    w = normalize(w)
    return w

def getWhiteWeights():
    # w = {}
    # w['num_black_Off_grid'] = 100
    # w['num_white_Off_grid'] = -100
    # w['num_black_on_edge'] = 100
    # w['num_white_on_edge'] = -100
    # w['black_average_pos'] = 100
    # w['white_average_pos'] = -100
    # w['black_coherence'] = -100
    # w['white_coherence'] = 100
    # w['black_break'] = -100
    # w['white_break'] = 100
    w = {'num_black_Off_grid': 11.622712460338024, 'num_white_Off_grid': -9.476337597924067, 'num_black_on_edge': 1.3089819093532071, 'num_white_on_edge': -0.18712317451057772, 'black_average_pos': 2.0062569948903897, 'white_average_pos': -0.061458291448646035, 'black_coherence': -0.006068921392942536, 'white_coherence': 1.85159872562587, 'black_break': 0.5038203759354308, 'white_break': 2.7659631373543543}

    # w = {'num_black_Off_grid': 12.0, 'num_white_Off_grid': -9.838700530701312, 'num_black_on_edge': 2.0422668564407758, 'num_white_on_edge': -0.6614323172236901, 'black_average_pos': 2.272661061466584, 'white_average_pos': -0.5059960126085488, 'black_coherence': -0.5666191005121458, 'white_coherence': 2.1590475367578774, 'black_break': 0.19654327711591962, 'white_break': 2.243561057001353}
    w = normalize(w)
    return w


def getDefaultWeights():
    w = {}
    w['num_black_Off_grid'] = -10.0
    w['num_white_Off_grid'] = 10.0
    w['num_black_on_edge'] = -1.0011062940155924
    w['num_white_on_edge'] =  0.9983901205525182
    w['black_average_pos'] = 0.9998278853441056
    w['white_average_pos'] = -1.0002396205464497
    w['black_coherence'] = 1.0000753562129148
    w['white_coherence'] = -0.9999787822015421
    w['black_break'] = -1.0
    w['white_break'] = 1.0

    w = normalize(w)
    return w

def getDepth(game, state):
    features = game.features(state)
    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
    if player == game.black:
        if features['black_break'] == 0:
            return 1
        else:
            return 2
    if player == game.white:
        if features['white_break'] == 0:
            return 1
        else:
            return 2


def getOrderedSuccStates(game, state, byIncreasingOrder):
    possibilities = []
    w = getDefaultWeights()
    for action in game.actions(state):
        succGameState = game.succ(state, action)
        if succGameState is None:
            continue
        evaluation = game.eval(succGameState, w)
        possibilities.append((succGameState, evaluation))
    sortedPossibilities =  sorted(possibilities, key=lambda x: x[1], reverse = byIncreasingOrder)
    return list(zip(*sortedPossibilities))[0]

def HeuristicAgent(game, state, side = 1):
    choices = []
    for action in game.actions(state):
        succGameState = game.succ(state, action)
        if succGameState is None:
            continue
        if side == game.black:
            w = getBlackWeights()
        elif side == game.white:
            w = getWhiteWeights()
        evaluation = (game.eval(succGameState, w), action)
        choices.append(evaluation)
    value, action = max(choices)
    return action

def AlphaBeta(game, state, side = 1):

    def recurse(game, state, alpha, beta, d = 1, side = 1):
        if game.isEnd(state):
            return side * game.utility(state)
        w_black = getBlackWeights()
        w_white = getWhiteWeights()
        if d == 0:
            if side == game.black:
                evaluation = game.eval(state, w_black)
                return evaluation
            else:
                evaluation = game.eval(state, w_white)
                return evaluation
        if game.player(state) == side:
            newAlpha = alpha
            choices = []
            orderedSuccStatesForMax = getOrderedSuccStates(game, state, False)
            for succGameState in orderedSuccStatesForMax:

            # for action in game.actions(state):
                # succGameState = game.succ(state, action)
                # if succGameState is None:
                #     continue
                succVal = recurse(game, succGameState, newAlpha, beta, d = d, side = side)
                if succVal > 0.5:
                    return succVal
                if beta is not None and succVal > beta:
                    return succVal
                if newAlpha is None or succVal > newAlpha:
                    newAlpha = succVal
                choices.append(succVal)

            sortedChoices = sorted(choices)
            return random.choice(sortedChoices[-2:])
            # return max(choices)
        else:
            newBeta = beta
            choices = []
            orderedSuccStatesForMin = getOrderedSuccStates(game, state, True)
            for succGameState in orderedSuccStatesForMin:
            # for action in game.actions(state):
                # succGameState = game.succ(state, action)
                # if succGameState is None:
                #     continue
                succVal = recurse(game, succGameState, alpha, newBeta, d = d - 1, side = side)
                if succVal < 0.3:
                    return succVal
                if alpha is not None and succVal < alpha:
                    return succVal
                if newBeta is None or succVal < newBeta:
                    newBeta = succVal
                choices.append(succVal)
            sortedChoices = sorted(choices)
            return random.choice(sortedChoices[:2])
            # return min(choices)

    alpha = None
    beta = None
    choices = []
    d = getDepth(game, state)
    print ("depth: ", d)
    for action in game.actions(state):
        succGameState = game.succ(state, action)
        if succGameState is None:
            continue
        succValAction = (recurse(game, succGameState, alpha, beta, d = d, side = side), action)
        if alpha is None or alpha < succValAction[0]:
            alpha = succValAction[0]
        choices.append(succValAction)
    value, action = max(choices)
    return action

gamesWon = 0
gamesLost = 0
gamesDraw = 0
numGames = 1
averageNumMoves = 0.0
for _ in range(numGames):
    game = model.AbaloneGame(100, boardSize = 3)
    policies = {game.black: AlphaBeta, game.white: humanPolicy}
    state = game.startState()
    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
    game.visualization(dict_pos)

    while not game.isEnd(state):
        print('='*20)
        player = game.player(state)
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        print("Number of Rounds: ", numRound)
        print("Current Player: ", player)
        policy = policies[player]
        start_time = time.time()
        action = policy(game, state, side = player)
        state = game.succ(state, action)
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        print("Num Black Off Grid: ", num_black_Off_grid)
        print("Num White Off Grid: ", num_white_Off_grid)
        # print ("My program took", time.time() - start_time, "to run")
        game.visualization(dict_pos)

    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
    averageNumMoves += numRound
    if (num_black_Off_grid >= game.numToWin):
        print("White Won!!")
        gamesLost +=1
    elif (num_white_Off_grid >= game.numToWin):
        print("Black Won!!")
        gamesWon += 1
    else:
        gamesDraw += 1
        print("No One Won!")

averageNumMoves /= numGames
print("Number of won games: ", gamesWon)
print("Number of lost games: ", gamesLost)
print("Number of draw games: ", gamesDraw)
print("average Number of Moves: ", averageNumMoves)
