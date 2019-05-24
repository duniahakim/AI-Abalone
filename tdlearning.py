import model

class TD:
    def __init__(self, w, eta = 0.01, gamma = 1):
        self.w = w #a dictionary
        self.gamma = gamma
        self.eta = eta

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
        print self.prediction(game, state), self.target(game, nextState), scale, features

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

        maxState = max(succStates, key = lambda k : game.eval(k, self.w))
        self.update(game, state, maxState)
        return maxState


w = {}
w['w_num_black_Off_grid'] = -200
w['w_num_white_Off_grid'] = 200
w['w_num_black_on_edge'] = -20
w['w_num_white_on_edge'] = 20
w['w_black_average_pos'] = -50
w['w_white_average_pos'] = 50
game = model.AbaloneGame(500)
td = TD(w)
state = game.startState()
print(td.w)
td.iteration(game, state)
print(td.w)
