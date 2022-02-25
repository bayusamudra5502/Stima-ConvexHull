import numpy as np
from util.line import point_distance, point_position

def test_jarak0():
  p = np.array([0,0])
  a = np.array([-1,1])
  b = np.array([1,1])

  res = point_distance(p, tuple([a,b]))
  assert res == 1

def test_jarak1():
  p = np.array([0,0])
  a = np.array([-1,-1])
  b = np.array([1,1])

  res = point_distance(p, tuple([a,b]))
  assert res == 0

def test_jarak2():
  p = np.array([1,0])
  a = np.array([-1,-1])
  b = np.array([1,1])

  res = point_distance(p, tuple([a,b]))
  assert res == 0.5 * np.sqrt(2)


def test_posisi0():
  p = np.array([0,0])
  a = np.array([-1,1])
  b = np.array([1,1])

  res = point_position(p, tuple([a, b]))
  assert res < 0

def test_posisi1():
  p = np.array([2,2])
  a = np.array([-1,1])
  b = np.array([1,1])

  res = point_position(p, tuple([a, b]))
  assert res > 0

def test_posisi2():
  p = np.array([1,0])
  a = np.array([-2,-2])
  b = np.array([2,2])

  res = point_position(p, tuple([a, b]))
  assert res < 0

def test_posisi3():
  p = np.array([0,0])
  a = np.array([-2,-2])
  b = np.array([2,2])

  res = point_position(p, tuple([a, b]))
  assert res == 0
