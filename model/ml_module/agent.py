# import numpy as np
# import random
# import model.ml_module.MCTS as mc
# from controller.loss import softmax_cross_entropy_with_logits
# import controller.config as config
# import time
#
# import matplotlib.pyplot as plt
# from IPython import display
# import pylab as pl

#
# class Agent:
#     def __init__(self, name, state_size, action_size, mcts_simulations, cpuct, model):
#         self.name = name
#         self.state_size = state_size
#         self.action_size = action_size
#         self.cpuct = cpuct
#         self.MCTSsimulations = mcts_simulations
#         self.model = model
#         self.mcts = None
#         self.train_overall_loss = []
#         self.train_value_loss = []
#         self.train_policy_loss = []
#         self.val_overall_loss = []
#         self.val_value_loss = []
#         self.val_policy_loss = []
#
#     def simulate(self):
#         ##### MOVE THE LEAF NODE
#         leaf, value, done, breadcrumbs = self.mcts.moveToLeaf()
#         ##### EVALUATE THE LEAF NODE
#         value, breadcrumbs = self.evaluateLeaf(leaf, value, done, breadcrumbs)
#         ##### BACKFILL THE VALUE THROUGH THE TREE
#         self.mcts.backFill(leaf, value, breadcrumbs)
#
#     def act(self, state, tau):
#         if self.mcts == None or state.id not in self.mcts.tree:
#             self.buildMCTS(state)
#         else:
#             self.changeRootMCTS(state)
#         #### run the simulation
#         for sim in range(self.MCTSsimulations):
#             self.simulate()
#         #### get action values
#         pi, values = self.getAV(1)
#         ####pick the action
#         action, value = self.chooseAction(pi, values, tau)
#         nextState, _, _ = state.takeAction(action)
#         NN_value = -self.get_preds(nextState)[0]
#         return (action, pi, value, NN_value)
#
#     def get_preds(self, state):
#         # predict the leaf
#         inputToModel = np.array([self.model.convertToModelInput(state)])
#         preds = self.model.predict(inputToModel)
#         value_array = preds[0]
#         logits_array = preds[1]
#         value = value_array[0]
#         logits = logits_array[0]
#         allowedActions = state.allowedActions
#         mask = np.ones(logits.shape, dtype=bool)
#         mask[allowedActions] = False
#         logits[mask] = -100
#         # SOFTMAX
#         odds = np.exp(logits)
#         probs = odds / np.sum(odds)  ###put this just before the for?
#         return ((value, probs, allowedActions))
#
#     def evaluateLeaf(self, leaf, value, done, breadcrumbs):
#         if done == 0:
#             value, probs, allowedActions = self.get_preds(leaf.state)
#             probs = probs[allowedActions]
#             for idx, action in enumerate(allowedActions):
#                 newState, _, _ = leaf.state.takeAction(action)
#                 if newState.id not in self.mcts.tree:
#                     node = mc.Node(newState)
#                     self.mcts.addNode(node)
#                 else:
#                     node = self.mcts.tree[newState.id]
#                 newEdge = mc.Edge(leaf, node, probs[idx], action)
#                 leaf.edges.append((action, newEdge))
#         return value, breadcrumbs
#
#     def getAV(self, tau):
#         edges = self.mcts.root.edges
#         pi = np.zeros(self.action_size, dtype=np.integer)
#         values = np.zeros(self.action_size, dtype=np.float32)
#         for action, edge in edges:
#             pi[action] = pow(edge.stats['N'], 1 / tau)
#             values[action] = edge.stats['Q']
#         pi = pi / (np.sum(pi) * 1.0)
#         return pi, values
#
#     def chooseAction(self, pi, values, tau):
#         if tau == 0:
#             actions = np.argwhere(pi == max(pi))
#             action = random.choice(actions)[0]
#         else:
#             action_idx = np.random.multinomial(1, pi)
#             action = np.where(action_idx == 1)[0][0]
#         value = values[action]
#         return action, value
#
#     def replay(self, ltmemory):
#         for i in range(config.TRAINING_LOOPS):
#             minibatch = random.sample(ltmemory, min(config.BATCH_SIZE, len(ltmemory)))
#
#             training_states = np.array([self.model.convertToModelInput(row['state']) for row in minibatch])
#             training_targets = {'value_head': np.array([row['value'] for row in minibatch])
#                 , 'policy_head': np.array([row['AV'] for row in minibatch])}
#             fit = self.model.fit(training_states, training_targets, epochs=config.EPOCHS, verbose=1, validation_split=0,
#                                  batch_size=32)
#             self.train_overall_loss.append(round(fit.history['loss'][config.EPOCHS - 1], 4))
#             self.train_value_loss.append(round(fit.history['value_head_loss'][config.EPOCHS - 1], 4))
#             self.train_policy_loss.append(round(fit.history['policy_head_loss'][config.EPOCHS - 1], 4))
#
#         plt.plot(self.train_overall_loss, 'k')
#         plt.plot(self.train_value_loss, 'k:')
#         plt.plot(self.train_policy_loss, 'k--')
#         plt.legend(['train_overall_loss', 'train_value_loss', 'train_policy_loss'], loc='lower left')
#         display.clear_output(wait=True)
#         display.display(pl.gcf())
#         pl.gcf().clear()
#         time.sleep(1.0)
#         self.model.printWeightAverages()
#
#     def predict(self, inputToModel):
#         preds = self.model.predict(inputToModel)
#         return preds
#
#     def buildMCTS(self, state):
#         self.root = mc.Node(state)
#         self.mcts = mc.MCTS(self.root, self.cpuct)
#
#     def changeRootMCTS(self, state):
#         self.mcts.root = self.mcts.tree[state.id]
# #
import copy
import random

