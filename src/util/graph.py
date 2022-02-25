# Graph Utility
# Utilitas untuk menampilkan grafik hasil ConvexHull

import matplotlib.pyplot as plt

def show_graph(points, convexhull, color):
  """Show result in graph"""
  plt.scatter(points, c=color)
  length_convex = len(convexhull)

  for i in range(length_convex):
    plt.plot(convexhull[i % length_convex], 
      convexhull[(i+1) % length_convex], 
      color)
  