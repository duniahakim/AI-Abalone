import model

def humanPolicy(game, state):
    while True:
        action = input('Input action:')
        if action in game.actions(state):
            return action

def minimaxPolicy(game, state):
    def recurse(state):
        if game.isEnd(state):
            return (game.utility(state), 'none')
        choices = []
        for action in game.actions(state):
            succ = game.succ(state, action)
            if succ is not None:
                choices.append((recurse(succ)[0], action))
        if game.player(state) == game.black:
            return max(choices)
        elif game.player(state) == game.white:
            return min(choices)
    value, action = recurse(state)
    print('minimax sats action = {}, value = {}'. format(action, value))
    return action


game = model.AbaloneGame(100)
policies = {game.black: humanPolicy, game.white: minimaxPolicy}
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
