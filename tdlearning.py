import model

def getBlackWeights():
    w = {}
    w['num_black_Off_grid'] = -10
    w['num_white_Off_grid'] = 12
    w['num_black_on_edge'] = -1
    w['num_white_on_edge'] = 2
    w['black_average_pos'] = -1
    w['white_average_pos'] = 2
    w['black_coherence'] = 2
    w['white_coherence'] = -1
    w['black_break'] = 2
    w['white_break'] = 0
    return w

def getWhiteWeights():
    w = {}
    w['num_black_Off_grid'] = 12
    w['num_white_Off_grid'] = -10
    w['num_black_on_edge'] = 2
    w['num_white_on_edge'] = -1
    w['black_average_pos'] = 2
    w['white_average_pos'] = -1
    w['black_coherence'] = -1
    w['white_coherence'] = 2
    w['black_break'] = 0
    w['white_break'] = 2
    return w



class TD:
    def __init__(self, w, game, eta = 0.00001, gamma = 0.2, side = 1):
        self.w = w #a dictionary
        self.gamma = gamma
        self.eta = eta
        self.objective = side

    def target(self, game, nextState):
        r = game.utility(nextState)
        V = game.eval(nextState, self.w)
        return r + self.gamma * V

    def prediction(self, game, state):
        return game.eval(state, self.w)

    def update(self, game, state, nextState):
        scale = - self.eta * (self.prediction(game, state) - self.target(game, nextState))
        features = game.features(state)
        self.dictAddition(self.w, features, scale)
        #print self.prediction(game, state), self.target(game, nextState), scale, features

    def dictAddition(self, d1, d2, scale = 1):
        #Modity d1 in place
        for key in d1:
            if key in d2:
                d1[key] += scale * d2[key]

    def iteration(self, game, state):
        succStates = []
        actions = game.actions(state)
        for action in actions:
            succ = game.succ(state, action)
            if succ is not None:
                succStates.append(succ)
        dict_pos, num_black_Off_grid, num_white_Off_grid, player, numRound = state
        selectedState = None
        if player == self.objective:
            selectedState = max(succStates, key = lambda k : game.eval(k, self.w))
        else:
            selectedState = min(succStates, key=lambda k: game.eval(k, self.w))
        self.update(game, state, selectedState)
        return selectedState


# w = {}
# w['num_black_Off_grid'] = -10
# w['num_white_Off_grid'] = 10
# w['num_black_on_edge'] = -1
# w['num_white_on_edge'] = 1
# w['black_average_pos'] = 1
# w['white_average_pos'] = -1
# w['black_coherence'] = 1
# w['white_coherence'] = -1
# w['black_break'] = -1
# w['white_break'] = 1

# w['num_black_Off_grid'] = -10
# w['num_white_Off_grid'] = 12
# w['num_black_on_edge'] = -1
# w['num_white_on_edge'] = 2
# w['black_average_pos'] = -1
# w['white_average_pos'] = 2
# w['black_coherence'] = 2
# w['white_coherence'] = -1
# w['black_break'] = 2
# w['white_break'] = 0

game = model.AbaloneGame(500, boardSize = 2)
side = game.white
if side == game.black:
    weights = getBlackWeights()
elif side == game.white:
    weights = getWhiteWeights()
for i in range(100):
    td = TD(weights, game, side = game.white)
    state = game.startState()
    while not game.isEnd(state):
        state = td.iteration(game, state)
        # game.visualization(state[0])
        weights = td.w
print(td.w)
