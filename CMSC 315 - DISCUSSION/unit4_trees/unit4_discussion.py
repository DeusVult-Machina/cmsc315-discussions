"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Implementation: Initialize the node with the given value
        # and set left and right to None as it's a leaf node initially.
        self.value = value
        self.left = None
        self.right = None
        pass


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # Implementation: root is initially None to signify an empty tree.
        self.root = None
        pass

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # A BST is ordered by definition. We compare the new value to the current node
        # to decide which (left for smaller, right for larger) to follow,
        # maintaining the sort of the tree.
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)
        pass

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: if we hit a dead end, create the new node here.
        if node is None:
            return Node(value)

        # Recursive step: traverse left if smaller, right if larger.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Return the current node to re-link the tree as the call stack unwinds.
        return node
        pass

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is efficient because it eliminates half of the remaining
        # search space with every comparison (O(log n) time complexity on average),
        # unlike a linear search which must check every single item (O(n) time).
        return self._search_recursive(self.root, value)
        pass

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        if node is None:
            return False
        if node.value == value:
            return True
        # Base cases: node is not found, or node is found.
        # Recursive step: search left if target is smaller, right if larger.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

        pass

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values
        pass

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # In-order traversal visits nodes in ascending order because
        # it exhaustively processes all smaller elements (left subtree)
        # before recording the current node, and then processes all
        # larger elements (right subtree).
        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)
        pass


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # 1. Create a BST object
    tree = BST()

    # 2 & 3. Insert 7 values routing left and right
    insert_values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {insert_values}")
    for val in insert_values:
        tree.insert(val)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # 1 & 2. Perform and display
    sorted_values = tree.inorder()
    print(f"In-order traversal output: {sorted_values}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # 1. Search for existing values
    print(f"Searching for 40 (Exists): {tree.search(40)}")
    print(f"Searching for 80 (Exists): {tree.search(80)}")

    # 2. Search for non-existing values
    print(f"Searching for 15 (Does not exist): {tree.search(15)}")
    print(f"Searching for 99 (Does not exist): {tree.search(99)}")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Edge Case: Searching and Traversing an empty tree
    empty_tree = BST()
    print(f"Traversing an empty tree: {empty_tree.inorder()}")
    print(f"Searching an empty tree for 50: {empty_tree.search(50)}")

if __name__ == "__main__":
    main()