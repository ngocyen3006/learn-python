# Find the Diameter of a Binary Tree

class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def diameter(self, root):
        if not root:
            return 0
        right_height = self.height(root.right_child)
        left_height = self.height(root.left_child)

        left_diameter = self.diameter(root.left_child)
        right_diameter = self.diameter(root.right_child)

        return max(left_height + right_height + 1, max(left_diameter, right_diameter))

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left_child), self.height(root.right_child))


if __name__ == '__main__':
    root = TreeNode(20)
    root.left_child = TreeNode(15)
    root.right_child = TreeNode(30)
    r = BinaryTree()
    print(r.diameter(root))

    root = TreeNode(1)
    root.right_child = TreeNode(2)
    right_child = root.right_child
    r_c = TreeNode(3)
    right_child.right_child = r_c
    r = BinaryTree()
    print(r.diameter(root))
