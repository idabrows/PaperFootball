EPISODES = 30
MCTS_SIMS = 50
MEMORY_SIZE = 10000
TURNS_UNTIL_TAU0 = 5
CPUCT = 1
EPSILON = 0.2
ALPHA = 0.8

BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 10

INPUT_SHAPE = (2,48,8)

HIDDEN_CNN_LAYERS = [
    {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
    , {'filters': 75, 'kernel_size': (4, 4)}
]

EVAL_EPISODES = 10
SCORING_THRESHOLD = 1.1
