class Node:
    '''
    The building block which makes up bigger data structures.

    A Node consists of two things:
    1) Some arbitrary data.
    2) A pointer to the next Node. (null if at the end of the list.)

    Nodes are used to construct linked lists, queues, stacks, and more.
    '''

    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        '''
        Node's main content.
        '''
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        '''
        Pointer to the next Node.
        '''
        return self._next_node

    @next.setter
    def next(self, new_next):
        self._next_node = new_next
