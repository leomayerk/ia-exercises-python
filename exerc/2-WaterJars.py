from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

states = {
  'EMPTY': 0,
  'L1': 1,
  'L2': 2,
  'L3': 3,
  'L4': 4
}

actions = {
  'FILL1': 'fill-jar-1',
  'FILL2': 'fill-jar-2',
  'EMPTY1': 'empty-jar-1',
  'EMPTY2': 'empty-jar-2',
  'TRANSFER1TO2': 'transfer-jar-1-to-2',
  'TRANSFER2TO1': 'transfer-jar-2-to-1'
}

class WaterJars:
  def __init__(self, jar1State, jar2State):
    self.jar1State = jar1State
    self.jar2State = jar2State

  def getActions(self):
    list = []

    if (self.jar1State < 3):
      list.append(actions['FILL1'])
    
    if (self.jar1State > 0):
      list.append(actions['EMPTY1'])

      if (self.jar2State < 4):
        list.append(actions['TRANSFER1TO2'])
    
    if (self.jar2State < 4):
      list.append(actions['FILL2'])
    
    if (self.jar2State > 0):
      list.append(actions['EMPTY2'])

      if (self.jar1State < 3):
        list.append(actions['TRANSFER2TO1'])

    return list
  
  def doAction(self, action):
    state = self.clone()

    if (action == actions['EMPTY1']):
      state.jar1State = states['EMPTY']

    elif (action == actions['EMPTY2']):
      state.jar2State = states['EMPTY']

    elif (action == actions['FILL1']):
      state.jar1State = states['L3']

    elif (action == actions['FILL2']):
      state.jar2State = states['L4']

    elif (action == actions['TRANSFER1TO2']):
      transfer = min(state.jar1State, 4 - state.jar2State)

      state.jar1State -= transfer
      state.jar2State += transfer

    elif (action == actions['TRANSFER2TO1']):
      transfer = min(state.jar2State, 3 - state.jar1State)

      state.jar1State += transfer
      state.jar2State -= transfer
    
    return state

  def equals(self, o):
    return o.jar1State == self.jar1State and o.jar2State == self.jar2State

  def clone(self):
    return WaterJars(self.jar1State, self.jar2State)

  def __str__(self):
    return '[{}, {}]'.format(self.jar1State, self.jar2State)

initial = WaterJars(states['EMPTY'], states['EMPTY'])

finals = [
  WaterJars(states['EMPTY'], states['L2']),
  WaterJars(states['L1'], states['L2']),
  WaterJars(states['L2'], states['L2']),
  WaterJars(states['L3'], states['L2'])
]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms['DSF'])

if (result):
  for i in result:
    print(i)