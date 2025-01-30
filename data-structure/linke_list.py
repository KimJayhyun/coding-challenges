class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    @classmethod
    def from_list(cls, arr):
        linked_list = cls()

        for data in arr:
            linked_list.append(data)

        return linked_list

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        old_head = self.head

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        self.tail = old_head

    def delete(self):
        if self.head is None:
            raise IndexError("Empty Linked List")

        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def __str__(self):
        result = []

        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return str(result)
