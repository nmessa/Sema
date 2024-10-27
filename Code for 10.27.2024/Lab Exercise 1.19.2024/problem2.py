##Lab Exercise 1.19.2024 Problem 2
##Author: nmessa

def is_strange_pair(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) == 0 and len(s2) > 0:
        return False
    if len(s1) > 0 and len(s2) == 0:
        return False
    if s1[0] == s2[-1] and s1[-1] == s2[0]:
        return True
    else:
        return False

print(is_strange_pair("ratio", "orator"))
print(is_strange_pair("sparkling", "groups"))
print(is_strange_pair("bush", "hubris"))
print(is_strange_pair("", ""))

##Output
##True
##True
##False
##True
