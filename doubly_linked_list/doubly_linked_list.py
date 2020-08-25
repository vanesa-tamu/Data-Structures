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
        # if no nodes
        if self.tail is None:
            return None

        # if one node
        elif self.tail == self.head:
            old_tail = self.tail
            new_tail = old_tail.prev  # None

            # update tail
            self.tail = new_tail

            # update head
            self.head = None
            # # change new_tail next to None
            # new_tail.next = None
            # # change old_tail prev pointer to None
            # old_tail.prev = None
            # decrement size
            self.length -= 1
            # return old tail value
            return old_tail.value

        # if 2 nodes, need to update head as well
        if self.length == 2:
            old_tail = self.tail
            new_tail = old_tail.prev

            # update tail
            self.tail = new_tail
            # decrement
            self.length -= 1
            return old_tail.value

        # if 3+ nodes
        else:
            old_tail = self.tail
            # update tail
            new_tail = old_tail.prev
            self.tail = new_tail
            # tail next points to none
            new_tail.next = None
            # decrement
            self.length -= 1
            return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # checks if a node value exists in list
    def is_in_list(self, node):
        old_head = self.head
        # print(f'i old_head: {old_head}')
        # iterate through list until find matching node or reach end of list
        # first case is for when list is empty and head and tail equal none (and have no value)
        # while old_head.value != node and old_head is not None and
        # old_head != old_head.value and old_head != self.tail:
        while self.length != 0 and old_head is not None and old_head.value != node.value and old_head != self.tail:
            old_head = old_head.next
            # print(f'f old_head: {old_head}')
        if old_head is None:
            return False
        # fixed from node to node.value (to fix delte method)
        elif node.value == old_head.value:
            return True
        else:
            return False

    def move_to_front(self, node):
        # length never changes (by def.)
        # need to check if input node is within the List
        if self.is_in_list(node):
            # can just delete node and move to front from here
            self.delete(node)
            self.add_to_head(node.value)  # add_to_head takes in a value
            return node.value
        else:
            return f'{node} is not in list'
        # if only one node, no change happens
        # if 2 nodes, the tail and head switch places
        # if 3+ nodes, head will need to be updated
        # if input node = tail node, then need to update tail too
        # pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.is_in_list(node):
            self.delete(node)
            self.add_to_tail(node.value)
        else:
            return f'{node} is not in list'

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node: ListNode):
        # print(node.prev)
        if self.is_in_list(node):
            # node is the only one in the list
            if self.head == self.tail:
                self.remove_from_head()
                # old_head = self.head
                # # point prev and next node to None
                # old_head.prev = None
                # old_head.next = None
                # # update head and tail
                # self.head = None
                # self.tail = None
                # # update length
                # self.length -= 1
            # node is the head
            elif self.head.value == node.value:
                self.remove_from_head()
                return node.value
            # node is the tail
            elif self.tail.value == node.value:
                self.remove_from_tail()
                return node.value
            # node is between head and tail
            else:
                # get previous node:
                previous_node = node.prev
                # get next node
                next_node = node.next
                # assign previous_node to point to next_node:
                previous_node.next = next_node
                # assign next_node to point to back to previous_node:
                next_node.prev = previous_node
                # set node's next and previous pointers to None
                node.prev = None
                node.next = None
                # decrement by 1
                self.length -= 1
                # return node.value that was deleted
                return node.value
        else:
            return f'{node} is not in list'

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


# Remove tail
# ll4 = DoublyLinkedList()
# ll4.add_to_head(50)
# ll4.add_to_head(15)
# ll4.add_to_head(35)  # 35 - 15 - 50
# print(ll4.remove_from_tail())  # 50 removed
# print(ll4)
# print(ll4.remove_from_tail())  # 15 removed
# print(ll4)
# print(ll4.remove_from_tail())  # 35 removed
# print(ll4)


# Move to front
# ll4 = DoublyLinkedList()
# ll4.add_to_head(50)
# ll4.add_to_head(15)
# ll4.add_to_head(35)  # 35 - 15 - 50
# # print(ll4.move_to_front(50))  # True
# print(ll4)
# print(ll4.is_in_list(ll4.head))  # True
# print(f'deleting head: {ll4.delete(35)}')  # returns none but success!
# print(ll4)
# print(f'deleting tail: {ll4.delete(50)}')  # returns none but success!
# print(ll4)
# print(f'deleting only node: {ll4.delete(15)}')  # returns none but success!
# print(ll4)
# print(f'deleting from empty list: {ll4.delete(600)}')  # returns 15 is not in list
# print(ll4)
# print(f'deleting from empty list: {ll4.delete(900)}')  # returns 15 is not in list
# print(ll4)


# Delete
# ll6 = DoublyLinkedList()
# ll6.add_to_head(35)
# ll5 = DoublyLinkedList()
# ll5.add_to_head(5)
# ll5.add_to_head(10)
# ll5.add_to_head(9)
# ll5.add_to_head(1)
# ll5.add_to_head(3)  # 3 - 1 - 9 - 10 - 5
# print(ll5.delete(ll5.tail))  # tail is now 10
# print(f'{ll5}\n')  # length = 4
# print(ll5.delete(ll5.head))  # head is now 1
# print(f'{ll5}\n')  # length = 3
# print(ll5.delete(ll6.head))  # 35 is not in list
# print(ll5.delete(ll5.head.next))  # 9 deleted
# print(f'{ll5}\n')  # length = 2
#
# print(ll5.delete(ll5.head))
# print(f'{ll5}\n')
#
# print(ll5.delete(ll5.head))
# print(f'{ll5}\n')
#
# print(ll5.delete(ll5.head))
# print(f'{ll5}\n')


# move to front
# ll7 = DoublyLinkedList()
# ll7.add_to_head(99)
# ll7.add_to_head(90)
# print(f'{ll7} \n')
# print(ll7.move_to_front(ll7.tail))
# print(f'{ll7} \n')


# move to end
# ll8 = DoublyLinkedList()
# ll8.add_to_head(100)
# ll8.add_to_head(190)
# print(f'{ll8} \n')
# print(ll8.move_to_end(ll8.head))
# print(f'{ll8} \n')


# find max
