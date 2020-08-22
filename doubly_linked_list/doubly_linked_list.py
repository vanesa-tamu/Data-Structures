"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f'Value: {self.value}'


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        return f'\n Head: {self.head} \n Tail: {self.tail} \n L: {self.length}'
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # if no node exists, return None
        if self.head is None:
            new_node = ListNode(value, prev=None, next=None)
            self.head = new_node
            self.tail = new_node

        # if only one node exists, change tail pointer
        elif self.head == self.tail:
            old_head = self.head
            new_node = ListNode(value, prev=None, next=old_head)
            # old_head previous will be new_node (not None)
            old_head.prev = new_node
            # change head node to be new_node
            self.head = new_node
            # change next pointer to old_head
            # new_node.next = old_head  

        # if has multiple nodes (General Case)
        else:
            old_head = self.head
            new_node = ListNode(value, prev=None, next=old_head)
            # point old_head to new node
            old_head.prev = new_node
            # new node as head
            self.head = new_node
        # add length regardless of case
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if no node:
        if self.head is None:
            return None
        # if one node:
        elif self.head == self.tail:
            old_head = self.head
            # point prev and next node to None
            old_head.prev = None
            old_head.next = None
            # update head and tail
            self.head = None
            self.tail = None
            # update length
            self.length -= 1
            return old_head.value
        else:
            old_head = self.head
            new_head = old_head.next
            # new_head previous points to None (not old_head)
            new_head.prev = None
            # update new head
            self.head = new_head
            # update length
            self.length -= 1
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # LL has no node
        if self.tail is None:
            tail_node = ListNode(value)
            # update head and tail
            self.head = tail_node
            self.tail = tail_node

        # LL has 1+ node(s) - General Case
        else:
            # old tail
            old_tail = self.tail
            # new node - prev. node is old tail
            new_tail = ListNode(value, old_tail, next=None)
            # old_tail next pointer points to new_tail
            old_tail.next = new_tail
            # update tail of LL
            self.tail = new_tail

        # update length
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

# Add to head:


# ll1 = DoublyLinkedList()
# print(ll1)
# ll1.add_to_head(1)
# print(ll1)
# ll1.add_to_head(20)
# print(ll1)
# ll1.add_to_head(40)
# print(ll1)

# Remove head

# ll2 = DoublyLinkedList()
# ll2.add_to_head(50)
# ll2.add_to_head(15)
# ll2.add_to_head(35)
# print(ll2.remove_from_head())  # 35 removed
# print(ll2.remove_from_head())  # 15 removed
# print(ll2.remove_from_head())  # 50 removed
# print(ll2)


# Add to tail:


# ll3 = DoublyLinkedList()
# print(ll3)
# ll3.add_to_tail(1)
# print(ll3)
# ll3.add_to_tail(20)
# print(ll3)
# ll3.add_to_tail(40)
# print(ll3)
