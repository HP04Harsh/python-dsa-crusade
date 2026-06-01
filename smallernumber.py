# How Many Numbers Are Smaller Than the Current Number


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0

            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
                else:
                    continue
            result.append(count)
        return result               