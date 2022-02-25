# Graph Utility
# Utilitas untuk menampilkan grafik hasil ConvexHull

import matplotlib.pyplot as plt

def show_graph(points, convexhull, color):
  """Show result in graph"""
  plt.scatter(points[:,0], points[:,1], c=color)
  x = []
  y = []

  for i in convexhull:
    x.append(i[0])
    y.append(i[1])
  
  plt.plot(x, y, color)
  plt.plot([convexhull[-1][0],convexhull[0][0]],
            [convexhull[-1][1],convexhull[0][1]],
            color)