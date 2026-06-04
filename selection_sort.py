class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        for i in range(n):
          minx = i

          for j in range(i+1,n):
            if nums[j]<nums[minx]:
                minx = j

          nums[i],nums[minx] = nums[minx],nums[i]
        return nums  
