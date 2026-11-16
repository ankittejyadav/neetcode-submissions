class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount=0
        hmap={}
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        for k,v in hmap.items():
            if v>maxCount:
                maxCount=v
                majority=k
        return majority