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

class LinkedList:
    '''
    A linear collection of nodes.
    '''

    def __init__(self, head=None):
        self._head = head

    def insert(self, data):
        '''
        Inserts a new Node into the front of the Linked List.
        '''
        # Create a Node with the given data.
        new_node = Node(data=data)
        # Point the new Node to the current head of the LL.
        new_node.next = self._head
        # Update the LL so that the new node is the head.
        self._head = new_node

    @property
    def size(self):
        '''
        Size of the Linked List.
        '''
        count = 0
        i_node = self._head
        while i_node != None:
            count += 1
            i_node = i_node.next
        return count

    def search(self, query):
        '''
        Returns Node with data matching the input query. Exception if no match.
        '''
        i_node = self._head
        while i_node != None:
            if i_node.data == query:
                return i_node
            i_node = i_node.next
        raise Exception("Could not find Node with data '{}'.".format(query))

    def delete(self, query):
        '''
        Deletes Node with data matching the input query. Exception if no match.
        '''
        this_node = self._head
        prev_node = None
        while this_node != None:
            if this_node.data == query:
                next_node = this_node.next
                # Make this Node point to nothing (effectively deletes it).
                this_node.next = None
                # If we're removing the head, simply reassign the head to the next node.
                if prev_node == None: self._head = next_node
                # Else, make the prev Node point to the next node.
                else: prev_node.next = next_node
                return
            prev_node = this_node
            this_node = this_node.next
        raise Exception("Could not find Node with data '{}'.".format(query))
