class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        start, end, chemistry = 0, len(skill)-1, 0
        valid = skill[start] + skill[end]
        
        while(start < end):
            if valid == (skill[start] + skill[end]):
                chemistry+=(skill[start] * skill[end])
                start+=1
                end-=1
            else:
                return -1
        return chemistry
        