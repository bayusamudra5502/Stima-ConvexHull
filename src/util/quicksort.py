# Quicksort
# Implementasi Quicksort

from pyclbr import Function
import numpy as np

def partition(arr: np.ndarray, comparator: Function) -> int:
  """Melakukan Partisi pada tiap state dari quicksort"""
  if len(arr) == 0:
    return 0

  p = 1
  q = len(arr) -1

  while(p <= q):
    while(p < len(arr) and comparator(arr[p],arr[0]) < 0):
      p += 1

    while(q > 0 and comparator(arr[q],arr[0]) > 0):
      q -= 1
    
    if p <= q:
      tmp = np.copy(arr[p])
      arr[p] = np.copy(arr[q])
      arr[q] = tmp
      p += 1
      q -= 1
  
  
  tmp = np.copy(arr[0])
  arr[0] = np.copy(arr[q])
  arr[q] = tmp
  return q

def quicksort(arr: np.ndarray, comparator: Function) -> None:
  """Pengurutan array menggunakan quicksort"""
  if len(arr) <= 1:
    return
  
  idx = partition(arr, comparator)
  quicksort(arr[:idx], comparator)
  quicksort(arr[idx+1:], comparator)
