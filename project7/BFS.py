from routing import *
from copy import copy

def BadassFS(wire, graph, limit="+infinity"):
    #Initialiation
    initState = wire[0]
    print 'Starting vertex: ' + str(wire[0])
    goalState = wire[1]
    print 'Goal vertex: ' + str(goalState)
    runCount = 0
    frontier = [pathNode(initState)]
    explored = []

    #Execution, with run count for case of breakdown
    while runCount < limit:

        #Break when frontier is empty
        if frontier == []:
            print "can't find solution in frontier"
            return None
        current = frontier.pop(0)

        #Break if we hit the goal
        if current.v == goalState:
            #print 'Runcount = ' + runCount
            print 'HOUSTON, WE MADE IT. - Puzzle solved.'
            print 'moves to get there:'
            print current.path
            return current

        #Generate the NEW FRONTIER, MR. SPOCK
        else:
            #print 'CURRENT VERTEX: ' + str(current.v) +'\n\n'
            ls = graph.adj(current.v)
            for n in ls:
                if (n not in explored) and (graph.getVal(n) == 0 or n == goalState):
                    newNode = pathNode(n, current)
                    frontier.append(newNode)
           # print 'frontier size: ' + str(len(frontier))
            runCount += 1
        explored.append(current.v)
    print "Could't reach solution without surpassing Limit = " + str(limit)
    return None

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

class pathNode:
    def __init__(self, coord, parent=None, cost=0):
        self.v = coord
        self.p = parent
        if parent:
            self.cost = parent.cost + 1
        else:
            self.cost = cost
        self.path = self.returnPath()

    def returnPath(self):
        if self.p == None:
            return []
        else:
            return [self.v] + self.p.returnPath()
        
    def pathData(self):
        p = self.returnPath()
        return (p, self.cost)



def generateWires(grid, points):
    graph = Graph(grid)
    combinations = permutations(points)
    #Best Tuple contains a score and path
    bestTuple = (float("+infinity"), None)

    for sequence in combinations:
        #print sequence + '\n\n\n'
        g = copy(graph)
        score = 0
        paths = []
        wireIt = 0
        for wire in sequence:
            #print wire
            wireIt += 1
            path = BadassFS(wire, g)
            if path == None:
                return None
            score += path.cost
            paths.append(path.path)
            for move in path.path:
                graph.putVal(path.v, 1000+wireIt)
        if score < bestTuple[0]:
            bestTuple = (score, path.path)
        ##return the first one that works, because otherwise
        ##it'll take forever. Commment out, though. If you wish...
        return path.path
    ##real return statement that would take into account all
    ##permutations before executing. Ain't nobody got time for that.
    return bestTuple[1]
            
