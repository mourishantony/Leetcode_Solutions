class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = Counter(arr)
        res = []
        for i in ans.keys():
            if ans[i] == 1:
                res.append(i)
        
        if len(res) >= k:
            return res[k-1]
        else:
            return ""