class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.nums1 = set(nums1)
        self.nums2 = set(nums2)

        return list(self.nums1.intersection(self.nums2))
        