class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.counter = 0
        self.queue = deque()
        self.i = 0
        
    def consec(self, num: int) -> bool:
        
        self.counter += 1
        self.queue.append(num)
        if num==self.value:
            self.i+=1
            
        if self.counter < self.k:
            return False
        else:

            if self.k==self.i:
                if self.queue.popleft()==self.value:
                    self.i-=1
                return True
            else:
                if self.queue.popleft()==self.value:
                    self.i-=1
                return False
            
             

