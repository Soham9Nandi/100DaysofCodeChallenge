class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        ans = 0
        for w in words:
            if set(w).issubset(set(allowed)):
               ans +=1
        return ans 
