# Время выполнения: O(n)
# Память: O(1)

class Node:
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next

head = Node(1, Node(2, Node(3, Node(2, Node(1, None)))))

def middle_node(head: Node) -> Node:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse_list(head: Node) -> Node | None:
    curr = head
    prev = None
    while curr:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

def is_palindrome(head: Node) -> bool:
    first_helf_end = middle_node(head)
    second_half_begin = reverse_list(first_helf_end)
    p1, p2 = head, second_half_begin
    while p2:
        if p1.data != p2.data:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

print(is_palindrome(head))