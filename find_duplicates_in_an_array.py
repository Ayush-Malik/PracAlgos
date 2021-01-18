# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=solved&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatussolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays
arr = list(map(eval , input().split(',')))
n = len(arr)

temp_lis = []
for i in range(n):
    temp_lis.append(1)

for i in range(n):
    arr[arr[i] % n] += n

ans_lis = []
for i in range(n):
   if arr[i] // n >= 2:
       ans_lis.append(i)

print( ans_lis if len(ans_lis) != 0 else [-1] )
