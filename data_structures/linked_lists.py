class Node:
    # An object for storing a single node of a linked list
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    # Singly linked list
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        # Returns the number of nodes in the list taking O(n) time
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        # Add new node containing data at the head of the list
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    #searching through the list returning the value if found and none if not found
    def search(self, key):
        current=self.key
        
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
            return None
        

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return ' -> '.join(nodes)
