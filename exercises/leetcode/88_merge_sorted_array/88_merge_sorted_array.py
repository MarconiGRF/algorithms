from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        while i < len(nums1) and j < n:
            if nums1[i] <= nums2[j] and nums1[i] != 0:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1

        k = len(nums1) - 1
        while k >= 0:
            if nums1[k] == 0:
                nums1.pop()
                k -= 1
            else:
                break

if __name__ == '__main__':
    # Solution.merge(None, [1,2,3,0,0,0], 3, [2,5,6], 3)
    Solution.merge(None, [1], 1, [], 0)