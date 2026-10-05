# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

While completing this assignment, I learned how to effectively model relationships—like a regional train network—using adjacency lists via Python dictionaries. I also practiced using the collections.deque module, which is vital because popping from the front of a standard Python list is an O(N) operation, whereas deque provides an efficient O(1) queue structure necessary for BFS.

A challenge I encountered was preventing infinite loops during traversal. If two cities pointed to each other (e.g., Seattle <-> Portland), the algorithm would bounce between them indefinitely. I overcame this by implementing a visited Set to track processed nodes in O(1) time, ensuring nodes are only added to the queue if they haven't been seen before.

Conceptually, BFS and DFS (Depth-First Search) are opposites. BFS uses a First-In-First-Out (FIFO) queue to explore broadly, making it the perfect algorithm for finding the shortest path on an unweighted graph (e.g., GPS routing or finding the closest connection on LinkedIn). Conversely, DFS uses a Last-In-First-Out (LIFO) stack to explore as deeply as possible before backtracking. DFS is better suited for tasks that require exploring all possibilities to the end, such as solving a maze or evaluating game-tree moves in artificial intelligence.