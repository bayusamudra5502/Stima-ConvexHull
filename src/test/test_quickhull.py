from myConvexHull import myConvexHull
import numpy as np

def test_tc_kuliah():
  p = [
    np.array([1,1]),
    np.array([2,2]),
    np.array([4,4]),
    np.array([0,0]),
    np.array([1,2]),
    np.array([3,1]),
    np.array([3,3])
  ]

  hasil = np.array(myConvexHull(p))
  ans = np.array([[0,0],[1,2],[4,4],[3,1]])
  
  assert (hasil == ans).all()