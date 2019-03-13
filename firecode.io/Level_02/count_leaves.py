# Count the leaves

class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root):
        if root == None:
            return 0
        if not root.left_child and not root.right_child:
            return 1

        return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)


if __name__ == '__main__':
    l4 = TreeNode(8)
    r4 = TreeNode(9)
    l3 = TreeNode(6, l4, r4)
    r3 = TreeNode(7)
    l2 = TreeNode(4)
    r2 = TreeNode(5)
    l1 = TreeNode(2, l2, r2)
    r1 = TreeNode(3, l3, r3)
    root = TreeNode(1, l1, r1)

    bTree = BinaryTree()
    print(bTree.number_of_leaves(root))
