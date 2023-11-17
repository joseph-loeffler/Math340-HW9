import random
import numpy as np

trials = 10000

for _ in range(trials):
    L1 = np.random.uniform(0,1)
    L2 = np.random.uniform(0,L1)
    L3 = np.random.uniform(0,L2)

    print(L1)

