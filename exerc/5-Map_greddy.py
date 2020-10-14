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

class Greddy:
  def __init__(self, local):
    self.local = local
  
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
      state.local = city["ARAD"]

    elif (action == actions["GOTOSIBIU"]):
      state.local = city["SIBIU"]

    elif (action == actions["GOTOTIMISUARA"]):
      state.local = city["TIMISUARA"]

    elif (action == actions["GOTOZERIND"]):
      state.local = city["ZERIND"]

    elif (action == actions["GOTOFAGARAS"]):
      state.local = city["FAGARAS"]

    elif (action == actions["GOTOORADEA"]):
      state.local = city["ORADEA"]

    elif (action == actions["GOTORIMNICU"]):
      state.local = city["RIMNICU"]

    elif (action == actions["GOTOPITESTI"]):
      state.local = city["PITESTI"]

    elif (action == actions["GOTOCRAIOVA"]):
      state.local = city["CRAIOVA"]      

    elif (action == actions["GOTOBUCHAREST"]):
      state.local = city["BUCHAREST"]

    elif (action == actions["GOTOLUGOJ"]):
      state.local = city["LUGOJ"]

    elif (action == actions["GOTOMEHADIA"]):
      state.local = city["MEHADIA"]

    elif (action == actions["GOTODOBRETA"]):
      state.local = city["DOBRETA"]
    
    return state

  def clone(self):
    return Greddy(self.local)

  def equals(self, o):
    return o.local == self.local

  def __str__(self):
    return 'City: {}'.format(self.local)

initial = Greddy(city["ARAD"])

finals = [
  Greddy(city["BUCHAREST"])
]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms["DSF"])

if (result):
  for i in result:
    print(i)