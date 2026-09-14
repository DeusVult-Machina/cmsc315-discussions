# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

While completing this assignment, I implemented linear search and binary search algorithms and analyzed their respective efficiencies across varying data parameters. I learned how to compare algorithmic performance practically by testing them against small, large, and empty datasets to identify execution behavior. A primary challenge I encountered was managing the internal indices (low and high) accurately during the binary search loop. If the index adjustments (+ 1 or - 1) were neglected, the search loop would iterate infinitely on non-existent values. I overcame this by methodically tracing the logic for edge cases like single-item lists to guarantee loop termination. 
In real-world scenarios, a linear search is most appropriate when querying small or fundamentally unsorted data arrays, as the initial computing overhead of sorting the dataset would outweigh the time saved by a faster search approach. Alternatively, binary search should always be implemented for large datasets that are already sorted (such as relational database indexes or alphabetical directories). By systematically halving the valid search space with every passing iteration, binary search ensures $O(\log n)$ performance, preventing operations from causing system lag even if the list scales to millions of data records.