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

class Stack:
    '''
    A linear collection of Nodes; last in, first out.
    '''

    def __init__(self):
        self._top = None

    def peek(self):
        '''
        Returns the top Node without changing the Stack.
        '''
        return self._top

    def pop(self):
        '''
        Returns and removes the top node from the Stack.
        '''
        top_node = self._top
        if top_node == None:
            raise Exception('Attempted to pop an empty Stack.')
        second_top_node = top_node.next
        # The 2nd top Node becomes the new top.
        self._top = second_top_node
        # 'Delete' the top Node and return it..
        top_node.next = None
        return top_node

    def push(self, data):
        '''
        Pushes a new Node onto the Stack.
        '''
        # Create a new Node, point it to the current top Node.
        new_node = Node(data=data, next_node=self._top)
        # Make the new Node the top Node.
        self._top = new_node

    @property
    def size(self):
        '''
        Size of the Stack.
        '''
        count = 0
        i_node = self._top
        while i_node != None:
            count += 1
            i_node = i_node.next
        return count

class Queue:
    '''
    A linear collection of Nodes; first in, first out.
    '''

    def __init__(self):
        self._front = None
        self._back = None

    def dequeue(self):
        '''
        Returns and removes the front Node of the Queue.
        '''
        if self.size == 0:
            raise Exception('Attempted to dequeu an empty Queue.')
        # Reference the front Node; it will be returned eventually.
        return_node = self._front
        # If only one Node, set front and back to None.
        if self.size == 1:
            self._front = None
            self._back = None
        else:
            # Iterate through the Queue,
            # Find 2nd-front Node (will become the new front).
            i_node = self._back
            while i_node != None:
                # If the next Node is the front of the queue, we found it.
                if i_node.next == self._front:
                    # 'Delete' the next Node.
                    i_node.next = None
                    # 2nd-front becomes the new front.
                    self._front = i_node
                    break
                i_node = i_node.next
        return return_node

    def enqueue(self, data):
        '''
        Adds a Node to the back of the Queue.
        '''
        # Create a new Node.
        new_node = Node(data=data)
        # If the Queue is empty, the new Node becomes the front.
        if self._front == None: self._front = new_node
        # Else, the new Node should point to the current back of the Queue.
        else: new_node.next = self._back
        # The new Node becomes the new back of the Queue.
        self._back = new_node
        pass

    def peek(self):
        '''
        Returns the front Node without changing the Queue.
        '''
        return self._front

    @property
    def size(self):
        '''
        Size of the Queue.
        '''
        count = 0
        i_node = self._back
        while i_node != None:
            count += 1
            i_node = i_node.next
        return count
