import numpy as np
from src.estimate import norm, denorm 
# import '/src/estimate.py' as e

ok = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

n = norm(ok, 9)
r = denorm(ok , n)
print(r)