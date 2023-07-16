class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {}
        res = []
        for element in list1:
            if element in list2:
                indexsum = list1.index(element)+list2.index(element)
                dic[element] = indexsum
        m = min(dic.values())
        for v in dic:
            if dic[v] == m:
                res.append(v)
        return res
