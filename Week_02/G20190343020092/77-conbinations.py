#回溯法
#但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法
#这题的回溯，终止条件是组合数组的长度已达到k
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def back(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n+1):
                back(j+1, k-1, tmp + [j])
        back(1, k, [])  
        return res
