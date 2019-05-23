import model

def humanPolicy(game, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

def AlphaBeta(game, state, side = 1):


    def recurse(game, state, alpha, beta, d = 1, side = 1):
        # if not game.printed2 and d == 2:
        #     print "depth: ", d
        #     game.printed2 = True
        #     game.printed1 = False
        #     game.printed0 = False
        # if not game.printed1 and d == 1:
        #     print "depth: ", d
        #     game.printed1 = True
        #     game.printed2 = False
        #     game.printed0 = False
        # if not game.printed0 and d == 0:
        #     print "depth: ", d
        #     game.printed0 = True
        #     game.printed1 = False
        #     game.printed2 = False
        if game.isEnd(state):
            return side * game.utility(state)
        if d == 0:
            if side == game.black:
                w = {}
                w['w_num_black_Off_grid'] = -200
                w['w_num_white_Off_grid'] = 200
                w['w_num_black_on_edge'] = -20
                w['w_num_white_on_edge'] = 20
                w['w_black_average_pos'] = -50
                w['w_white_average_pos'] = 50
                return game.eval(state, w)
            else:
                w = {}
                w['w_num_black_Off_grid'] = 100
                w['w_num_white_Off_grid'] = -100
                w['w_num_black_on_edge'] = 300
                w['w_num_white_on_edge'] = -200
                w['w_black_average_pos'] = 100
                w['w_white_average_pos'] = -100
                return game.eval(state, w)
        if game.player(state) == side:
            newAlpha = alpha
            choices = []
            for action in game.actions(state):
                succGameState = game.succ(state, action)
                if succGameState is None:
                    continue
                succVal = recurse(game, succGameState, newAlpha, None, d = d, side = side)
                if beta is not None and succVal > beta:
                    return succVal
                if newAlpha is None or succVal > newAlpha:
                    newAlpha = succVal
                choices.append(succVal)
            return max(choices)
        else:
            newBeta = beta
            choices = []
            for action in game.actions(state):
                succGameState = game.succ(state, action)
                if succGameState is None:
                    continue
                succVal = recurse(game, succGameState, None, newBeta, d = d - 1, side = side)
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
        succValAction = (recurse(game, succGameState, alpha, beta, side = side), action)
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
    action = policy(game, state, side = player)
    state = game.succ(state, action)
    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
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
