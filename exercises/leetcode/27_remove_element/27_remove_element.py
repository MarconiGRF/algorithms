from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurrences = 0

        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i +=1
                occurrences += 1
        return occurrences