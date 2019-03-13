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
    tree = TreeNode(1)
    tree = BinaryTree(tree)
    print(tree.number_of_leaves(1))
