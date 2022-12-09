class Node:
    def __init__(self, value, prev, next) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLL:
    def __init__(self) -> None:
        self.head = Node(0, None, None)
        self.tail = self.head

    def size(self):
        return self.head.value

    def increment_size(self, by=1):
        self.head.value += by
        return self.head.value

    def decrement_size(self, by=1):
        self.head.value -= by
        return self.head.value

    def is_empty(self):
        return self.size() == 0

    def peek_first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.next.value

    def peek_last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.tail.value

    def append(self, value):
        self.tail.next = Node(value, self.tail, None)
        self.tail = self.tail.next
        self.increment_size()

    def append_first(self, value):
        new_value = Node(value, self.head, self.head.next)
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
            position += 1
        iter.next = Node(value, iter, iter.next)
        self.increment_size()

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.head.next = self.head.next.next
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head

    def remove_at(self, at):
        if self.is_empty():
            raise Exception("List is empty")
        if at < 0 or at >= self.size():
            raise Exception("Index out of bounds")
        position = 0
        iter = self.head
        while position < at:
            iter = iter.next
            position += 1
        iter.next = iter.next.next
        self.decrement_size()
        if self.is_empty():
            self.tail = self.head

    def display(self):
        iter = self.head
        output = ""
        while iter.next != None:
            output += f" <--> {iter.next.value}"
            iter = iter.next
        print(output)
