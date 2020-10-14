class CandidateState:
  def __init__(self, state, parent=None, action=None):
    self.state = state
    self.parent = parent
    self.action = action
    self.children = []

  def getSuccessors(self):
    actions = self.state.getActions()
    successors = []

    for action in actions:
      state = self.state.doAction(action)

      success = CandidateState(state, self, action)
      self.children.append(success)

      successors.append(success)

    return successors

  def __str__(self):
    if(self.action):
      return '{} > {} '.format(self.action, self.state)

    else:
      return 'start > {} '.format(self.state)