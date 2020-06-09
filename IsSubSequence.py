#DP Approach(O(len(s)*len(t)) Time and space
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        
        dp=[[0 for i in range(len(t)+1)]for j in range(len(s)+1)]
        for r in range(1,len(s)+1):
            for c in range(1,len(t)+1):
                if s[r-1]==t[c-1]:
                    dp[r][c]=(dp[r-1][c-1]+1)
                else:
                    dp[r][c]=max(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])
        return len(s)==dp[r][c]