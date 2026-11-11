class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hmap={}
        res=[]
        for c in words[0]:
            hmap[c]=1+hmap.get(c,0)
        
        for w in words[1:]:
            hmap2={}
            for c in w:
                hmap2[c]=1+hmap2.get(c,0)
            for c in hmap:
                hmap[c]=min(hmap[c], hmap2.get(c,0))

        for c in hmap:
            res.extend([c]*hmap[c])
        return res
            