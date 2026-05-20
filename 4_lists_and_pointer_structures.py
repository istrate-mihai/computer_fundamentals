# Singly linked list
# A(tail) -> B(head)
class Node_Single:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
            return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node_Single(data)

        if self.head:
            self.head.next = node
            self.head      = node
        else:
            self.tail = node
            self.head = node
        
        self.size += 1

    def iter(self):
        current = self.tail

        while current:
            value   = current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        prev    = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next

                self.size -= 1
                return

            prev    = current
            current = current.next

    def search(self, data):
        for node_value in self.iter():
            if node_value == data:
                return True

        return False

    def clear(self):
        self.head = None
        self.tail = None

words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

# Client code should not interact with node objects
# current = words.tail
# while current:
#     print(current.data)
#     current = current.next

# We use a generator instead
for word in words.iter():
    print(word)

# Doubly linked list
# A(head) <-> B(tail)
class Node_Doubly:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node_Doubly(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev   = self.tail
            self.tail.next  = new_node
            self.tail       = new_node

            self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head      = current.next
            self.head.prev = None
            node_deleted   = False
        elif self.tail.data == data:
            self.tail      = self.tail.prev
            self.tail.next = None
            node_deleted   = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted      = True
                current = current.next

        if node_deleted:
            self.count -= 1

    def iter(self):
        current = self.head

        while current:
            value   = current.data
            current = current.next
            yield value

    def search(self, data):
        for node_value in self.iter():
            if node_value == data:
                return True
        return False

# Circular Lists
# Is a special case of linked list where the last node points back to the first node
# It can be based on both singly or doubly linked lists
# Singly Circular Linked List
# A(tail) -> B(head)
class SinglyCircularLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node_Single(data)

        if self.head:
            self.head.next = node
            self.head      = node
        else:
            self.tail = node
            self.head = node

        self.head.next = self.tail
        self.size += 1

    def iter(self):
        current = self.tail

        while current:
            value   = current.data
            current = current.next
            yield value

    def delete(self, data):
        current = self.tail
        prev    = self.tail

        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail      = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next

                self.size -= 1
                return

            prev    = current
            current = current.next

    def search(self, data):
        for node_value in self.iter():
            if node_value == data:
                return True

        return False

    def clear(self):
        self.head = None
        self.tail = None

words = SinglyCircularLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')

counter = 0
for word in words.iter():
    print(word)
    counter += 1
    if counter > 1000:
        break
