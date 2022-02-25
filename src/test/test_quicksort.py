import numpy as np
from util.quicksort import partition, quicksort

def test_partition1():
  arr = np.array([5,1,2,3,4])
  partition(arr, lambda x,y: x - y)

  assert (arr == np.array([4,1,2,3,5])).all()

def test_partition2():
  arr = np.array([1,2,3,4,5])
  partition(arr, lambda x,y: x - y)

  assert (arr == np.array([1,2,3,4,5])).all()

def test_partition3():
  arr = np.array([4,3,5,2,2])
  partition(arr, lambda x,y: x - y)

  assert (arr == np.array([2,3,2,4,5])).all()

def test_partition4():
  arr = np.array([])
  partition(arr, lambda x,y: x - y)

  assert (arr == np.array([])).all()

def test_sort1():
  arr = np.array([1,3,2,5,2,6,6,8,9,2])
  ans = np.sort(arr)

  quicksort(arr, lambda x,y: x-y)

  assert (ans == arr).all()

def test_sort2():
  arr = np.array([5,1,2,3,4])
  ans = np.sort(arr)

  quicksort(arr, lambda x,y: x-y)

  assert (ans == arr).all()

def test_sort3():
  arr = np.array([5,4,3,2,1,0])
  ans = np.sort(arr)

  quicksort(arr, lambda x,y: x-y)

  assert (ans == arr).all()

def test_sort4():
  arr = np.array([1,2,1])
  ans = np.sort(arr)

  quicksort(arr, lambda x,y: x-y)

  assert (ans == arr).all()

def test_sort4():
  arr = np.array([])
  ans = np.sort(arr)

  quicksort(arr, lambda x,y: x-y)

  assert (ans == arr).all()
