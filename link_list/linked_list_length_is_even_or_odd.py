# https://practice.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1/?category[]=Linked%20List&category[]=Linked%20List&page=1&query=category[]Linked%20Listpage1category[]Linked%20List#
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


def linked_list_length_is_even_or_odd(head):
    temp = head
    while temp != None:
        if temp.next != None and temp.next.next != None:
            temp = temp.next.next
        else:
            break
    if temp.next == None:
        print("ODD")
    else:
        print("EVEN")

ll = LinkedList()
ll.insert(36)
ll.insert(10)
ll.insert(40)
ll.insert(5)
ll.insert(50)
ll.display()

linked_list_length_is_even_or_odd(ll.head)
