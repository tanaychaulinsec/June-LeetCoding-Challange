import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph=defaultdict(dict)
        for start,end,cost in flights:
            graph[start][end]=cost
        hq=[(0,src,K+1)]
        visited=defaultdict(int)
        while hq:
            cur_cost,cur_dst,K=heapq.heappop(hq)
            visited[cur_dst]=K
            if cur_dst==dst:
                return cur_cost
            if K>0:
                for j in graph[cur_dst]:
                    if j in visited and K-1<=visited[j]:
                        continue
                    heapq.heappush(hq,(cur_cost+graph[cur_dst][j],j,K-1))
        return -1
        
        