import numpy as np


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


a = sigmoid(0.5632)

print(a)