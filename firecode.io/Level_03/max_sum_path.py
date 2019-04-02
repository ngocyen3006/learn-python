# Maximum Sum Path

class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # All the necessary collection moduled have been already imported.
    def max_sum_path(self, root):
        max_recursive_holder = [0]
        self.max_sum_path_main(root, max_recursive_holder)
        return max_recursive_holder[0]

    def max_sum_path_main(self, root, max_recursive_holder):
        if root == None:
            return 0
        left_sum = self.max_sum_path_main(root.left_child, max_recursive_holder)
        right_sum = self.max_sum_path_main(root.right_child, max_recursive_holder)

        node_cum_val = max(root.data + left_sum, root.data + right_sum)
        max_recursive_holder[0] = max(max_recursive_holder[0], left_sum + root.data + right_sum)
        return node_cum_val
