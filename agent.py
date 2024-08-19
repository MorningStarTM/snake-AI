import torch
from collections import deque
import numpy as np
from snake import SnakeGameAI


MAX_MEM = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self) -> None:
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0
        self.memory = deque(maxlen=MAX_MEM)
        # TODO: model , trainer

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self):
        pass

    def get_action(self, state):
        pass



def train():
    


if __name__ == "__main__":
    train()