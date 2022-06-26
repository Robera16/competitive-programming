class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        boats=0
        
        while(len(people)):
            if people[0]+people[-1]<=limit:
                people.pop(0)
            if len(people):
                people.pop()
            boats+=1
        return boats

        