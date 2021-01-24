# https://practice.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1/?category[]=Mathematical&category[]=Arrays&category[]=Strings&category[]=Mathematical&category[]=Arrays&category[]=Strings&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Mathematicalcategory[]Arrayscategory[]Stringscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Mathematicalcategory[]Arrayscategory[]Strings

def isRotated(a , b):
    #code here
    if len(a) != len(b):
        return False

    # Now if len(a) == len(b)
    n = len(a)
    # Checking first combination when first two characters are moved to end in string(a) to obtain string(b)
    for i in range(len(a)):
        if a[(i + 2) % n] != b[i]:
            break
    else:
        return True

    # Checking second combination when last two characters are moved ot front in string(a) to obtain string(b)
    for i in range(len(a)):
        if a[(n - 2 + i) % n] != b[i]:
            break
    else:
        return True

    return False


print(isRotated(input() , input()))