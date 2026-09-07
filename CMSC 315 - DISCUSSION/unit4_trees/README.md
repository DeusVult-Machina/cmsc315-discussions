# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

I learned how to build and navigate a Binary Search Tree using recursive methods. Implementing the insertion, search, and in-order traversal functions practically reinforced my understanding of tree data structure architecture. The primary challenge I encountered was correctly managing recursive base cases and node assignments when building the tree dynamically. I overcame this by writing out and tracing the execution path, which helped me visualize how the insert_recursive function properly updates and returns node references up the call stack to link parent and child nodes.
A Binary Search Tree dictates that values smaller than the current node are stored to the left, and larger values are stored to the right. This ordering creates massive efficiency compared to linear data structures like standard arrays. Instead of checking every single element sequentially, a balanced BST divides the search space in half at each step. This allows for rapid logarithmic data retrieval, making sorting and searching extraordinarily efficient as the dataset grows.