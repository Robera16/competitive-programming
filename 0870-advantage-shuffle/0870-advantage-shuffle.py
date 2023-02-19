class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        result = []
        counter = defaultdict(list)
        for idx in sorted(nums2, reverse=True):
            if nums1[-1] > idx: 
                counter[idx].append(nums1.pop())
        for idx in nums2:
            if counter[idx]:
                result.append(counter[idx].pop())
            else:
                result.append(nums1.pop())
        return result