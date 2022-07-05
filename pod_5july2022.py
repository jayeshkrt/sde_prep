#https://practice.geeksforgeeks.org/problems/count-bst-nodes-that-lie-in-a-given-range/1# 

class Solution:
    def getCount(self, root, low, high):
        count = 0
        def helper(root, l, h, c):
            if not root:
                return None

            left = helper(root.left, l, h, c)
            ryt = helper(root.right, l, h, c)
            if l <= root.data <= h:
                return left + ryt + 1
            else:
                return ryt+left
        return helper(root, low, high, count)
