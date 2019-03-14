# Number of Full Nodes in a Binary Tree

class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # Required collection modules have already been imported.
    def number_of_full_nodes(self, root):
        if not root or not root.left_child or not root.right_child:
            return 0

        return 1 + self.number_of_full_nodes(root.left_child) + self.number_of_full_nodes(root.right_child)


if __name__ == '__main__':
    l2 = TreeNode(5)
    r2 = TreeNode(10)
    r1 = TreeNode(8, l2, r2)
    l1 = TreeNode(2)
    root = TreeNode(4, l1, r1)
    print(BinaryTree().number_of_full_nodes(root))
    print("-" * 25)

    l2 = TreeNode(5)
    r1 = TreeNode(4)
    r1.right_child = l2
    l3 = TreeNode(1)
    l1 = TreeNode(2, l3)
    root = TreeNode(3, l1, r1)
    print(BinaryTree().number_of_full_nodes(root))
    print("-" * 25)

    a1 = TreeNode(8)
    a2 = TreeNode(9)
    a3 = TreeNode(4, a1, a2)
    a4 = TreeNode(5)
    a5 = TreeNode(2, a3, a4)
    a6 = TreeNode(6)
    a7 = TreeNode(7)
    a8 = TreeNode(3, a6, a7)
    root = TreeNode(1, a5, a8)
    print(BinaryTree().number_of_full_nodes(root))
    print("-" * 25)
