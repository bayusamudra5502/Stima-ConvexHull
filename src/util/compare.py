# Fungsi Compare
# Utilitas untuk komparasi

import numpy as np

def compare_point(p1: np.ndarray, p2: np.ndarray):
  if(p1[0] == p2[0]):
    return p1[1] - p2[1]
  else:
    return p1[0] - p2[0]

