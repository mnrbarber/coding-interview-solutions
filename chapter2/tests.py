from chapter2.linkedLists import *
from unittest import TestCase


class RemoveDuplicatesTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        list_nodes = ["A", "B", "B", "C", "D", "D", "A", "B","C"]
        self.unique_nodes = ["A", "B", "C", "D"]
        for node in list_nodes:
            self.linked_list.append(data=node)
        self.unique_linked_list = LinkedList()
        for node in self.unique_nodes:
            self.unique_linked_list.append(data=node)
        self.unique_list = "[" + ", ".join(self.unique_nodes) + "]"

    def test_remove_duplicates(self):
        self.linked_list.remove_duplicates()
        self.assertEqual(self.unique_list, str(self.linked_list))

    def test_unique_list(self):
        self.unique_linked_list.remove_duplicates()
        self.assertEqual(self.unique_list, str(self.unique_linked_list))


class DeleteMiddleNodeTestCase(TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
        self.nodes = ["a", "b", "c", "d", "e"]
        for node in self.nodes:
            self.linked_list.append(data=node)
        self.list = "[" + ", ".join(self.nodes) + "]"
        self.new_list = "[" + ", ".join(["a", "b", "d", "e"]) + "]"

    def test_delete_middle_node(self):
        self.linked_list.delete_middle_node("c")
        self.assertEqual(self.new_list, str(self.linked_list))

    def test_delete_non_existant_node(self):
        self.linked_list.delete_middle_node("f")
        self.assertEqual(self.list, str(self.linked_list))


class SumListTestCase(TestCase):
    def setUp(self):
        self.list_one = LinkedList()
        self.list_two = LinkedList()
        self.list_sum = LinkedList()
        self.nodes_one = [7, 1, 6]
        self.nodes_two = [5, 9, 2]
        self.summed_nodes = [2, 1, 9]
        for node in self.nodes_one:
            self.list_one.append(node)
        for node in self.nodes_two:
            self.list_two.append(node)
        for node in self.summed_nodes:
            self.list_sum.append(node)

    def test_summed_list(self):
        list = sum_lists(self.list_one, self.list_two)
        self.assertEqual(str(self.list_sum), str(list))


class IntersectionTestCase(TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.intersecting_list = LinkedList()
        self.non_intersecting_list = LinkedList()
        for node in ["A", "B", "C", "D", "E"]:
            self.list.append(node)
        for node in ["F", "G", "C"]:
            self.intersecting_list.append(node)
        for node in ["F", "G", "H", "I"]:
            self.non_intersecting_list.append(node)

    def test_intersecting_list(self):
        intersecting_node = intersections(self.list, self.intersecting_list)
        self.assertEqual(intersecting_node.data, "C")

    def test_non_intersecting_list(self):
        non_intersecting_node = intersections(self.list, self.non_intersecting_list)
        self.assertIsNone(non_intersecting_node)
