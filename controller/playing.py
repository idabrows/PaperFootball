# import numpy as np
# import random
#
# from controller import config
# from model.game import Game
# from model.ml_module.agent import Agent
# from model.ml_module.ml_model import Residual_CNN
# from model.ml_module.user import User


# def playMatchesBetweenVersions(env, run_version, player1version, player2version,
#                                EPISODES, logger, turns_until_tau0, goes_first = 0):
#     if player1version == -1:
#         player1 = User('player1', env.state_size, env.action_size)
#         return 0
#     else:
#         player1_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, env.input_shape,
#                                   env.action_size, config.HIDDEN_CNN_LAYERS)
#         if player1version > 0:
#             player1_network = player1_NN.read(env.name, run_version, player1version)
#             player1_NN.model.set_weights(player1_network.get_weights())
#         player1 = Agent('player1', env.state_size, env.action_size, config.MCTS_SIMS, config.CPUCT, player1_NN)
#     if player2version == -1:
#         player2 = User('player2', env.state_size, env.action_size)
#     else:
#         player2_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, env.input_shape,
#                                   env.action_size, config.HIDDEN_CNN_LAYERS)
#
#         if player2version > 0:
#             player2_network = player2_NN.read(env.name, run_version, player2version)
#             player2_NN.model.set_weights(player2_network.get_weights())
#         player2 = Agent('player2', env.state_size, env.action_size, config.MCTS_SIMS, config.CPUCT, player2_NN)
#
#     scores, memory, points, sp_scores = playMatches(player1, player2, EPISODES, logger, turns_until_tau0, None, goes_first)
#
#     return scores, memory, points, sp_scores
#
#
# def playMatches(player1, player2, EPISODES, logger, turns_until_tau0, memory = None, goes_first = 0):
#     env = Game()
#     scores = {player1.name:0, "drawn": 0, player2.name:0}
#     sp_scores = {'sp':0, "drawn": 0, 'nsp':0}
#     points = {player1.name:[], player2.name:[]}
#     for e in range(EPISODES):
#         state = env.reset()
#         done = 0
#         turn = 0
#         player1.mcts = None
#         player2.mcts = None
#         if goes_first == 0:
#             player1Starts = random.randint(0,1) * 2 - 1
#         else:
#             player1Starts = goes_first
#         if player1Starts == 1:
#             players = {1:{"agent": player1, "name":player1.name}
#                     , -1: {"agent": player2, "name":player2.name}
#                     }
#         else:
#             players = {1:{"agent": player2, "name":player2.name}
#                     , -1: {"agent": player1, "name":player1.name}
#                     }
#         while done == 0:
#             turn = turn + 1
#             #### Run the MCTS algo and return an action
#             if turn < turns_until_tau0:
#                 action, pi, MCTS_value, NN_value = players[state.playerTurn]['agent'].act(state, 1)
#             else:
#                 action, pi, MCTS_value, NN_value = players[state.playerTurn]['agent'].act(state, 0)
#             if memory != None:
#                 ####Commit the move to memory
#                 memory.commit_stmemory(env.identities, state, pi)
#             ### Do the action
#             state, value, done, _ = env.step(action) #the value of the newState from the POV of the new playerTurn i.e. -1 if the previous player played a winning move
#
#             if done == 1:
#                 if memory != None:
#                     #### If the game is finished, assign the values correctly to the game moves
#                     for move in memory.stmemory:
#                         if move['playerTurn'] == state.playerTurn:
#                             move['value'] = value
#                         else:
#                             move['value'] = -value
#                     memory.commit_ltmemory()
#                 if value == 1:
#                     scores[players[state.playerTurn]['name']] = scores[players[state.playerTurn]['name']] + 1
#                     if state.playerTurn == 1:
#                         sp_scores['sp'] = sp_scores['sp'] + 1
#                     else:
#                         sp_scores['nsp'] = sp_scores['nsp'] + 1
#                 elif value == -1:
#                     scores[players[-state.playerTurn]['name']] = scores[players[-state.playerTurn]['name']] + 1
#
#                     if state.playerTurn == 1:
#                         sp_scores['nsp'] = sp_scores['nsp'] + 1
#                     else:
#                         sp_scores['sp'] = sp_scores['sp'] + 1
#                 else:
#                     scores['drawn'] = scores['drawn'] + 1
#                     sp_scores['drawn'] = sp_scores['drawn'] + 1
#                 pts = state.score
#                 points[players[state.playerTurn]['name']].append(pts[0])
#                 points[players[-state.playerTurn]['name']].append(pts[1])
#     return scores, memory, points, sp_scores
from random import random
from controller import config
from model.game import Game


def play_training(p1, p2, memory):
    env = Game()
    players = {1: p1, -1: p2}
    for e in range(config.EPISODES):
        env.reset()
        done, result = 0, 0
        if random.randint(0, 1) > 0.5:
            p1, p2 = p2, p1
        while done == 0:
            next_state, curr_point, move = players[env.currentPlayer].get_move(env)
            memory.append_stmemory(env.currentPlayer, next_state, curr_point)
            done, result = env.make_move(move)
            if done == 1:
                memory.commit_stmemory(env, result)
            env.change_turn()
    # return memory

def play_valid(p1, p2):
    pass