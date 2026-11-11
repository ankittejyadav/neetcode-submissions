class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for c in range(len(s)-1,-1,-1):
            if s[c]!=' ':
                count+=1
            elif s[c]==' ' and count>0:
                return count
        return count