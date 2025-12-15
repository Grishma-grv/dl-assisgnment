import numpy as np
import pickle

class Player:
    def __init__(self, epsilon=0.3):
        self.Q = {}
        self.epsilon = epsilon
        self.lr = 0.2
        self.gamma = 0.9

    def get_state(self, board):
        return str(board)

    def choose_action(self, board, actions):
        if np.random.rand() < self.epsilon:
            return actions[np.random.choice(len(actions))]
        values = [self.Q.get((self.get_state(board), a), 0) for a in actions]
        return actions[np.argmax(values)]

print("Tic Tac Toe optimized RL model ready")
