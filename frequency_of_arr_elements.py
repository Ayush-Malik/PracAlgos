# https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays
# 2,3,2,3,5
# [0, 2, 2, 0, 1]


arr = list(map(eval , input().split(',')))

n = len(arr)
for i in range(n):
    index = arr[i] % (n + 1)
    arr[index - 1] += (n + 1)

for i in range(n):
    arr[i] = arr[i] // (n + 1)

print(arr)
