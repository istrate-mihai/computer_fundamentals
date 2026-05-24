from random import randint
import time

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Node_Doubly:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self):
        self.top  = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top  = node
        else:
            self.top = node
        
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data 
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ("{", "[", "("):
            stack.push(ch)

        if ch in ("}", "]", ")"):
            last = stack.pop()

            if last == "[" and ch == "]":
                continue
            elif last == "(" and ch == ")":
                continue
            elif last == "{" and ch == "}":
                continue
            else:
                return False

    if stack.size > 0:
        return False
    else:
        return True

sl = (
 "{(foo)(bar)}[hello](((this)is)a)test",
 "{(foo)(bar)}[hello](((this)is)atest",
 "{(foo)(bar)}[hello](((this)is)a)test))"
)

# for s in sl:
#     m = check_brackets(s)
#     print("{}: {}".format(s, m))

# List based queues
class ListQueue:
    def __init__(self):
        self.items = []
        self.size  = 0

    def enqueue(self, data):
        self.items.append(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data

# Stack based queues
class StackQueue:
    def __init__(self):
        self.inbound_stack  = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                data = self.inbound_stack.pop()
                self.outbound_stack.append(data)

        return self.outbound_stack.pop()

# queue = StackQueue()
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# print(queue.inbound_stack)
# queue.dequeue()
# print(queue.inbound_stack)
# print(queue.outbound_stack)
# queue.dequeue()
# print(queue.outbound_stack)

# Node based queues
# A(head) <-> B(tail)
class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node_Doubly(data, None, None)

        if self.tail is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev  = self.tail
            self.tail.next = new_node
            self.tail      = new_node
        
        self.count += 1

    def dequeue(self):
        current = self.head
        
        if self.count == 1:
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None

        self.count -= 1
        return current

# Applications of queues
class Track:

    def __init__(self, title = None):
        self.title = title
        self.length = randint(5, 10)

track_1 = Track("white whistle")
track_2 = Track("butter butter")
print(track_1.length)
print(track_2.length)

class MediaPlayerQueue(NodeQueue):
    
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)

track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")
print(track1.length)
print(track2.length)
media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()
