# https://practice.geeksforgeeks.org/problems/count-the-zeros2550/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1company[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays

arr = list(map(eval , input().split()))
ele = int(input())

def modified_binary_search(arr , ele):
    n = len(arr)
    ele = 1
    left  = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == ele:
            if arr[mid + 1] == 1:
                left = mid + 1
            else:
                return (n - mid - 1)
        elif arr[mid] > ele:
            left = mid + 1
        elif arr[mid] < ele:
            right = mid - 1
    return n


print(modified_binary_search(arr , ele))

