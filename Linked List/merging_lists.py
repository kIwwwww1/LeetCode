# Время выполнения: O(n+m)
# Память: O(1)

class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        result = []
        curr = self
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return " -> ".join(result)


head1 = Node(1, Node(2, Node(3, Node(4, Node(10, None)))))
head2 = Node(2, Node(2, Node(7, Node(8, None))))

def merge(head1: Node, head2: Node) -> Node:
    dummy = Node(0, None)
    curr = dummy
    while head1 and head2:
        if head2 is None or (head1 is not None and head1.data <= head2.data):
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    curr.next = head1 or head2
    return dummy.next

print(merge(head1, head2))