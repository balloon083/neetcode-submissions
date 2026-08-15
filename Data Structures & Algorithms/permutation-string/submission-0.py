class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}
        for c in range(len(s1)):
            count[s1[c]] = 1 + count.get(s1[c], 0)
        
        res = False
        window = len(s1)
        for l in range(len(s2) - window + 1):
            check = {}
            for c in range(window):
                check[s2[l + c]] = 1 + check.get(s2[l + c], 0)
            if check == count:
                return True
        return False
