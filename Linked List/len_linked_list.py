# Время выполнения: O(n)
# Память: O(1)

class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

head = Node(1, Node(2, Node(3, Node(4, None))))
head = Node(1,None)
head = Node(1,Node(2, None))

def size(head: Node):
    count = 0
    current = head

    while current:
        count +=1 
        current = current.next
    return count

print(size(head))
    
