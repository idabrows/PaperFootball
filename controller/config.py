EPISODES = 60
MCTS_SIMS = 50
MEMORY_SIZE = 5000
TURNS_UNTIL_DET = 6
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8

max_t = 1500

BATCH_SIZE = 64
EPOCHS = 4
REG_CONST = 0.001
LEARNING_RATE = 0.02
MOMENTUM = 0.9
TRAINING_LOOPS = 1

INPUT_SHAPE = (48,8,1)

HIDDEN_CNN_LAYERS = [
    {'filters': 175, 'kernel_size': (4, 4)}
    , {'filters': 175, 'kernel_size': (4, 4)}
    , {'filters': 175, 'kernel_size': (4, 4)}
    # , {'filters': 175, 'kernel_size': (4, 4)}
    # , {'filters': 175, 'kernel_size': (4, 4)}
    # , {'filters': 175, 'kernel_size': (4, 4)}
]

EVAL_EPISODES = 10
SCORING_THRESHOLD = 1.1
