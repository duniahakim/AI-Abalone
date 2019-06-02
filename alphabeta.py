import model
import random
import time

def humanPolicy(game, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

def getDefaultWeights():
    w = {}
    w['num_black_Off_grid'] = 100
    w['num_white_Off_grid'] = -100
    w['num_black_on_edge'] = 100
    w['num_white_on_edge'] = -100
    w['black_average_pos'] = 100
    w['white_average_pos'] = -100
    w['black_coherence'] = -100
    w['white_coherence'] = 100
    w['black_break'] = -100
    w['white_break'] = 100
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
    return zip(*sortedPossibilities)[0]



def AlphaBeta(game, state, side = 1):

    def recurse(game, state, alpha, beta, d = 1, side = 1):
        if game.isEnd(state):
            return side * game.utility(state)
        if d == 0:
            if side == game.black:
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

                return game.eval(state, w)
            else:
                w = {}
                w['num_black_Off_grid'] = 100
                w['num_white_Off_grid'] = -100
                w['num_black_on_edge'] = 100
                w['num_white_on_edge'] = -100
                w['black_average_pos'] = 100
                w['white_average_pos'] = -100
                w['black_coherence'] = -100
                w['white_coherence'] = 100
                w['black_break'] = -100
                w['white_break'] = 100



                return game.eval(state, w)
        if game.player(state) == side:
            newAlpha = alpha
            choices = []
            orderedSuccStatesForMax = getOrderedSuccStates(game, state, False)
            for succGameState in orderedSuccStatesForMax:
            # for action in game.actions(state):
                # succGameState = game.succ(state, action)
                # if succGameState is None:
                #     continue
                d = getDepth(game, succGameState)
                succVal = recurse(game, succGameState, newAlpha, beta, d = d, side = side)

                if beta is not None and succVal > beta:
                    return succVal
                if newAlpha is None or succVal > newAlpha:
                    newAlpha = succVal
                choices.append(succVal)
            return max(choices)
        else:

            newBeta = beta
            choices = []
            orderedSuccStatesForMin = getOrderedSuccStates(game, state, True)
            for succGameState in orderedSuccStatesForMin:
            # for action in game.actions(state):
                # succGameState = game.succ(state, action)
                # if succGameState is None:
                #     continue
                d = getDepth(game, succGameState)
                succVal = recurse(game, succGameState, alpha, newBeta, d = d - 1, side = side)
                if alpha is not None and succVal < alpha:
                    return succVal
                if newBeta is None or succVal < newBeta:
                    newBeta = succVal
                choices.append(succVal)
            return min(choices)

    alpha = None
    beta = None
    choices = []
    for action in game.actions(state):
        succGameState = game.succ(state, action)
        if succGameState is None:
            continue
        d = getDepth(game, succGameState)
        succValAction = (recurse(game, succGameState, alpha, beta, d = d, side = side), action)
        if alpha is None or alpha < succValAction[0]:
            alpha = succValAction[0]
        choices.append(succValAction)
    value, action = max(choices)
    return action


game = model.AbaloneGame(500)
policies = {game.black: AlphaBeta, game.white: AlphaBeta}
state = game.startState()
dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
game.visualization(dict_pos)

while not game.isEnd(state):
    print('='*20)
    player = game.player(state)
    policy = policies[player]
    start_time = time.time()
    action = policy(game, state, side = player)
    print "My program took", time.time() - start_time, "to run"
    state = game.succ(state, action)
    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
    print("Number of Rounds: ", numRound)
    print("Current Player: ", player)
    print("Num Black Off Grid: ", num_black_Off_grid)
    print("Num White Off Grid: ", num_white_Off_grid)
    game.visualization(dict_pos)

dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
if (num_black_Off_grid >= 6):
    print("White Won!!")
elif (num_white_Off_grid >= 6):
    print("Black Won!!")
else:
    print("No One Won!")
