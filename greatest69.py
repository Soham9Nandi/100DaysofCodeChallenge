class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        if '6' in s:
            s[s.index('6')] = '9'
            return int(''.join(s))
        else:
            return num
