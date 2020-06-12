import random
class RandomizedSet(object):

    def __init__(self):
        self.dic={}
        self.nums=[]
        
    def insert(self, val):
        if val not in self.dic:
            self.dic[val]=len(self.nums)
            self.nums.append(val)
            return True
        return False
    
    def remove(self, val):
        if val in self.dic:
            idx=self.dic[val]
            self.dic[self.nums[-1]]=idx
            self.nums[idx]=self.nums[-1]
            del self.dic[val]
            self.nums.pop()
            return True
        return False
            
    def getRandom(self):
        return random.choice(self.nums)
        
