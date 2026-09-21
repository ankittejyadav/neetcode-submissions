class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for n in nums:
            if n in hashmap:
                return True
            hashmap[n]=1+hashmap.get(n,0)
        return False