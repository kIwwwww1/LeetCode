# Время выполнения: O(n)
# Память: O(1)

class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next


head = Node(1, Node(2, Node(3, Node(4, None))))

def middle(head: Node) -> Node:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

data = middle(head)
print(middle(head))
