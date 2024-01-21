import heapq


def dijkstra(graph, start):
    """
    This function implements Dijkstra's algorithm to find the shortest path from the start node to all other nodes in the graph.

    Parameters:
    graph (dict): A dictionary containing nodes as keys and lists of adjacent nodes as values.
    start (str): The starting node for the algorithm.

    Returns:
    dict: A dictionary containing the shortest path from the start node to all other nodes.
    """

    # Initialize the priority queue and distances dictionary
    priority_queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while priority_queue:
        # Get the current shortest distance and corresponding node
        curr_distance, curr_node = heapq.heappop(priority_queue)

        # If we've already found a shorter path to this node, skip it
        if curr_distance > distances[curr_node]:
            continue

        # Update the distances to adjacent nodes
        for neighbor in graph[curr_node]:
            distance = curr_distance + 1

            # If we found a shorter path to the neighbor, update its distance and add it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Define the graph as a dictionary of nodes and their adjacent nodes
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Add the edge weights as a dictionary of tuples representing the edges and their weights
edges = {
    ('A', 'B'): 2,
    ('A', 'C'): 1,
    ('B', 'A'): 2,
    ('B', 'D'): 4,
    ('B', 'E'): 1,
    ('C', 'A'): 1,
    ('C', 'F'): 5,
    ('D', 'B'): 4,
    ('E', 'B'): 1,
    ('E', 'F'): 3,
    ('F', 'C'): 5,
    ('F', 'E'): 3
}

# Run Dijkstra's algorithm on the graph starting from node 'A'
distances = dijkstra(graph, 'A')

# Print the shortest path from node 'A' to all other nodes
print(distances)