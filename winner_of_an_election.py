# https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1/?category[]=Strings&category[]=Strings&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=Accolite&problemStatus=unsolved&problemType=functional&page=1&sortBy=submissions&query=category[]Stringscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]AccoliteproblemStatusunsolvedproblemTypefunctionalpage1sortBysubmissionscompany[]Amazoncompany[]Microsoftcompany[]Adobecompany[]Samsungcompany[]Accolitecategory[]Strings#
def second_string_is_lex_smaller(a , b):
    for i in range(min(len(a) , len(b))):
        if ord(a[i]) < ord(b[i]):
            return False
        elif ord(a[i]) > ord(b[i]):
            return True

    if len(a) < len(b) :
         return False
    else:
        return True


def _(arr):
    dic = dict()
    max_val = 1
    for val in arr:
        if val in dic.keys():
            dic[val] += 1
            max_val = max(max_val , dic[val])
        else:
            dic[val] = 1

    ans = ''
    for key in dic.keys():
        if dic[key] == max_val:
            if ans == '' or second_string_is_lex_smaller(key , ans):
                ans = key


    return ans , dic[ans]
arr = list(input().split())
print(_(arr))
