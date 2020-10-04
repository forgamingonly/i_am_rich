class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, key):
        node = self.head
        if node is None:
            self.head = self.tail = Node(key)
            self.tail.previous = self.head
            return

        self.head = Node(key)
        self.head.next = node
        node.previous = self.head

    def remove(self, key):
        if self.head is None:
            return

        if self.head.key == key:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next

    def pop(self):
        old_node = self.tail
        self.tail = old_node.previous
        self.tail.next = None
        return old_node.key

    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

class LRU_Cache:
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dictionary = dict()
        self.capacity = capacity

    def get(self, key):
        value = self.dictionary.get(key)
        if value:
            return value
        else:
            return -1

    def set(self, key, value):
        if self.dictionary.get(key):
            return

        if self.capacity == self.list.size():
            old_key = self.list.pop()
            del self.dictionary[old_key]

        self.list.remove(key)
        self.list.prepend(key)
        self.dictionary[key] = value


# Test Cases
our_cache = LRU_Cache(5)
our_cache.set(1, 11)
our_cache.set(2, 22)
our_cache.set(3, 33)
our_cache.set(5, "Not a number")
our_cache.set(None, 42)


print(our_cache.get(1))
# returns 11

print(our_cache.get(2))
# returns 22

print(our_cache.get(3))
# returns 33

print(our_cache.get(5))
# returns "Not a number"

print(our_cache.get(None))
# return 42

our_cache.set(10, 99)

print(our_cache.get(1))
# returns -1 , because 1 was least recently used so it was popped out

print(our_cache.get(2))
# returns 2

print(our_cache.get(3))
# returns -1

print(our_cache.get(5))
# returns "Not a number"

print(our_cache.get(None))
# return 42
