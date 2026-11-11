class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap={}
        for e in nums:
            if e in hmap:
                return True
            hmap[e]=1+hmap.get(e,0)
        return False