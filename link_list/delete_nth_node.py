class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self , data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def delete_nth_node(self , n):
        x = 1
        temp = self.head
        if n == 1:
            self.head = temp.next
        while x < n - 1:
            x += 1
            temp = temp.next
        temp.next = temp.next.next


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.display()
ll.delete_nth_node(1)
ll.display()