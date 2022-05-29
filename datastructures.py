from time import sleep
import os

class buffer:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.queue = [None] * max_size
        self.size = 0
        pass

class circularBuffer(buffer):
    """
    circularBuffer implements an array with dynamic start - and endpoint.\n
    The head and tail are updated when putting an item on the queue and\n 
    taking an item off of it. When the number of items in the queue grows\n
    bigger than max_size, the oldest item is taken out of the queue and the\n
    new item is placed on top.

    --------
    ### Arguments:
    - `max_size (int)` - The maximum number of items in the buffer at any point in time.

    --------
    ### Functions:
    - `dequeue()`: Takes the oldest item off of the queue.
    - `enqueue(item)`: Puts item on top of the queue.
    """
    def __init__(self) -> None:
        # self.max_size = max_size
        # self.queue = [None] * max_size              # Make a list of max_size long

        # self.second_chances = [0] * max_size        # Keep track of the second chances per item in the queue
        self.tail = -1                              # Indicates where the newest item in the queue is
        self.head = 0                               # Indicates where the olderst item in the queue is
        # self.size = 0                               # Current size of the list  
        self.network_speed = 20                     # Estimated speed of the connection  

    def dequeue(self):
        if self.size == 0:
            print('The queue is empty')
            return
        else: 
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return tmp
        
    def enqueue(self, origin, item):
        try:
            timeout = (os.path.getsize(origin + '/' + item))/self.network_speed # For now network speed has to be checked manually
        except FileNotFoundError:
            timeout = 0
        self.tail += 1
        if self.size == self.max_size:
            sleep(timeout)
            self.tail = (self.tail) % self.max_size
            self.dequeue()
        self.queue[self.tail] = item
        self.size += 1


class clockBuffer(buffer):
    """
    Some description
    """
    def __init__(self) -> None:
        pass

    def dequeue(self):
        raise NotImplementedError('Not implemented yet')

    def enqueue(self, origin, item):
        raise NotImplementedError('Not implemented yet')

class secondChanceBuffer(buffer):
    """
    Some description
    """
    def __init__(self) -> None:
        pass

    def dequeue(self):
        raise NotImplementedError('Not implemented yet')

    def enqueue(self, origin, item):
        raise NotImplementedError('Not implemented yet')


class LRUBuffer(buffer):
    """
    Some description
    """
    def __init__(self) -> None:
        self.lru = 0
        pass

    def dequeue(self):
        raise NotImplementedError('Not implemented yet')

    def enqueue(self, origin, item):
        raise NotImplementedError('Not implemented yet')
    