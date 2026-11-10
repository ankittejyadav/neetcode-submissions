class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        visited=set()
        for i in range(len(g)):
            for j in range(len(s)):
                if s[j]>=g[i] and j not in visited:
                    count+=1
                    visited.add(j)
                    break
        return count