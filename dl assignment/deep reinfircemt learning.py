import numpy as np

class QLearningAgent:
    def __init__(self, size, gamma=0.8):
        self.Q = np.zeros((size, size))
        self.gamma = gamma

    def update(self, state, action, reward):
        self.Q[state, action] = reward + self.gamma * np.max(self.Q[action])

agent = QLearningAgent(11)

for _ in range(1000):
    s = np.random.randint(0,11)
    a = np.random.randint(0,11)
    agent.update(s, a, 100)

print("Q-learning training completed")
