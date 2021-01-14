# https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays#

arr = list(map(eval , input().split(', ')))

ptr_1 = 0
x = 0
for ptr_2 in range(1 , len(arr)):
    if arr[ptr_1] != arr[ptr_2]:
        ptr_1 += 1
        arr[ptr_1] = arr[ptr_2]
        x += 1


print(arr[0 : x + 1])