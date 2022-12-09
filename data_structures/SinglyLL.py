class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next


class SinglyLL:
    def __init__(self) -> None:
        # head contains the size of list
        self.head = Node(0, None)
        self.tail = self.head

    def display(self):
        iter = self.head
        print_str = ""
        while iter.next != None:
            print_str += f" --> {iter.next.value}"
            iter = iter.next
        print(print_str)

    def size(self):
        return self.head.value

    def is_empty(self):
        return self.size() == 0

    def increment_size(self, by=1):
        self.head.value += by
        return self.head.value

    def decrement_size(self, by=1):
        self.head.value -= by
        return self.head.value

    def peek_last(self):
        if self.is_empty():
            return None
        return self.tail.value

    def peek_first(self):
        if self.is_empty():
            return None
        return self.head.next.value

    def append(self, value):
        self.tail.next = Node(value, None)
        self.tail = self.tail.next
        self.increment_size()

    def append_first(self, value):
        new_value = Node(value, self.head.next)
        self.head.next = new_value
        if self.is_empty():
            self.tail = new_value
        self.increment_size()

    def insert(self, value, at):
        if at <= 0:
            self.append_first(value)
            return
        if at >= self.size():
            self.append(value)
            return
        iter = self.head
        position = 0
        while position < at:
            iter = iter.next
        iter.next = Node(value, iter.next)

    def remove_first(self):
        if self.is_empty():
            raise Exception("Empty list, cant remove")
        self.head.next = self.head.next.next
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head

    def remove_at(self, at):
        if self.is_empty():
            raise Exception("Empty list, cant remove")
        if at < 0 or at >= self.size():
            raise Exception("Index out of bounds")
        iter = self.head
        position = 0
        while position < at:
            position += 1
            iter = iter.next
        iter.next = iter.next.next
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head

    def remove_last(self):
        self.remove_at(self.size() - 1)
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head
