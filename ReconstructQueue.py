class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        d={}
        res=[]
        for h,k in people:
            if h not in d:
                d[h]=[[h,k]]
            else:
                d[h].append([h,k])
        for h in sorted(d.keys(),reverse=True):
            group=sorted(d[h])
            if res:
                for h,k in group:
                    res.insert(k,[h,k])
            else:
                res+=group
        return res