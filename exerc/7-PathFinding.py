import matplotlib.pyplot as plt
 
class PathFinding(object):
  def __init__(self):
    self.bars = []
    self.bars.append([(3, 3)])
 
  def heuristic(self, initial, goal):
    h = 1
    h1 = 1
    hx = abs(initial[0] - goal[0])
    hy = abs(initial[1] - goal[1])

    return h * (hx + hy) + (h1 - 2 * h) * min(hx, hy)
 
  def getVertexNeighbours(self, position):
    vertexNeighboursList = []

    for hx, hy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
      x1 = position[0] + hx
      y1 = position[1] + hy
      
      if x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7:
        continue
      
      vertexNeighboursList.append((x1, y1))

    return vertexNeighboursList
 
  def expenseChange(self, a, b):
    for bar in self.bars:
      if b in bar:
        return 100
      return 10
 
def Search(initial, final, graph):
  G = {}
  O = {}
 
  G[initial] = 0
  O[initial] = graph.heuristic(initial, final)
 
  closed = set()
  open = set([initial])

  cameFrom = {}
 
  while len(open) > 0:
    current = None
    currentValue = None
    
    for position in open:
      if current is None or O[position] < currentValue:
        currentValue = O[position]
        current = position
 
    if current == final:
      path = [current]
      while current in cameFrom:
        current = cameFrom[current]
        path.append(current)

      path.reverse()
      return path, O[final]
 
    open.remove(current)
    closed.add(current)
 
    for neighbour in graph.getVertexNeighbours(current):
      if neighbour in closed:
        continue

      candidateG = G[current] + graph.expenseChange(current, neighbour)
 
      if neighbour not in open:
        open.add(neighbour)
      elif candidateG >= G[neighbour]:
        continue
 
      cameFrom[neighbour] = current
      G[neighbour] = candidateG

      H = graph.heuristic(neighbour, final)
      O[neighbour] = G[neighbour] + H
 
if __name__ == "__main__":
  graph = PathFinding()
  route, expense = Search((5, 5), (0, 0), graph)

  print("ROTA: {}".format(route))
  print("CUSTO: {}".format(expense))

  plt.plot([v[0] for v in route], [v[1] for v in route])

  for bar in graph.bars:
    plt.plot([v[0] for v in bar], [v[1] for v in bar])
        
  plt.xlim(-1, 8)
  plt.ylim(-1, 8)
  plt.show()
 