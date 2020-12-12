"""LinkedList Solutions from Cracking the Coding Interview by Gayle Laakmann McDowell"""


class Node:
    """Node of the Linked List"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return "[" + ", ".join(nodes) + "]"

    def node_list(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(curr.data)
            curr = curr.next
        return nodes

    def prepend(self, data):
        """Add a node to the start of the list"""
        self.head = Node(data=data, next=self.head)

    def append(self, data):
        """Append a node to the end of the list"""
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def len(self):
        """Length Function for Linked List"""
        if not self.head:
            return 0
        i = 1
        curr = self.head
        while curr.next:
            i += 1
            curr = curr.next
        return i

    def remove_duplicates(self):
        """Remove Duplicated Data in the list"""
        unique_values = []
        curr = self.head
        unique_values.append(curr.data)
        while curr.next:
            prev_node = curr
            curr = curr.next
            if curr.data in unique_values:
                # do the removal
                prev_node.next = curr.next
                curr = prev_node
            else:
                unique_values.append(curr.data)

    def delete_middle_node(self, node):
        """Delete a middle node from the center of a list"""
        curr = self.head
        while curr:
            if curr.next and curr.next.data == node:
                curr.next = curr.next.next
                return
            curr = curr.next

    def kth_to_last(self, k):
        """Return the kth to last node of a singly linked list"""
        len = self.len()
        if k > len:
            return
        curr = self.head
        for x in range(0, len-k):
            curr = curr.next
        return curr

    def partition(self, partition):
        """Partition to left and right elements < partition and elements >= partition"""
        curr = self.head
        last = None
        while curr:
            next = curr.next
            if curr.data < partition and last:
                # Delete from list and prepend
                last.next = curr.next if curr.next else None
                curr.next = self.head
                self.head = curr
            else:
                last = curr
            if not curr.next:
                return
            curr = next
        return

    def check_palindrome(self):
        """Check whether a Linked List is a Palindrome"""
        if not self.head:
            return False
        curr = self.head
        stack = Stack()

        for _ in range(0, self.len()):
            stack.push(curr.data)
            curr = curr.next
        curr = self.head
        while curr:
            if curr.data != stack.pop():
                return False
            curr = curr.next
        return True

    def check_circular_loop(self):
        """Using Floyd's Algorithm (Tortoise and Hare) to check if the loop is circular"""
        # TODO: add in finding the start of the loop
        if not self.head:
            return False
        slow = fast = self.head
        while True:
            # move slow
            slow = slow.next
            # move fast
            if fast.next:
                fast = fast.next.next
            if not fast or not slow:
                return False
            if fast == slow:
                return True


def sum_lists(list_first, list_second):
    """Passed 2 lists of [number, tens, hundreds, ...]"""
    summed_list = LinkedList()
    curr_1 = list_first.head
    curr_2 = list_second.head
    carrying = 0
    while curr_1 or curr_2 or carrying:
        total = curr_1.data + curr_2.data + carrying
        carrying = 0
        summed_list.append(total % 10)
        if total > 10:
            carrying = 1
        curr_1 = curr_1.next
        curr_2 = curr_2.next
    return summed_list


def intersections(list_one, list_two):
    """Return the intersecting nodes of 2 linked lists if they exist"""
    curr_1 = list_one.head
    while curr_1:
        curr_2 = list_two.head
        while curr_2:
            if curr_1.data == curr_2.data:
                return curr_1
            curr_2 = curr_2.next
        curr_1 = curr_1.next
    return None


class StackNode:
    def __init__(self, data=None, prev=None):
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self):
        self.top_node = None

    def __repr__(self):
        curr = self.top_node
        nodes = []
        while curr:
            nodes.append(curr.data)
            curr = curr.prev
        return "-------\n" + "\n".join(nodes)

    def push(self, data):
        # Create StackNode for new data with prev being the prev top of the stack
        self.top_node = StackNode(data=data, prev=self.top_node)

    def pop(self):
        top_node = self.top_node
        self.top_node = self.top_node.prev
        return top_node.data
