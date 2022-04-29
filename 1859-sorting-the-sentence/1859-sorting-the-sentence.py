class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split()
        list2=[0]*len(list1)
        
        for word in list1:
            list2[int(word[-1])-1]=word.rstrip(word[-1])
        
        string=''
        i=0
        for word in list2:
            string+=word
            if(i!=len(list1)-1):
                string+=' '
            i+=1
        return string