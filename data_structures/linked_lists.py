
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
        current=self.head
        
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None
    
    def insert(self, data, index):
        
        #inserts a new Node containing data at index position insertion takes O(1) time but finding the node at the insertion point takes O(n)
        if index==0:
            self.add(data)
        if index>0:
            new=Node(data)
            
            position=index
            current=self.head
            
            while position >1:
                current=Node.next_node
                position-=1
                
            prev_node=current
            next_node=current.next_node
            
            prev_node.next_node=current
            new.next_node=next_node
                
    def remove(self, key): 
        #Removes the node matching the key returning the node or None if key doesnt exist. takes O(n) time
        current=self.head
        previous=None
        found=False
        
        while current and not found:
            if current.data==key and current is self.head:
                found=True
                self.head=current.next_node
            elif current.data==key:
                found=True
                previous.next_node=current.next_node
            else:
                previous =current
                current=current.next_node  
        return current   

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
