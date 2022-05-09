class circularBuffer:
    def __init__(self, max_size: int = 3) -> None:
        self.max_size = max_size
        self.queue = [None] * max_size              # Make a list of max_size long
        self.tail = -1                              # Indicates where the newest item in the queue is
        self.head = 0                               # Indicates where the olderst item in the queue is
        self.size = 0                               # Current size of the list    

    def dequeue(self):
        if self.size == 0:
            print('The queue is empty')
            return

        else: 
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size

        self.size -= 1
        return tmp
        
    def enqueue(self, item):
        self.tail += 1
        if self.size == self.max_size:
            self.tail = (self.tail) % self.max_size
            self.dequeue()
        self.queue[self.tail] = item
        self.size += 1
    
    # def display(self):
    #     if self.size == 0:
    #         print('Queue is empty')
    #     else: 
    #         index = self.head
    #         for _ in range(self.size):
    #             print(self.queue[index])
    #             index = (index + 1) % self.max_size

# test = loggingList()
# test.append('test')
# print(test)
# test[0] = 'changed'