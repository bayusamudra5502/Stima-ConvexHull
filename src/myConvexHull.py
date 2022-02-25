# Library myConvexHull
# Mencari Convex Hull dari larik titik dua dimensi

import numpy as np

from util.line import max_point, point_position
from util.quicksort import quicksort
from util.compare import compare_point

def myConvexHull(points: np.ndarray) -> list:
  """Mencari ConvexHull menggunakan Strategi DnC"""
  upper = []
  lower = []

  pointSorted = np.copy(points)
  quicksort(pointSorted, compare_point)
  line = (pointSorted[0], pointSorted[-1])

  for i in pointSorted:
    if(point_position(i, line) > 0):
      upper.append(i)
    elif(point_position(i,line) < 0):
      lower.append(i)

  upperPartition = convexHullPartition(upper, line)
  lowerPartition = convexHullPartition(lower, line)

  result = [pointSorted[0]] + upperPartition + [pointSorted[-1]] + lowerPartition
  return result

def convexHullPartition(points: list, anchor: tuple) -> list:
  """Partisi untuk perhitungan convexhull"""
  if len(points) <= 1:
    return points

  point = max_point(points, anchor)
  lineleft = (anchor[0], point)
  lineright = (point, anchor[1])
  upleft = []
  upright = []

  for i in points:
    if point_position(i, lineleft) > 0:
      upleft.append(i)
    elif point_position(i, lineright) > 0:
      upright.append(i)
  
  leftCH = convexHullPartition(upleft, lineleft)
  rightCH = convexHullPartition(upright, lineright)

  result = leftCH + [point] + rightCH
  return result
