from tarfile import FIFOTYPE
from time import sleep
import os

class buffer:
    def __init__(self, max_size: int, origin: str = None) -> None:
        self.max_size = max_size
        self.queue = [None] * max_size
        self.size = 0
        self.origin = origin
        pass

class fifoBuffer(buffer):
    """
    fifoBuffer implements an array with dynamic start - and endpoint.\n
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
        self.tail          = -1                       # Indicates where the newest item in the queue is
        self.head          = 0                        # Indicates where the olderst item in the queue is
        # self.size = 0                               # Current size of the list  
        self.network_speed = 20                       # Estimated speed of the connection  

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

class timedBuffer(buffer):
    """
    timedBuffer implements an array with dynamic start - and endpoint.\n
    The head and tail are updated when putting an item on the queue and\n 
    taking an item off of it. When the number of items in the queue grows\n
    bigger than max_size, the oldest item is taken out of the queue and the\n
    new item is placed on top. A delay is added to wait for a small amount of \n
    time to let items that are almost done uploading finish uploading.

    --------
    ### Arguments:
    - `max_size (int)` - The maximum number of items in the buffer at any point in time.
    - `origin (str)` - The origin folder. This is used in some enqueue methods.

    --------
    ### Functions:
    - `dequeue()`: Takes the oldest item off of the queue.
    - `enqueue(item, origin)`: Puts item on top of the queue. Origin is set as optional, but \n
         this is merely for implementation reasons. You should really set a value.
    """
    def __init__(self) -> None:
        self.tail          = -1                       # Indicates where the newest item in the queue is
        self.head          = 0                        # Indicates where the olderst item in the queue is
        self.network_speed = 20                       # Estimated speed of the connection Mb/sec

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
        try:
            timeout = (os.path.getsize(self.origin + '/' + item))/self.network_speed # For now network speed has to be checked manually
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
    secondChanceBuffer implements an array with dynamic start - and endpoint.\n
    The head and tail are updated when putting an item on the queue and\n 
    taking an item off of it. When the number of items in the queue grows\n
    bigger than max_size, the `enqueue()` looks for the oldest item that has \n
    not been visited by the tail before and that item is taken out of the queue \n 
    and the new item is placed on top.

    --------
    ### Arguments:
    - `max_size (int)` - The maximum number of items in the buffer at any point in time.

    --------
    ### Functions:
    - `dequeue()`: Takes the oldest item off of the queue.
    - `enqueue(item)`: Puts item on top of the queue and checks which item should be taken off.
    """
    def __init__(self) -> None:
        self.visited = [0] * self.max_size
        pass

    def dequeue(self):
        if self.size == 0:
            print('The queue is empty')
            return
        else: 
            tmp = self.queue[self.head]
            self.visited[self.head] = 0
            self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return tmp
        # raise NotImplementedError('Not implemented yet')

    def enqueue(self, item):
        self.tail += 1
        if self.size == self.max_size:
            self.tail = (self.tail) % self.max_size
            if self.visited[self.tail] == 1:
                self.dequeue()
                self.queue[self.tail] = item
                self.size += 1
                return
            else:
                self.visited[self.tail] = 1
                self.enqueue(self,item)
        else:
            self.queue[self.tail] = item
            self.size += 1
            return

        # raise NotImplementedError('Not implemented yet')


class lruBuffer(buffer):
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

class spacingBuffer(buffer):
    """
    spacingBuffer implements an array with dynamic start - and endpoint.\n
    The head and tail are updated when putting an item on the queue and\n 
    taking an item off of it. When the number of items in the queue grows\n
    bigger than max_size, the `enqueue()` deletes the oldest item that has \n
    a space of at least `spacing` between it and the last deleted item, and \n 
    the new item is placed on top.

    --------
    ### Arguments:
    - `spacing (int)` - The minimum amount of uploads between two deletions.
    - `max_size (int)` - The maximum number of items in the buffer at any point in time.

    --------
    ### Functions:
    - `dequeue()`: Takes the oldest item off of the queue.
    - `enqueue(item)`: Puts item on top of the queue and checks which item should be taken off.
    """
    def __init__(self, spacing: int = 5) -> None:
        self.previous_deletion: int = 0
        self.itemnr: int            = 0
        self.spacing                = spacing
        pass

    def dequeue(self):
        if self.size == 0:
            print('The queue is empty')
            return
        else: 
            tmp = self.queue[self.head]
            self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return tmp
        # raise NotImplementedError('Not implemented yet')

    def enqueue(self, item):
        self.tail += 1
        if self.size == self.max_size:
            self.tail = (self.tail) % self.max_size
            if self.itemnr - self.previous_deletion >= self.spacing:
                self.previous_deletion = self.itemnr
                self.dequeue()
                self.queue[self.tail] = item
                self.size += 1
                self.itemnr += 1
                return
            else:
                self.enqueue(self,item)
                self.itemnr += 1
        else:
            self.queue[self.tail] = item
            self.size += 1
            itemnr += 1
            return

    