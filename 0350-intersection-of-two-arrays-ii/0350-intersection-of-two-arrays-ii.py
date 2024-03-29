class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        pt1, pt2, output = 0, 0, []
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] < nums2[pt2]:
                pt1+=1
            elif nums1[pt1] > nums2[pt2]:
                pt2+=1
            else:
                output.append(nums1[pt1])
                pt1+=1
                pt2+=1
        return output