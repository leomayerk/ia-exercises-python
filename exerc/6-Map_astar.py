from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

city = {
  'ARAD': ['Arad', 366],
  'SIBIU': ['Sibiu', 253],
  'TIMISUARA': ['Timisuara', 329],
  'ZERIND': ['Zerind', 374],
  'FAGARAS': ['Fagaras', 176],
  'ORADEA': ['Oradea', 380],
  'RIMNICU': ['Rimnicu', 193],
  'PITESTI': ['Pitesti', 100],
  'CRAIOVA': ['Craiova', 160],
  'BUCHAREST': ['Bucharest', 0],
  'LUGOJ': ['Lugoj', 244],
  'MEHADIA': ['Mehadia', 241],
  'DOBRETA': ['Dobreta', 242]
}

actions = {
  'GOTOARAD': 'go-to-arad',
  'GOTOSIBIU': 'go-to-sibiu',
  'GOTOTIMISUARA': 'go-to-timisuara',
  'GOTOZERIND': 'go-to-zerind',
  'GOTOFAGARAS': 'go-to-fagaras',
  'GOTOORADEA': 'go-to-radea',
  'GOTORIMNICU': 'go-to-rimnicu',
  'GOTOPITESTI': 'go-to-pitesti',
  'GOTOCRAIOVA': 'go-to-craiova',
  'GOTOBUCHAREST': 'go-to-bucharest',
  'GOTOLUGOJ': 'go-to-lugoj',
  'GOTOMEHADIA': 'go-to-mehadia',
  'GOTODOBRETA': 'go-to-dobreta',
}

class AStar:
  def __init__(self, local, distance=0):
    self.local = local
    self.distance = distance
  
  def getActions(self):
    list = []
    
    if (self.local == city['ARAD']):
      list.append(actions["GOTOSIBIU"])
      list.append(actions["GOTOTIMISUARA"])
      list.append(actions["GOTOZERIND"])

    elif (self.local == city["ZERIND"]):
      list.append(actions["GOTOARAD"])
      list.append(actions["GOTOORADEA"])

    elif (self.local == city["TIMISUARA"]):
      list.append(actions["GOTOARAD"])
      list.append(actions["GOTOLUGOJ"])

    elif (self.local == city["SIBIU"]):
      list.append(actions["GOTOARAD"])
      list.append(actions["GOTOFAGARAS"])
      list.append(actions["GOTOORADEA"])
      list.append(actions["GOTORIMNICU"])

    elif (self.local == city["ORADEA"]):
      list.append(actions["GOTOZERIND"])
      list.append(actions["GOTOSIBIU"])

    elif (self.local == city["FAGARAS"]):
      list.append(actions["GOTOSIBIU"])
      list.append(actions["GOTOBUCHAREST"])

    elif (self.local == city["RIMNICU"]):
      list.append(actions["GOTOSIBIU"])
      list.append(actions["GOTOPITESTI"])
      list.append(actions["GOTOCRAIOVA"])

    elif (self.local == city["PITESTI"]):
      list.append(actions["GOTORIMNICU"])
      list.append(actions["GOTOBUCHAREST"])
      list.append(actions["GOTOCRAIOVA"])

    elif (self.local == city["CRAIOVA"]):
      list.append(actions["GOTORIMNICU"])
      list.append(actions["GOTOPITESTI"])
      list.append(actions["GOTODOBRETA"])

    elif (self.local == city["LUGOJ"]):
      list.append(actions["GOTOTIMISUARA"])
      list.append(actions["GOTOMEHADIA"])

    elif (self.local == city["MEHADIA"]):
      list.append(actions["GOTOLUGOJ"])
      list.append(actions["GOTODOBRETA"])

    elif (self.local == city["DOBRETA"]):
      list.append(actions["GOTOCRAIOVA"])
      list.append(actions["GOTOMEHADIA"])

    return list

  def doAction(self, action):    
    state = self.clone()

    if (action == actions["GOTOARAD"]):
      if(state.local == city["SIBIU"]):
        state.distance = 140
      elif(state.local == city["TIMISUARA"]):
        state.distance = 118
      elif(state.local == city["ZERIND"]):
        state.distance = 75

      state.local = city["ARAD"]

    elif (action == actions["GOTOSIBIU"]):
      if(state.local == city["ARAD"]):
        state.distance = 140
      elif(state.local == city["ORADEA"]):
        state.distance = 151
      elif(state.local == city["FAGARAS"]):
        state.distance = 99
      elif(state.local == city["RIMNICU"]):
        state.distance = 80

      state.local = city["SIBIU"]

    elif (action == actions["GOTOTIMISUARA"]):
      if(state.local == city["ARAD"]):
        state.distance = 118
      elif(state.local == city["LUGOJ"]):
        state.distance = 111
      
      state.local = city["TIMISUARA"]

    elif (action == actions["GOTOZERIND"]):
      if(state.local == city["ARAD"]):
        state.distance = 75
      elif(state.local == city["ORADEA"]):
        state.distance = 71
      
      state.local = city["ZERIND"]

    elif (action == actions["GOTOFAGARAS"]):
      if(state.local == city["SIBIU"]):
        state.distance = 99
      
      state.local = city["FAGARAS"]

    elif (action == actions["GOTOORADEA"]):
      if(state.local == city["SIBIU"]):
        state.distance = 151
      elif(state.local == city["ZERIND"]):
        state.distance = 71
      
      state.local = city["ORADEA"]

    elif (action == actions["GOTORIMNICU"]):
      if(state.local == city["SIBIU"]):
        state.distance = 80

      state.local = city["RIMNICU"]

    elif (action == actions["GOTOPITESTI"]):
      if(state.local == city["RIMNICU"]):
        state.distance = 97
      
      state.local = city["PITESTI"]

    elif (action == actions["GOTOCRAIOVA"]):
      if(state.local == city["RIMNICU"]):
        state.distance = 146

      state.local = city["CRAIOVA"]

    elif (action == actions["GOTOBUCHAREST"]):
      if(state.local == city["FAGARAS"]):
        state.distance = 211
      
      state.local = city["BUCHAREST"]

    elif (action == actions["GOTOLUGOJ"]):
      if(state.local == city["TIMISUARA"]):
        state.distance = 111

      state.local = city["LUGOJ"]

    elif (action == actions["GOTOMEHADIA"]):
      if(state.local == city["LUGOJ"]):
        state.distance = 70

      state.local = city["MEHADIA"]

    elif (action == actions["GOTODOBRETA"]):
      
      state.local = city["DOBRETA"]
    
    return state

  def clone(self):
    return AStar(self.local)

  def equals(self, o):
    return o.local == self.local

  def __str__(self):
    return 'City: {}'.format(self.local)

initial = AStar(city["ARAD"])

finals = [
  AStar(city["BUCHAREST"])
]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms["DSF"])

if (result):
  for i in result:
    print(i)