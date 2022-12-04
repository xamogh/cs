class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def length(self):
        return self.size

    def append(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1

    def append_first(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head = Node(value, self.head)
        self.size += 1

    def insert(self, at, value):
        if at <= 0:
            self.append_first(value)
            return
        if at >= self.size:
            self.append(value)
            return

        iter = self.head
        i = 0

        while i < at - 1:
            if iter is None:
                break
            iter = iter.next
            i += 1

        iter.next = Node(value, iter.next)

    def insert_multiple(self, values, at):
        self.size += len(values)
        if at <= 0:
            for value in reversed(values):
                self.append_first(value)
            return
        if at >= self.size:
            for value in values:
                self.append(value)
            return

        iter = self.head
        i = 0

        while i < at - 1:
            if iter.next is None:
                break
            iter = iter.next
            i += 1

        for value in reversed(values):
            iter.next = Node(value, iter.next)

    def remove_first(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.size -= 1

        if self.head == None:
            self.tail = None

    def remove(self, at):
        if at < 0 or at >= self.length():
            raise Exception("Index out of bounds")

        if at == 0:
            self.remove_first()
            if self.head == None:
                self.tail = None
            return

        i = 0
        iter = self.head
        while i < at - 1:
            iter = iter.next
            i += 1

        if at == self.length() - 1:
            iter.next = None
            self.tail = iter
        else:
            iter.next = iter.next.next

    def remove_last(self):
        if self.head == None:
            return
        self.remove(self.length() - 1)

    def __str__(self) -> str:
        output = ""
        trav = self.head
        while trav != None:
            output += f'-->{str(trav.value)}'
            trav = trav.next
        return output


ll = SinglyLL()
ll.append(5)
ll.append(10)
ll.append_first(2)
ll.append_first(8)
ll.append(20)
ll.insert(5, 500)
ll.insert_multiple([1, 2, 3], 2)
ll.remove_first()
ll.remove_first()

print(ll)
ll.remove_last()
ll.append(1000)
print(ll)
