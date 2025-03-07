# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    s= util.Stack() #use stack for DFS
    s.push((problem.getStartState(),[],[])) #First get the starting position
    while not s.isEmpty():
        pos,action,visited = s.pop()  # pop the last element and get the child position and action
        if problem.isGoalState(pos):
            return action  #if we find the goal then return the action

        for child, direction, steps in problem.getSuccessors(pos):
            if not child in visited: #make sure it doesn't go back to the previous position
                s.push((child, action + [direction], visited + [pos]))  # push child position, action and visited path in stack
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    q = util.Queue()    #use queue for BFS
    q.push((problem.getStartState(),[],[]))     #Get the starting position
    visited = []
    while not q.isEmpty():
        pos,action,num = q.pop()    #pop the last element and get the child position and actions
        if not pos in visited:       #can't go back in cornerproblem
            visited.append(pos)      #don't have duplicates in output so I use list
            if problem.isGoalState(pos):
                return action    #if pacman find the goal then return the path
            for child, direction, steps in problem.getSuccessors(pos):   #for each child push the child position, action
                q.push((child, action + [direction],num+[steps]))    #the last element doesn't matter it's ready for the priortity queue
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()    # Use Priority queue for UCS
    pq.push((problem.getStartState(), [], 0), 0)   #Set the Priority to and cost to 0 and also get the starting position
    expand = []

    while not pq.isEmpty():
        pos, action, num = pq.pop()     #pop the position, action and the cost to the position
        if not pos in expand:   #make sure that it doesn't go backward
            expand.append(pos)
            if problem.isGoalState(pos):
                return action   #if pacman find the goal then return the path
            for child, direction, cost in problem.getSuccessors(pos):     #for each child push the child position, action
                pq.push((child, action + [direction], num + cost), num + cost)  #the only difference is that we need consider about the cost for all the paths
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # This is the almost the same as UCS, The only difference it will be is that instead of
    # using the cost as a priority, we use heuristic + the cost as priority
    pq = util.PriorityQueue()   #use the priorityqueue for astar
    pq.push((problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem))   #get the start position and the heuristic
    expand = []   #this empty list is used for checking if the position is visited
    while not pq.isEmpty():
        pos, action, num = pq.pop()  #pop the next position, action and cost
        if not pos in expand:
            expand.append(pos)    #append the new position to the list
            if problem.isGoalState(pos):
                return action   #each time got to the next one, return the action
            for child, direction, cost in problem.getSuccessors(pos):
                pq.push((child, action + [direction], num + cost), num + cost + heuristic(child, problem))

    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
