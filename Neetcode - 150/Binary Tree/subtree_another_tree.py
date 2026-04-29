from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def isSubtree(s, t):
            if not s:
                return False
            if isSameTree(s, t):
                return True
            return isSubtree(s.left, t) or isSubtree(s.right, t)

        return isSubtree(root, subRoot)


# Test 1: t is a subtree of s
s1 = TreeNode(3)
s1.left = TreeNode(4)
s1.right = TreeNode(5)
s1.left.left = TreeNode(1)
s1.left.right = TreeNode(2)

t1 = TreeNode(4)
t1.left = TreeNode(1)
t1.right = TreeNode(2)

print(Solution().isSubtree(s1, t1))   # True

# Test 2: t is NOT a subtree of s
s2 = TreeNode(3)
s2.left = TreeNode(4)
s2.right = TreeNode(5)
s2.left.left = TreeNode(1)
s2.left.right = TreeNode(2)
s2.left.right.left = TreeNode(0)

t2 = TreeNode(4)
t2.left = TreeNode(1)
t2.right = TreeNode(2)

print(Solution().isSubtree(s2, t2))   # False

# Test 3: both trees are identical
s3 = TreeNode(1)
s3.left = TreeNode(2)
s3.right = TreeNode(3)

t3 = TreeNode(1)
t3.left = TreeNode(2)
t3.right = TreeNode(3

print(Solution().isSubtree(s3, t3))   # True

# Test 4: subRoot is a single node
s4 = TreeNode(1)
s4.left = TreeNode(2)
s4.right = TreeNode(3)

t4 = TreeNode(2)

print(Solution().isSubtree(s4, t4))   # True

# Test 5: root is None
print(Solution().isSubtree(None, t4)) # False