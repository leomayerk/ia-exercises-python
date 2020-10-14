from CandidateState import CandidateState

algorithms = {
  "DSF": 'dsf',
  "BSF": 'bsf'
}

class UninformedSearch:
  def __init__(self, initialState, finalStates):
    self.initialState = initialState
    self.finalStates = finalStates

  def find(self, index, list):
    isEqual = False

    for i in list:
      if i.equals(index):
        isEqual = True

    return isEqual

  def search(self, type):
    visited = []

    candidate = CandidateState(self.initialState)
    pending = [ candidate ]

    i = 0
    count = 0

    while len(pending) != 0:
      candidate = pending.pop(0) if type == algorithms['DSF'] else pending.pop()
      i += 1

      if (i % 1000 == 0):
        print(i)

      if (self.find(candidate.state, self.finalStates)):
        result = []

        while (candidate):
          result.append(candidate)
          candidate = candidate.parent

        result.reverse()

        return result

      else:
        visited.append(candidate.state)

        successors = candidate.getSuccessors()  
        
        for successor in successors:
          if not self.find(successor.state, visited):
            pending.append(successor)
      
      count += 1

    return None
