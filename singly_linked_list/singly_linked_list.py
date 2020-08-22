class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list

    def __str__(self):
        return f'Node value is {self.value}'


class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
        self.length = 0

    def __str__(self):
        return f'\n Head: {self.head} \n Tail: {self.tail} \n Length: {self.length} \n'

    def add_to_head(self, value):
        # create new Node obj.
        new_head = Node(value, None)
        # Check if there's a head
        # If no head (emtpy list)
        if self.head is None:
            # set tail & head to new Node created
            self.head = new_head
            self.tail = new_head
        # Check if single node in list
        elif self.head == self.tail:
            old_head = self.head  # evaluates to node 1 value
            # change head to new node value
            self.head = new_head
            self.head.next = old_head
            # self.tail = old_head  # do I have to add to self.tail too?? Makes no dif.
        # Add new node (General case)
        else:
            # save old head value
            old_head = self.head
            # set new node to head
            self.head = new_head
            # set the head's next node
            self.head.next = old_head
        self.length += 1

    def add_to_tail(self, value):
        # Check if there's a tail
        # If there is no tail (empty list)
        if self.tail is None:
            # Create a new node
            new_tail = Node(value, None)
        #    Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        # If not head (empty list)
        if self.head is None:  # if self.head is None
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length = self.length - 1
            return current_head.value

    def remove_tail(self):
        pass
        # Remove Tail:
        # Check if it's there
        if self.tail is None:
            return None
        # List of 1 element:

        if self.tail == self.head:
            # Save the current_tail.value
            current_tail = self.tail
            # Set self.tail to None
            self.tail = None
            # Set self.head to None
            self.head = None
            self.length -= 1
            return current_tail.value

        # General case:
        else:
            current_node = self.head
            # Start at head and iterate to the next-to-last node
            # Stop when current_node.next == self.tail
            while current_node.next != self.tail:
                current_node = self.head.next

            # Save the current_tail value
            current_tail = self.tail
            # Set self.tail to current_node
            self.tail = current_node
            # current_node = current_tail -> no b/c ev. to 30
            # Set current_node.next to None
            current_node.next = None
            self.length -= 1
            return current_tail.value

# Remove Tail


# ll1 = LinkedList()
# # print(ll1.remove_tail())  # None
# # print(f'{ll1}')
# #
# # ll1.add_to_tail(10)
# # print(f'{ll1}')
# # print(ll1.remove_tail())  # 10
# # print(f'{ll1}')
# # print(ll1.remove_tail())  # None
# #
# # ll1.add_to_tail(20)
# # ll1.add_to_tail(30)
# # print(f'{ll1}')  # len = 2
# # print(f'{ll1.remove_tail()}')  # 30
# # print(f'{ll1}')  # len = 1


# Add Head

ll2 = LinkedList()
print(ll2)
ll2.add_to_head(1)
print(ll2)
ll2.add_to_head(100)
print(ll2)
ll2.add_to_head(1000)
print(ll2)
