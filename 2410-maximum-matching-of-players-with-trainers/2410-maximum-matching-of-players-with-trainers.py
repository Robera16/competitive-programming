class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ability, capacity, output = 0, 0, 0
        while ability < len(players) and capacity < len(trainers):
            if players[ability] <= trainers[capacity]:
                output+=1
                ability+=1
            capacity+=1
        return output
            