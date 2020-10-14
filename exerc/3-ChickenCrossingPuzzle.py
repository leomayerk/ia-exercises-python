from UninformedSearch import UninformedSearch
from UninformedSearch import algorithms

states = {
  'LEFT': 'left',
  'RIGHT': 'right'
}

actions = {
  'GOALONE': 'go-alone',
  'GOWITHFOX': 'go-with-fox',
  'GOWITHCHICKEN': 'go-with-chicken',
  'GOWITHCORN': 'go-with-corn',
  'COMEBACKALONE': 'come-back-alone',
  'COMEBACKWITHFOX': 'come-back-with-fox',
  'COMEBACKWITHCHICKEN': 'come-back-with-chicken',
  'COMEBACKWITHCORN': 'come-back-with-corn',    
}

class ChickenCrossingPuzzle:
  def __init__(self, farmerState, foxState, chickenState, cornState):
    self.farmerState = farmerState
    self.foxState = foxState
    self.chickenState = chickenState
    self.cornState = cornState
  
  def getActions(self):
    list = []

    if (self.farmerState == states['LEFT']):

      if ((self.foxState != self.chickenState) and (self.chickenState != self.cornState)):
        list.append(actions['GOALONE'])

      if ((self.foxState == states['LEFT']) and (self.chickenState != self.cornState)):
        list.append(actions['GOWITHFOX'])

      if (self.chickenState == states['LEFT']):
        list.append(actions['GOWITHCHICKEN'])

      if ((self.cornState == states['LEFT']) and (self.foxState != self.chickenState)):
        list.append(actions['GOWITHCORN'])

    else:
      if ((self.foxState != self.chickenState) and (self.chickenState != self.cornState)):
        list.append(actions['COMEBACKALONE'])

      if ((self.foxState == states['RIGHT']) and (self.chickenState != self.cornState)):
        list.append(actions['COMEBACKWITHFOX'])

      if (self.chickenState == states['RIGHT']):
        list.append(actions['COMEBACKWITHCHICKEN'])

      if ((self.cornState == states['RIGHT']) and (self.foxState != self.chickenState)):
        list.append(actions['COMEBACKWITHCORN'])
    
    return list
  
  def doAction(self, action):
    state = self.clone()

    if (action == actions['GOALONE']):
      state.farmerState = states['RIGHT']

    elif (action == actions['GOWITHFOX']):
      state.farmerState = states['RIGHT']
      state.foxState = states['RIGHT']

    elif (action == actions['GOWITHCHICKEN']):
      state.farmerState = states['RIGHT']
      state.chickenState = states['RIGHT']

    elif (action == actions['GOWITHCORN']):
      state.farmerState = states['RIGHT']
      state.cornState = states['RIGHT']

    elif (action == actions['COMEBACKALONE']):
      state.farmerState = states['LEFT']

    elif (action == actions['COMEBACKWITHFOX']):
      state.farmerState = states['LEFT']
      state.foxState = states['LEFT']

    elif (action == actions['COMEBACKWITHCHICKEN']):
      state.farmerState = states['LEFT']
      state.chickenState = states['LEFT']

    elif (action == actions['COMEBACKWITHCORN']):
      state.farmerState = states['LEFT']
      state.cornState = states['LEFT']
    
    return state

  def equals(self, o):
    return o.farmerState == self.farmerState and o.foxState == self.foxState and o.chickenState == self.chickenState and o.cornState == self.cornState

  def clone(self):
    return ChickenCrossingPuzzle(
      self.farmerState,
      self.foxState,
      self.chickenState,
      self.cornState)

  def __str__(self):
    return '[farmer={}, fox={}, chicken={}, corn={}]'.format(self.farmerState, self.foxState, self.chickenState, self.cornState)

initial = ChickenCrossingPuzzle(states['LEFT'], states['LEFT'], states['LEFT'], states['LEFT'])

finals = [ ChickenCrossingPuzzle(states['RIGHT'], states['RIGHT'], states['RIGHT'], states['RIGHT']) ]

problem = UninformedSearch(initial, finals)

result = problem.search(algorithms['DSF'])

if (result):
  for i in result:
    print(i)