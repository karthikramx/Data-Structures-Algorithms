class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        first_node = Node(value)
        self.head = first_node
        self.tail = first_node
        self.length = 1


if __name__ == '__main__':
    LL = LinkedList(4)
    print(LL.head.value)


    

