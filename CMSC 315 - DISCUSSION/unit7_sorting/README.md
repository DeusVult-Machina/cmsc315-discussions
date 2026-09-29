# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

While completing this assignment, I solidified my understanding of iterative versus recursive problem-solving. Implementing the divide-and-conquer logic of Merge Sort required tracking how Python slices lists and processes call stacks. A challenge I encountered was within the `merge` helper function; initially, I forgot to account for appending the "leftover" elements when one half of the divided list was exhausted before the other. I resolved this by adding two `while` loops at the end of the method to safely sweep up any remaining values.

When comparing the two, efficiency tradeoffs become obvious. Bubble Sort has an average time complexity of O(N²), making it highly inefficient for large datasets due to its nested loops. However, it boasts O(1) space complexity, meaning it sorts in place and uses very little memory. It is also adaptive—if the list is already sorted, it exits in O(N) time. Conversely, Merge Sort consistently performs at O(N log N) regardless of the starting data, making it highly scalable and reliable for massive datasets. The tradeoff is space; Merge Sort requires O(N) auxiliary space to construct the separated sub-lists during the recursive splitting phase.