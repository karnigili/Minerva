# from PIL import Image
import numpy as np
import heapq
from scipy import ndimage
from itertools import product, starmap


def heuristic(a, b):
   # geometric distance
   return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**.5


def get_neighbors (node, size):
    # finds all neighbors for the given node in resepct to the array size
    cell_x = node[0]
    cell_y = node[1]

    neighbors_array = []

    for x in range(cell_x-1, cell_x+2):
        for y in range(cell_y-1, cell_y+2):
            if (
                -1 < cell_x <= size-1 and 
                -1 < cell_x <= size-1 and 
                (cell_x != x or size != y) and
                (0 <= x <= size-1) and 
                (0 <= y <= size-1) and 
                (x != cell_x or y != cell_y)
                ):
                neighbors_array.append((x,y))

    return neighbors_array
  

def a_star (start, goal, graph):
    # finds the shortest way from the start to the goal based on the a* algorithm
    # return visited: all the nodes that were checked by the algorithm , the cheapest price for the goal

    # a queue of location to look at, prioritized using a heap
    to_search = [(start, None)] # (next, heuristic_cost)
    heapq.heapify(to_search)

    # keeps track of all nodes that have been looked into 
    visited = {} # current : previous

    # keeps track of the total movement cost from the start location
    agg_cost = {} # {current : cost} 

    # initial values 
    visited[start] = None  # from None to start
    agg_cost[start] = 0 # cost to start is 0


    while to_search:

        # checks the lowest cost node
        current = heapq.heappop(to_search)

        # stopping condition 
        if current[0] == goal:
            break

        neighbors = get_neighbors(current[0], len(graph))

        for potential_next in neighbors:
            
            # the saved current cost + the potential added cost
            potential_next_cost = agg_cost[current[0]] + graph[potential_next[0]][potential_next[1]]

            # compares with visited nodes and the potential cost of the next step with its saved one (did we find a cheaper way?)
            if potential_next not in agg_cost or potential_next_cost < agg_cost[potential_next]:

                # uses heuristics to choose assign cost
                agg_cost[potential_next] = potential_next_cost
                cost = potential_next_cost + heuristic(goal, potential_next)

                # adds to the to_search queue and to the visited nodes
                heapq.heappush(to_search, (potential_next, cost))
                visited[potential_next] = current[0]

    return {'visited': visited, 'cost':agg_cost[goal]}


def print_shortest_path(start, goal, a_dict):
    # print the result of the a* algorithm

    path = []

    current = goal

    while current != None:

        path.append(current)

        current = a_dict['visited'][current]


    return {'path':path[::-1], 'cost':a_dict['cost']}


##################
rand = np.random.rand(800,800)


# 50: 2
# 100: 
# 200:15
# 300: 27
# 400: 52
# 500: 87
# 600: 100
# 800 : 

# graph_example = [[2,3,4],[6,15,7],[5,4,3]]
s,e =(0,0),(748,745)

t = a_star(s,e , rand)

print print_shortest_path(s, e , t)
