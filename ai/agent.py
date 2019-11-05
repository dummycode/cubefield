class Agent:
    def __init__(self):
        return

    def trainNetwork(self, model, game_state):
        D = deque()

        do_nothing = np.zeros(ACTIONS)
