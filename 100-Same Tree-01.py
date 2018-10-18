##Given two binary trees, write a function to check if they are the same or not.
##
##Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
##
##Example 1:
##
##Input:     1         1
##          / \       / \
##         2   3     2   3
##
##        [1,2,3],   [1,2,3]
##
##Output: true
##Example 2:
##
##Input:     1         1
##          /           \
##         2             2
##
##        [1,2],     [1,null,2]
##
##Output: false
##Example 3:
##
##Input:     1         1
##          / \       / \
##         2   1     1   2
##
##        [1,2,1],   [1,1,2]
##
##Output: false

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        ##递归算法，在函数内继续进行函数的递归，如果存在p和q，分层级遍历，先对比val也就是树杈处是否相等。
        ##然后再对左右两个分叉进行isSameTree的递归比较，因为有null树枝的存在所以不能单纯的对比p.left和q.left。
        ##最后全部一致或者全部null的情况下输出布尔值。这个function本身输出结果就是bool。所以用return
        if p and q:
            return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return p == q