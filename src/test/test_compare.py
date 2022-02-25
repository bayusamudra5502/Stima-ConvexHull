import numpy as np
from util.compare import compare_point

def test_compare_lth():
  assert compare_point([1,3],[2,2]) < 0
  assert compare_point(np.array([1,3]),np.array([1,5])) < 0

def test_compare_eq():
  assert compare_point([0,0], [0,0]) == 0
  assert compare_point(np.array([0,0]), np.array([0,0])) == 0

def test_compare_gth():
  assert compare_point([3,3],[2,10]) > 0
  assert compare_point(np.array([3,3]),np.array([1,2])) > 0
