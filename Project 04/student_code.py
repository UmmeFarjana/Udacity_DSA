def shortest_path(M,start,goal):
    print("shortest path called")
    return
import math
import heapq
from helpers import Map, load_map, show_map


def shortest_path(M, start, goal):
    print("Getting shortest path...")
    
    # Tracking of costs
    current_cost = {}
    current_cost[start] = 0
    
    # Already explored areas at the current state
    explored = {}
    explored[start] = None
    # Frontiers at the current state
    frontiers = [(0, start)]

    while len(frontiers) > 0:
        
        # node with minimum cost at the current frontiers
        node = heapq.heappop(frontiers)[1]
        
        # Check if already reached at the goal
        if node == goal:
            break
            
        # Otherwise, continue searching
        for neighbor in M.roads[node]:
            
            # Compute costs
            path_cost = distance(M.intersections[node], M.intersections[neighbor]) # g(path)
            estimated_distance_to_goal = current_cost[node] # h(s)
            new_cost = path_cost + estimated_distance_to_goal # f = g(path) + h(s)
            
            # Check if
            # 1) node/neighbor is not visited, OR
            # 2) distance of the node from the starting node is less than the distance stored previously for this node
            # Then update cost, explored and frontiers
            if neighbor not in explored or new_cost < current_cost[neighbor]:
                explored[neighbor] = node
                current_cost[neighbor] = new_cost
                heapq.heappush(frontiers, (new_cost, neighbor))
                
    # Get the best route based on the explored nodes
    return best_route(explored, start, goal)


def distance(source, destination):
    '''Euclidean distance between two points'''
    return math.sqrt( (destination[0]-source[0])**2 + (destination[1]-source[1])**2 )


def best_route(explored, start, goal):
    '''Get the best route based on the explored nodes.
    From goal to start and then reverse the path.
    '''
    # Check if goal/destination exists in the map.
    if goal not in explored:
        print(f"Destination: {node} does not exist in the map.")
        return
    
    node = goal
    path = []
        
    # Accumulate the paths
    while node != start:
        path.append(node)
        node = explored[node]
    path.append(start)
    path = path[::-1]
    for stop in path[:-1]:
        print(stop, end='-->')
    print(path[-1])
        
    return path