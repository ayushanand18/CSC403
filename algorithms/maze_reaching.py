"""
Maze Reaching between two points of the graph using DFS.
"""
import typing

class Graph(object):
    """
    Define the graph object

    Graph.E: Edges
    Graph.V: Vertices
    Graph.nodes: Number of nodes
    """
    def __init__(self, edges: list, vertices: list)->typing.Self:
        """Initialise the Edges and Vertices"""
        self.E = edges
        self.V = vertices

edges = [
    [1,2],
    [2,3],
    [3,4],
    [3,7],
    [4,7],
    [4,5],
    [5,9],
    [5,8],
    [5,6],
    [7,6],
    [9,10],
    [10,11],
    [19,13],
    [13,14],
    [14,15],
    [12,13],
    [6,12],
    [6,17],
    [6,16],
    [13,16],
    [17,25],
    [7,19],
    [7,18],
    [19,20],
    [18,23],
    [23,22],
    [22,21],
    [21,24],
    [24,26],
    [24,27],
    [27,28],
    [28,29],
    [29,30],
]
vertices = list(range(1,31))

maze = Graph(edges, vertices)

def dfs(adjacency_list: dict, visited: list, path: list, start: int, target: int)-> bool:
    # if the current node matches target, we return True
    if start==target:
        path.append(target)
        return True
    # if we have already explored this node before, return False
    if start in visited:
        return False
    # add this need to explored
    visited.append(start)
    # find possible path for each neighbor of start
    for neighbor in adjacency_list[start]:
        val = dfs(adjacency_list, visited, path, neighbor, target)
        if(val):
            path.append(start)
            return True
    return False

def solve_maze(maze: Graph, source: int, dest: int) -> list:
    """
    Solves Maze Problem (using graph).
    """
    # intialize path as empty list
    path = []
    # intialize the empty dictionary as adjacency_list
    adjacency_list = dict()
    # prepare the adjacency_list
    for edge in maze.E:
        if edge[0] in adjacency_list:
            adjacency_list[edge[0]].append(edge[1])
        else:
            adjacency_list[edge[0]] = [edge[1]]
        if edge[1] in adjacency_list:
            adjacency_list[edge[1]].append(edge[0])
        else:
            adjacency_list[edge[1]] = [edge[0]]
    # prepare list of visited nodes
    visited = []
    # Do the traversal and simulataneously print if the search was successfull
    print(dfs(adjacency_list, visited, path, source, dest))
    # reverse the pathj at the endbecause we added last elements in the path
    # first, and the starting elements later when the recursion falls down
    path.reverse()
    return path

print(solve_maze(maze, 1, 30))