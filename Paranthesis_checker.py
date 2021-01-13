# https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1


x = input().split()

def element_remover(arr , ele):
    for val in arr:
        if val == ele:
            arr.remove(ele)
            return True
    return False

def ispar(x):
    lis = []
    for i in range(len(x)):
        if x[i] == '[' or x[i] == '(' or x[i] == '{':
            lis.append(x[i])
        else: # Means x[i] is from => ']' , ')' , '}'
            if x[i] == ']':
                remove_ele = '['
            elif x[i] == ')':
                remove_ele = '('
            elif x[i] == '}':
                remove_ele = '{'
            if not element_remover(lis , remove_ele):
                return False

    if len(lis) == 0:
        return True
    else:
        return False

print(ispar(x))