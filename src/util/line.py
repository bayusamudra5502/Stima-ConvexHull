# Line Utility
# Utilitas yang berkaitan dengan garis dan titik

import numpy as np

def point_distance(p: np.ndarray, line:tuple[np.ndarray,np.ndarray]):
  """Menghitung jarak titik ke garis"""
  a = p - line[0]
  b = line[1] - line[0]

  factor = np.sum(a * b)/np.sum(b * b)
  v = a - factor * b

  return np.sqrt(np.sum(v * v))

def point_position(p: np.ndarray, line:tuple[np.ndarray,np.ndarray]):
  """Fungsi untuk menentukan posisi titik
  
  Menghasilkan > 0 jika diatas garis, = 0 jika tepat pada garis, dan
  < 0 jika dibawah garis
  """
  
  return (p[1] * line[1][0] + p[0] * line[0][1] + line[0][0] * line[1][1]) - \
      (p[0] * line[1][1] + line[0][0] * p[1] + line[0][1] * line[1][0])