from controller import config
import numpy as np


class Agent:
    def __init__(self, name, model, random_moves=0):
        self.name = name
        self.model = model

    def retrain(self, memory, config=config):
        for i in range(config.TRAINING_LOOPS):
            # print([row['state'] for row in memory.ltmemory][0])
            # [self.model.convertToModelInput(row['state']) for row in memory.ltmemory]
            training_states = np.array([self.model.convertToModelInput_fit(row['state']) for row in memory.ltmemory])
            training_targets = {'value_head': np.array([row['result'] for row in memory.ltmemory])}
            print(training_states.shape)
            self.model.fit(training_states, training_targets, epochs=config.EPOCHS, verbose=1, validation_split=0.2,
                           batch_size=config.BATCH_SIZE)

    #             self.train_overall_loss.append(round(fit.history['loss'][config.EPOCHS - 1], 4))
    #             self.train_value_loss.append(round(fit.history['value_head_loss'][config.EPOCHS - 1], 4))
    #             self.train_policy_loss.append(round(fit.history['policy_head_loss'][config.EPOCHS - 1], 4))

    def get_move(self, env, turn, random_moves):
        best_move, best_score = None, -100
        all_moves = env.get_all_allowed_moves()
        print(len(all_moves))
        if len(all_moves) > 1000:
            all_moves = random.sample(all_moves, 1000)
        for move in all_moves:
            sc = self.score_move(move, env, turn, random_moves)
            if sc > best_score:
                best_score = sc
                best_move = move
                if sc == 100:
                    return best_move
        return best_move

    def score_move(self, move, env, turn, random_moves):
        env_test = copy.deepcopy(env)
        done, result = env_test.make_move(move)
        if done == 1:
            if result == 1:
                return 100
            else:
                return -99
        else:
            if turn < random_moves:
                return random.uniform(0, 1)
            # print('Predictin: ', self.model.predict(env_test.gameState.board, env_test.gameState.current_position))
            return self.model.predict(self.model.convertToModelInput(env_test.gameState.board), env_test.gameState.current_position)