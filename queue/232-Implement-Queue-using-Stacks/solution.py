class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        ele = self.queue[0]
        del self.queue[0]
        return ele
        

    def peek(self):
        """
        :rtype: int
        """
        ele = self.queue[0]
        return ele

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
