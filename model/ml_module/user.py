# import numpy as np
#
#
# class User():
#     def __init__(self, name, state_size, action_size):
#         self.name = name
#         self.state_size = state_size
#         self.action_size = action_size
#
#     def act(self, state, tau):
#         action = input('Enter your chosen action: ')
#         pi = np.zeros(self.action_size)
#         pi[action] = 1
#         value = None
#         NN_value = None
#         return action, pi, value, NN_value
