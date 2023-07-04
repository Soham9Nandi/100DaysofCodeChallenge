class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) == 2:
            if goal == s[::-1]:
                return True
            else:
                return False
        else:
            flag = 0
            change = []
            for i in range(0,len(s)):
                if s[i] != goal[i]:
                    flag +=1
                    change.append(i)      
            if flag>2 or flag ==1:
                return False
            elif flag == 2:
                if s[change[0]] == goal[change[1]] and s[change[1]] == goal[change[0]]:
                    return True
                else:
                    return False
            else:
                l = list(s)
                m = set(l)
                if len(l) == len(m):
                    return False
                else:
                    return True 
        
