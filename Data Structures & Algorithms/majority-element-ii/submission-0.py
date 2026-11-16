class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap={}
        res=[]
        nlen=len(nums)//3
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        
        for k,v in hmap.items():
            if v>nlen:
                res.append(k)
        return res