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

    def get_length_of_ll(self):
        temp = self.head
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        return length

    def nth_node_from_end(self , n):
        length = self.get_length_of_ll()
        temp = self.head

        x = 1

        if length - n < 0: # Means required node doesn't exist
            return -1

        while x <= length - n:
            temp = temp.next
            x += 1

        return temp.data


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.display()
print(ll.nth_node_from_end(1))