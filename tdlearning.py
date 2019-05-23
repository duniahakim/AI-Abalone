import model

class TD:
    def __init__(self, w, eta = 0.1):
        self.w = w #a dictionary
        self.eta = eta

    def target(self, game, nextState):
        r = game.util(nextState)
        V = game.eval(nextState, self.w)
        return r + self.gamma * V

    def prediction(self, game, state):
        return game.eval(state, self.w)

    def update(self, game, state, action, nextState):
        scale = - self.eta * (self.prediction(game, state) - self.target(game, nextState))
        features = game.features()
        self.dictAddition(self.w, features, scale)

    def dictAddition(self, d1, d2, scale = 1):
        #Modity d1 in place
        for key in d1:
            if key in d2:
                d1[key] += scale * d2

    def iteration(self, game, state):
        actions = game.actions(state)
        #for action in action
        #TO BE COMPLETED
