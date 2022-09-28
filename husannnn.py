l1 = [1,2,3,4,5,6,7,8]
l2 = [2,3,4,5,6,7,8,9,90]
l3 = [33,44,55,66,77]

def get_max(royhat):
    max_n = 0
    for i in royhat:
        if i > max_n:
            max_n = i
    return max_n 

print(get_max(l1))
print(get_max(l2))
print(get_max(l3))