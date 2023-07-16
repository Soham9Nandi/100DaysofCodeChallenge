class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for element in words:
            if set(element.lower()).issubset(set('qwertyuiop')) or set(element.lower()).issubset(set('asdfghjkl')) or set(element.lower()).issubset(set('zxcvbnm')):
                res.append(element)
        return res
