from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

positions = {
  "ROOM1": 'room1',
  "ROOM2": 'room2',
  "ROOM3": 'room3'
}

states = {
  "DIRTY": 'dirty',
  "CLEAN": 'clean'
}

actions = {
  "GOTOROOM1": 'go-to-room-1',
  "GOTOROOM2": 'go-to-room-2',
  "GOTOROOM3": 'go-to-room-3',
  "CLEAR": 'clear-room'
}

class VacuumCleanerWorld:
  def __init__(self, vacuumPosition, room1State, room2State, room3State):
    self.vacuumPosition = vacuumPosition
    self.room1State = room1State
    self.room2State = room2State
    self.room3State = room3State

  def getActions(self):
    list = []

    if (self.vacuumPosition == positions["ROOM1"]):
      
      if (self.room1State == states["DIRTY"]):
        list.append(actions["CLEAR"])

      list.append(actions["GOTOROOM2"])

    elif (self.vacuumPosition == positions["ROOM2"]):

      if (self.room2State == states["DIRTY"]):
        list.append(actions["CLEAR"])

      list.append(actions["GOTOROOM1"])
      list.append(actions["GOTOROOM3"])

    else:
      if (self.room3State == states["DIRTY"]):
        list.append(actions["CLEAR"])
      list.append(actions["GOTOROOM2"])

    return list
  
  def doAction(self, action):   

    state = self.clone()

    if (action == actions["GOTOROOM1"]):
      state.vacuumPosition = positions["ROOM1"]

    elif (action == actions["GOTOROOM2"]):
      state.vacuumPosition = positions["ROOM2"]

    elif (action == actions["GOTOROOM3"]):
      state.vacuumPosition = positions["ROOM3"]

    elif (action == actions["CLEAR"]):

      if (self.vacuumPosition == positions["ROOM1"]):
        state.room1State = states["CLEAN"]

      elif (self.vacuumPosition == positions["ROOM2"]):
        state.room2State = states["CLEAN"]

      else:
        state.room3State = states["CLEAN"]
    
    return state

  def clone(self):
    return VacuumCleanerWorld(self.vacuumPosition, self.room1State, self.room2State, self.room3State)

  def equals(self, o):
    return o.vacuumPosition == self.vacuumPosition and o.room1State == self.room1State and o.room2State == self.room2State and o.room3State == self.room3State

  def __str__(self):
    return '[{}, {}, {}, {}]'.format(self.vacuumPosition, self.room1State, self.room2State, self.room3State)

initial = VacuumCleanerWorld(positions["ROOM1"], states["DIRTY"], states["DIRTY"], states["DIRTY"])

finals = [
  VacuumCleanerWorld(positions["ROOM1"], states["CLEAN"], states["CLEAN"], states["CLEAN"]),
  VacuumCleanerWorld(positions["ROOM2"], states["CLEAN"], states["CLEAN"], states["CLEAN"]),
  VacuumCleanerWorld(positions["ROOM3"], states["CLEAN"], states["CLEAN"], states["CLEAN"])
]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms["DSF"])

if (result):
  for i in result:
    print(i)