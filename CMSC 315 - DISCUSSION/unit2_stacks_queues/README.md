# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
 - Used a standard Python list, utilizing append() and pop() methods to manage the internal data.
2. Implement queue operations.
- Utilized Python's collections.deque module for efficient management while using append() and popleft().
3. Demonstrate LIFO behavior.
- Used a while loop to pop items off the stack, successfully showing that the most recently added items were the first to be removed.
4. Demonstrate FIFO behavior.
- Used a while loop to dequeue items, successfully showing that the oldest items in the queue were the first to be accessed.
5. Create and test edge cases.
- Implemented conditional checks (is_empty()) to return friendly string error messages rather than throwing exceptions when attempting to remove or peek at items. Also verified that single-item structures properly reported as empty once the final item was removed.
6. Create a real-world scenario.
- Strategy games like Stellaris or Civilization use this time of queue when setting up a build queue where the first one ordered is the first completed. 

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
