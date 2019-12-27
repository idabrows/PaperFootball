import pickle

import numpy as np
from collections import deque
from controller import config


class Memory:
    def __init__(self, size):
        self.MEMORY_SIZE = size
        self.ltmemory = deque(maxlen=2*size)
        self.stmemory = deque(maxlen=2*size)
        self.iter = 0

    def clear_ltmemory(self):
        self.iter += 1
        # file = open('games'+str(self.iter), 'wb')
        # pickle.dump(self.ltmemory, file)
        self.ltmemory.clear()

    def append_stmemory(self, player, state, current_position=None, result=None):
        self.stmemory.append({
            'player': player
            , 'state': state
            , ' ': result
            , 'current_position': current_position
        })

    def commit_stmemory(self, env, result):
        self.stmemory.append({
            'player': env.currentPlayer
            , 'state': env.gameState.board
            , 'result': result
            , 'current_position': env.gameState.current_position
        })

        for x in self.stmemory:
            if x['player'] == env.currentPlayer:
                x['result'] = result
            else:
                x['result'] = -result

        for i in self.stmemory:
            self.ltmemory.append(i)
        self.stmemory.clear()

    # def commit_ltmemory(self):
    #     for i in self.stmemory:
    #         self.ltmemory.append(i)
    #     self.clear_stmemory()
    #
