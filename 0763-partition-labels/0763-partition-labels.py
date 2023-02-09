class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last=0
        output=[]
        track=0
        for start, char in enumerate(s):
            last=max(last, s.rfind(char))
            if start==last:
                output.append(last-track+1)
                track=last+1

        return output
                
                
            