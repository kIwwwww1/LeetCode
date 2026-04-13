# Время выполнения: O(n)
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

head = Node(1, Node(2, Node(3, Node(4, None))))

def reverse(head: Node) -> Node:
    prev = None
    current = head

    while current:
        tmp = current
        current = current.next
        tmp.next = prev
        prev = tmp
    return prev

print(reverse(head))