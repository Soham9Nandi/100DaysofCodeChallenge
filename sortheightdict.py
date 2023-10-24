class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = []
        for char in s:
            if char == 'I':
                ans.append(0)
            else:
                ans.append(1)
        return ans
