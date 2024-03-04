import numpy as np
    
for i in range(5):
    np.random.seed()
    a = np.arange(10)
    np.random.shuffle(a)
    print(a)

