
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

    def prepend(self, data):
        self.head = Node(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data=data)

    def len(self):
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
        curr = self.head
        while curr:
            if curr.next and curr.next.data == node:
                curr.next = curr.next.next
                return
            curr = curr.next


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
    curr_1 = list_one.head
    while curr_1:
        curr_2 = list_two.head
        while curr_2:
            if curr_1.data == curr_2.data:
                return curr_1
            curr_2 = curr_2.next
        curr_1 = curr_1.next
    return None
