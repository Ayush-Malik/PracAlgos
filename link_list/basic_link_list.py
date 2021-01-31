class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self , data):
        if self.head == None: # LinkedList was empty
            self.head = Node(data)
        else: # There were some nodes present initially in LinkedList
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.display()