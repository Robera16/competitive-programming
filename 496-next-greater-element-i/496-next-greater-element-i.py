class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for i in nums1:
            qry=-1
            for j in range(nums2.index(i)+1, len(nums2)):
                if nums2[j] > i:
                    qry=nums2[j]
                    break
            output.append(qry)
        return output