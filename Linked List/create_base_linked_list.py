class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, None)))