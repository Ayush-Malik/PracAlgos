# https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1/?category[]=Linked%20List&category[]=Linked%20List&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Linked%20Listcompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Linked%20List
class Node:
    def __init__(self , data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self , data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)
            self.tail = temp.next

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

def findIntersection(head1,head2):
    #return head
    counter = 0
    ll = LinkedList()

    while head1 != None:

        while head2 != None and head2.data <= head1.data:
            if head1.data == head2.data:
                if ll.tail == None :
                    ll.insert(head1.data)
                else:
                    if ll.tail.data != head1.data:
                        ll.insert(head1.data)
            head2 = head2.next
        head1 = head1.next

    return ll.head


ll1 = LinkedList()
ll2 = LinkedList()

ll1.insert(1)
ll1.insert(2)
ll1.insert(3)
ll1.insert(4)
ll1.insert(6)

ll2.insert(2)
ll2.insert(4)
ll2.insert(6)
ll2.insert(8)

head3 = findIntersection(ll1.head , ll2.head)

while head3 != None:
    print(head3.data)
    head3 = head3.next