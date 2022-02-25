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

def point_cosine(p: np.ndarray, line:tuple[np.ndarray,np.ndarray]):
  """Menghitung cosinus dari garis"""
  a = p - line[0]
  b = line[1] - line[0]
  na = np.sum(a * a)
  nb = np.sum(b * b)

  return np.sum(a * b) / (na * nb)

def point_position(p: np.ndarray, line:tuple[np.ndarray,np.ndarray]):
  """Fungsi untuk menentukan posisi titik
  
  Menghasilkan > 0 jika diatas garis, = 0 jika tepat pada garis, dan
  < 0 jika dibawah garis
  """
  
  return (p[1] * line[1][0] + p[0] * line[0][1] + line[0][0] * line[1][1]) - \
      (p[0] * line[1][1] + line[0][0] * p[1] + line[0][1] * line[1][0])

def max_point(points: list, line: tuple) -> np.ndarray:
  """Mencari Titik dengan jarak terjauh dan sudut terbesar"""
  maxPoint = points[0]
  maxDist = point_distance(maxPoint, line)

  for i in points:
    dist = point_distance(i, line)

    if maxDist < dist:
      maxDist = dist
      maxPoint = i
    elif maxDist == dist:
      curCos = point_cosine(maxPoint, line)
      iCos = point_cosine(i, line)

      if(iCos < curCos):
        # Sudut lebih besar
        maxPoint = i
        maxDist = dist