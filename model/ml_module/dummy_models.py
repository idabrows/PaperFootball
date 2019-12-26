import random
import math


class RandomModel:

    @staticmethod
    def convertToModelInput(x):
        return x

    @staticmethod
    def predict(x, pos=None):
        return random.uniform(0, 1)


class ForwardModel:

    @staticmethod
    def convertToModelInput(x):
        return x

    @staticmethod
    def predict(x, pos=None):
        return 1 - math.sqrt((pos[0]) ** 2 + (4 - pos[1]) ** 2) / 15


class BackwardModel:

    @staticmethod
    def convertToModelInput(x):
        return x

    @staticmethod
    def predict(x, pos=None):
        return 1 - math.sqrt((12 - pos[0]) ** 2 + (4 - pos[1]) ** 2) / 15
