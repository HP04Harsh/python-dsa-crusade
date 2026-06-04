class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ans = {}

        for i in range(n):
            rem = target - numbers[i]
            if rem in ans:
                return [ans[rem]+1,i+1]
            ans[numbers[i]] = i    


        