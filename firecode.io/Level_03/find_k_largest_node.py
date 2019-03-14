# Find the kth Largest Node in a BST

class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:

    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    # Helper Method
    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_largest(self, root, k):
        if root == None:
            return None

        size_right_child = self.size(root.right_child)
        if size_right_child > k:
            return self.find_kth_largest(root.right_child, k)

        if size_right_child + 1 == k:
            return root

        if size_right_child + 1 < k:
            return self.find_kth_largest(root.left_child, k - size_right_child - 1)


if __name__ == '__main__':
    l2 = TreeNode(5)
    r2 = TreeNode(10)
    r1 = TreeNode(8, l2, r2)
    l1 = TreeNode(2)
    root = TreeNode(4, l1, r1)
    print(BinaryTree().size(root))
    print(BinaryTree().find_kth_largest(root, 2))
    print("-" * 25)

    l2 = TreeNode(5)
    r1 = TreeNode(4)
    r1.right_child = l2
    l3 = TreeNode(1)
    l1 = TreeNode(2, l3)
    root = TreeNode(3, l1, r1)
    print(BinaryTree().size(root))
    print(BinaryTree().find_kth_largest(root, 2))
    print("-" * 25)
