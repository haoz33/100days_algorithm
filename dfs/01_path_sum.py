import re
from turtle import right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.current = 0

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        val = targetSum - root.val

        if val == 0 and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)


# If node is a leaf node, and current sum is equal to the target sum, return true
# How to determine if a node is leaf node?
# Node does not have any child


# What do I need to return when node is null?
# False

# How to keep track of current target value?
# pass down the targetSum-root.val
