# In a binary tree, we define a node "visible" when no node on the root-to-itself path (inclusive) has a greater value. The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.


import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree_node(root: Node) -> int:

    def dfs(root: Node, previous):
        if root is None:
            return 0

        total = 0
        if root.val >= previous:
            total += 1

        total += dfs(root.left, max(root.val, previous))
        total += dfs(root.right, max(root.val, previous))

        return total

    return dfs(root, float('-inf'))


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x':
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


root = build_tree(iter(input().split()), int)
res = visible_tree_node(root)
