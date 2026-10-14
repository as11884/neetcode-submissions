class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1 

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        newNode = ListNode(val)
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        nextNode = cur.next
        newNode.next = nextNode
        cur.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        self.size -= 1
