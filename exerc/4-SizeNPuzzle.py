from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

actions = {
  'MOVEUP': 'move-up',
  'MOVEDOWN': 'move-down',
  'MOVELEFT': 'move-left',
  'MOVERIGHT': 'move-right'  
}

class SizeNPuzzle:
  def __init__(self, matrix):
    self.matrix = []

    for x in range(len(matrix)):
      self.matrix.append([])

      for z in range(len(matrix[x])):
        	self.matrix[x].append(matrix[x][z])

  def findIndx(self, arr):
    res = [-1, -1]
    count = 0

    for e in arr:
      index = [i for i in range(len(e)) if e[i] == None]

      if(len(index) > 0):
        res = [count, index[0]]
      
      count += 1
    
    return res

  def doAction(self, action):
    state = self.clone()
    i = 0
    j = None

    while (i < len(self.matrix)):
      l = self.findIndx(self.matrix)
      j = l[1]
      i = l[0]

      if (j != -1):
        break

    if (action == actions['MOVEDOWN']):
      state.matrix[i][j] = self.matrix[i + 1][j]
      state.matrix[i + 1][j] = None

    elif (action == actions['MOVEUP']):
      state.matrix[i][j] = self.matrix[i - 1][j]
      state.matrix[i - 1][j] = None

    elif (action == actions['MOVELEFT']):
      state.matrix[i][j] = self.matrix[i][j - 1]
      state.matrix[i][j - 1] = None

    elif (action == actions['MOVERIGHT']):
      state.matrix[i][j] = self.matrix[i][j + 1]
      state.matrix[i][j + 1] = None

    return state

  def getActions(self):
    arr = []
    i = 0
    j = None

    while (i < len(self.matrix)):
      l = self.findIndx(self.matrix)
      j = l[1]
      i = l[0]

      if (j != -1):
        break

    if (i + 1 < len(self.matrix)):
      arr.append(actions['MOVEDOWN'])
    
    if (i - 1 >= 0):
      arr.append(actions['MOVEUP'])

    if (j + 1 < len(self.matrix[i])):
      arr.append(actions['MOVERIGHT'])

    if (j - 1 >= 0):
      arr.append(actions['MOVELEFT'])

    return arr

  def equals(self, o):
    if (len(self.matrix) != len(o.matrix)):
      return False
    
    for i in range(len(self.matrix)):
      if (len(self.matrix[i]) != len(o.matrix[i])):
        return False
      
      for j in range(len(self.matrix[i])):

        if (self.matrix[i][j] != o.matrix[i][j]):
          return False
    
    return True

  def clone(self):
    return SizeNPuzzle(self.matrix)

  def __str__(self):
    str = "[\n"

    for i in range(len(self.matrix)):
      str += '[{}]\n'.format(self.matrix[i])
    
    str += "]"

    return str

initial = SizeNPuzzle(
  [
    [   4,    2,    7],
    [None,    8,    6],
    [   3,    5,    1]
  ]
)

finals = [
  SizeNPuzzle (
    [
      [    1,    4,    7],
      [    2,    5,    8],
      [    3,    6, None]
    ]
  )
]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms['DSF'])

if (result):
  for i in result:
    print(i)