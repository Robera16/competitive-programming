class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1, st2 = list(set(nums1)), list(set(nums2))
        st1.sort()
        st2.sort()
        output, pt1, pt2 = [], 0, 0
        while pt1 < len(st1) and pt2 < len(st2):
            if st1[pt1] < st2[pt2]:
                pt1+=1
            elif st1[pt1] > st2[pt2]:
                pt2+=1
            else:
                output.append(st1[pt1])
                pt1+=1
                pt2+=1
                
        return output
        
        