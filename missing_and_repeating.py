# https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Arrayscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Arrays
arr = list(map(eval , input().split(', ')))
n   = len(arr)

def find_repeating_and_missing_elements(arr , n):
    missing_ele   = -1
    repeating_ele = -1

    for i in range(len(arr)):
        arr[ arr[i] % (n + 1) - 1] += (n + 1)

    for i in range(len(arr)):
        count = arr[i] // (n + 1)
        if count == 0:
            missing_ele = i + 1
        elif count == 2:
            repeating_ele = i + 1

    return [repeating_ele , missing_ele]


print(find_repeating_and_missing_elements(arr , len(arr)))