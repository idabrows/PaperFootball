import random
import math

class RandomModel:

    def predict(self, x, pos=None):
        return random.uniform(0, 1)


class ForwardModel:

    def predict(self, x, pos=None):
        return 1 - math.sqrt((pos[0])**2 + (4 - pos[1])**2)/15


class BackwardModel:

    def predict(self, x, pos=None):
        return 1 - math.sqrt((12 - pos[0])**2 + (4 - pos[1])**2)/15
