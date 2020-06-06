import random
class Solution:
    def __init__(self, w):
        self.cumArray=w
        for i in range(1,len(w)):
            self.cumArray[i]=self.cumArray[i-1]+w[i]

    def pickIndex(self):
        l,r=0,len(self.cumArray)-1
        rand_num=random.randint(1,self.cumArray[-1])
        while l<=r:
            mid=(l+r)//2
            if self.cumArray[mid]<rand_num:
                l=mid+1
            else:
                r=mid-1
        return l