class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        list.append(i)
                        list.append(j)
                        return list               
        