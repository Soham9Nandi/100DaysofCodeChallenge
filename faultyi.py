class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for letter in s:
            if letter == 'i':
                stack.reverse()
            else:
                stack.append(letter)
        return ''.join(stack)
