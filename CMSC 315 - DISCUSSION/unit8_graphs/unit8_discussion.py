"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # Handle the edge case where the start node doesn't exist in the graph
    if start not in graph:
        return []

    # Track visited nodes using a Set for O(1) lookup time to prevent revisiting nodes
    visited = set()

    # Why a queue is used:
    # A queue follows First-In-First-Out (FIFO) logic. This ensures that nodes discovered
    # first are processed first, which naturally creates a level-by-level traversal.
    queue = deque([start])

    # Track the order of nodes we actually process to return at the end
    traversal_order = []

    # Mark the start node as visited immediately so it isn't added again
    visited.add(start)

    while queue:
        # Pop the oldest node from the front of the queue
        current_node = queue.popleft()
        traversal_order.append(current_node)

        # Why neighbors are added to the queue:
        # We look at all direct connections (neighbors) of the current node. By adding
        # unvisited neighbors to the back of the queue, we ensure they are processed
        # only *after* all currently discovered nodes in the current level are finished.
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # How BFS differs from depth-first traversal (DFS):
    # BFS explores broadly, scanning all immediate neighbors (level 1) before moving
    # deeper to the neighbors' neighbors (level 2). It uses a Queue.
    # DFS explores deeply, following a single path down to its very end before
    # backtracking to check other paths. It uses a Stack (or recursion).

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Real-world Example: A regional train network.
    # Nodes represent Cities (train stations).
    # Edges represent direct train routes connecting the cities.
    train_network = {
        'Seattle': ['Portland', 'Boise'],
        'Portland': ['Seattle', 'Sacramento'],
        'Boise': ['Seattle', 'Salt Lake City'],
        'Sacramento': ['Portland', 'San Francisco', 'Salt Lake City'],
        'San Francisco': ['Sacramento', 'Los Angeles'],
        'Salt Lake City': ['Boise', 'Sacramento', 'Las Vegas'],
        'Las Vegas': ['Salt Lake City', 'Los Angeles'],
        'Los Angeles': ['San Francisco', 'Las Vegas']
    }

    print("Regional Train Network (Adjacency List):")
    for city, connections in train_network.items():
        print(f"  {city} connects to -> {connections}")


    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    start_city = 'Seattle'
    print(f"Starting BFS Traversal from: {start_city}")

    # Explaining the level-by-level traversal:
    # Level 0: Seattle
    # Level 1 (Neighbors of Seattle): Portland, Boise
    # Level 2 (Neighbors of Level 1): Sacramento, Salt Lake City
    # Level 3 (Neighbors of Level 2): San Francisco, Las Vegas
    # Level 4 (Neighbors of Level 3): Los Angeles
    traversal_result = bfs(train_network, start_city)
    print(f"Traversal Order: {traversal_result}")

    print("\nAdding a new city (Denver) and connecting it to Salt Lake City...")
    # Adding a new node and edge
    train_network['Denver'] = ['Salt Lake City']
    train_network['Salt Lake City'].append('Denver')

    updated_traversal = bfs(train_network, start_city)
    print(f"Updated Traversal Order: {updated_traversal}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Start node is not in the graph
    print("\nEdge Case 1: Missing Start Node Safely")
    print("Attempting to traverse starting from 'Miami' (not in network).")
    missing_node_result = bfs(train_network, 'Miami')
    print(f"Result: {missing_node_result}")
    print("Explanation: The 'if start not in graph' check safely catches this, returning an empty list rather than throwing a KeyError.")

    # Edge Case 2: Disconnected Graph
    print("\nEdge Case 2: Disconnected Graph")
    disconnected_graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'], # C and D are isolated from A and B
        'D': ['C']
    }
    print(f"Graph: {disconnected_graph}")
    print("Starting traversal from 'A'...")
    disconnected_result = bfs(disconnected_graph, 'A')
    print(f"Result: {disconnected_result}")
    print("Explanation: BFS only visits nodes reachable from the starting point. It visits 'A' and 'B', but the queue empties before it can reach 'C' or 'D', demonstrating that standard BFS doesn't automatically map disjointed sub-graphs.")


if __name__ == "__main__":
    main()