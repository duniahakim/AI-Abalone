import model

def humanPolicy(game, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

def AlphaBeta(game, state):


    def recurse(game, state, alpha, beta, d = 1):
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
            return game.utility(state)
        if d == 0:
            return game.eval(state)
        if game.player(state) == game.black:
            newAlpha = alpha
            choices = []
            for action in game.actions(state):
                succGameState = game.succ(state, action)
                if succGameState is None:
                    continue
                succVal = recurse(game, succGameState, newAlpha, None, d = d)
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
                succVal = recurse(game, succGameState, None, newBeta, d = d - 1)
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
        succValAction = (recurse(game, state, alpha, beta), action)
        if alpha is None or alpha < succValAction[0]:
            alpha = succValAction[0]
        choices.append(succValAction)
    value, action = max(choices)
    return action


game = model.AbaloneGame(100)
policies = {game.black: AlphaBeta, game.white: humanPolicy}
state = game.startState()
dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
game.visualization(dict_pos)

while not game.isEnd(state):
    print('='*20)
    player = game.player(state)
    policy = policies[player]
    action = policy(game, state)
    state = game.succ(state, action)
    dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
    game.visualization(dict_pos)