class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def printLinkedList(self):
        temp = self.head
        if temp is None:
            print("Empty List")
            return
        while temp.next is not None:
            print(f"{temp.val} -> ", end="")
            temp = temp.next
        print(temp.val)  

    def convertToLinkedList(self, array):
        if len(array) == 0:
            print("Empty Array")
            return
        if self.head is not None:
            print("The Linked List is already populated")
            return

        self.head = Node(array[0])
        temp = self.head
        for i in range(1, len(array)):
            temp.next = Node(array[i])
            temp = temp.next

def test_linked_list():
    # Create empty list
    ll = LinkedList()
    print("Test 1: Empty list print")
    ll.printLinkedList()  # should print "Empty List"

    # Convert array to linked list
    print("\nTest 2: Populate with [10, 20, 30, 40]")
    ll.convertToLinkedList([10, 20, 30, 40])
    ll.printLinkedList()  # should print 10 -> 20 -> 30 -> 40

    # Try converting again (should give warning)
    print("\nTest 3: Try converting again")
    ll.convertToLinkedList([1, 2, 3])  # should print "already populated"

    # Check empty array case
    print("\nTest 4: Empty array input")
    ll2 = LinkedList()
    ll2.convertToLinkedList([])  # should print "Empty Array"

if __name__ == "__main__":
    test_linked_list()
