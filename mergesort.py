class Solution:


    def merge(self,left,right):
        result = []
        i = j =0 

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1    

        result.extend(left[i:])
        result.extend(right[j:])
        return result        


    def mergeSort(self,arr):

        if len(arr)<=1:
            return arr

        mid = len(arr)//2 
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left,right)   


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
            
