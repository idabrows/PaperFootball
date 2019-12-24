from controller import config
from controller.playing import play_training, play_valid
from model.ml_module.agent import Agent
from model.ml_module.memory import Memory
from model.ml_module.ml_model import Residual_NN_simple


def main_train():
    current_nn = Residual_NN_simple(config.REG_CONST, config.LEARNING_RATE, config.INPUT_SHAPE, config.HIDDEN_CNN_LAYERS)
    best_nn = Residual_NN_simple(config.REG_CONST, config.LEARNING_RATE, config.INPUT_SHAPE, config.HIDDEN_CNN_LAYERS)
    best_nn.model.set_weights(current_nn.model.get_weights())
    memory = Memory(config.MEMORY_SIZE)
    current_player = Agent('current_player', current_nn)
    best_player = Agent('best_player',  best_nn)

    i = 0
    while i < 100:
        play_training(best_player, best_player, memory)
        if len(memory.ltmemory) >= config.MEMORY_SIZE:
            current_player.retrain(memory)
            memory.clear_ltmemory()
            scores = play_valid(current_player, best_player)
            print(scores)
            if scores > config.SCORING_THRESHOLD:
                best_player.model.set_weights(current_player.model.get_weights())

    return best_player
