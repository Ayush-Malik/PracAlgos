# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays#
arr = list(map(eval , input().split(',')))
req_sum = int(input())
n = len(arr)


curr_sum = 0
ptr = -1
for i in range(n):
    curr_sum += arr[i]
    if curr_sum > req_sum:
        while ptr < i and curr_sum > req_sum:
            ptr += 1
            curr_sum -= arr[ptr]

    if curr_sum == req_sum:
        print(ptr + 2 , i + 1)
        break