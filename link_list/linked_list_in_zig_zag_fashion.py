# https://practice.geeksforgeeks.org/problems/linked-list-in-zig-zag-fashion/1/?category[]=Linked%20List&category[]=Linked%20List&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemType=functional&page=1&query=category[]Linked%20Listcompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemTypefunctionalpage1company[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Linked%20List#

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

def zigzag(head_node):
    # Complete this function
    temp = head_node
    x = 1
    while temp.next != None:
        if x % 2 != 0:
            if temp.data > temp.next.data:
                temp.data , temp.next.data = temp.next.data , temp.data
        else:
            if temp.data < temp.next.data:
                temp.data , temp.next.data = temp.next.data , temp.data
        x += 1
        temp = temp.next
    return head_node

def traverse(head):
    while head != None:
        print(head.data)
        head = head.next

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
new_head = zigzag(ll.head)

print("After converting to zig-zag fashion!!!")
traverse(new_head)