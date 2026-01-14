class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def print_tree(self, tree_node):
        if tree_node is None:
            return

        print(tree_node.data)
        self.print_tree(tree_node.left)
        self.print_tree(tree_node.right)

testing_tree = BinaryTree()

node_b = TreeNode("B")
node_c = TreeNode("C")
node_a = TreeNode("A", node_b, node_c)

node_d = TreeNode("D")
node_e = TreeNode("E")

testing_tree.print_tree(node_a)

print("")

testing_tree.root = node_a
testing_tree.print_tree(testing_tree.root)

print("")

node_b.left = node_d
node_b.right = node_e

testing_tree.print_tree(node_b)

# 
#             A
#        /       \
#       B         C
#      / \       /  \
#     D   E   none   none
