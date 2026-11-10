class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j]==g[i]:
                    count+=1
                    break
        return count