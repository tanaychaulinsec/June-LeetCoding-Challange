import heapq
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff=[]
        minCost=0
        for a,b in costs:
            diff.append(b-a)
            minCost+=a
        heapq.heapify(diff)
        for i in range(len(costs)//2):
            minCost+=heapq.heappop(diff)
        return minCost