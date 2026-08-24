"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []
        pass

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # This supports LIFO behavior because the most recently appended
        self.items.append(value)
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # Empty-stack handling: Returns a friendly error message instead of throwing an IndexError.
        # What should happen if the stack is empty?
        # Removes and returns the most recently added value.
        if self.is_empty():
            return "Error: Cannot pop from an empty stack."
        return self.items.pop()
        pass

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Returns the top value without removing it so you can see what is next.
        if self.is_empty():
            return "Error: Cannot peek at an empty stack."
        return self.items[-1]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0
        pass


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # This supports FIFO behavior because items are added to the back
        self.items.append(value)
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Empty-queue handling: Returns a friendly error message to prevent crashes.
        if self.is_empty():
            return "Error: Cannot dequeue from an empty queue."
        return self.items.popleft()
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Returns the front value without removing it so you can check who is first in line.
        # Removes and returns the value from the front (left side) of the queue.
        if self.is_empty():
            return "Error: Cannot dequeue from an empty queue."
        return self.items[0]
        pass

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0
        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
my_stack = Stack()
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("Pushing 4 values onto the stack (10, 20, 30, 40)...")
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
print(f"Stack peek (should be 40): {my_stack.peek()}")
print("\nDemonstrating LIFO behavior (popping all items):")
while not my_stack.is_empty():
    print(f"Popped: {my_stack.pop()}")

print("      test popping from an empty stack,")

print(f"Popping from empty stack: {my_stack.pop()}")
print("      test peeking at an empty stack,")

print(f"Peeking at empty stack: {my_stack.peek()}")
print("      and verify a single-item stack becomes empty after removal.")
print("\nSingle-item stack test:")
single_stack = Stack()
single_stack.push(99)
print(f"Popped the single item: {single_stack.pop()}")
print(f"Is the stack empty now? {single_stack.is_empty()}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
my_queue = Queue()
print("Enqueueing 4 values into the queue ('A', 'B', 'C', 'D')...")
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
my_queue.enqueue('D')
print(f"Queue front (should be 'A'): {my_queue.front()}")
print("\nDemonstrating FIFO behavior (dequeuing all items):")
while not my_queue.is_empty():
    print(f"Dequeued: {my_queue.dequeue()}")
print("      test dequeuing from an empty queue,")
print(f"Dequeuing from empty queue: {my_queue.dequeue()}")
print("      test viewing the front of an empty queue,")
print(f"Viewing front of empty queue: {my_queue.front()}")
print("      and verify a single-item queue becomes empty after removal.")
single_queue = Queue()
single_queue.enqueue('Z')
print(f"Dequeued the single item: {single_queue.dequeue()}")
print(f"Is the queue empty now? {single_queue.is_empty()}")

if __name__ == "__main__":
    main()
