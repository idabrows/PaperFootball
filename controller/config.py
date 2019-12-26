EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 1000
TURNS_UNTIL_DET = 8
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8

BATCH_SIZE = 256
EPOCHS = 3
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 1

INPUT_SHAPE = (48,8,1)

HIDDEN_CNN_LAYERS = [
    {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
]

EVAL_EPISODES = 4
SCORING_THRESHOLD = 1.1
