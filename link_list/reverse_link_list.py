# https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1/?company[]=Amazon&company[]=Amazon&problemType=functional&page=1&sortBy=submissions&query=company[]AmazonproblemTypefunctionalpage1sortBysubmissionscompany[]Amazon
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

    def reverse(self):
        prev = None
        curr = self.head
        next = self.head.next

        while curr != None:
            curr.next = prev
            prev = curr
            curr = next
            if next != None:
                next = next.next

        self.head = prev


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.reverse()
ll.display()