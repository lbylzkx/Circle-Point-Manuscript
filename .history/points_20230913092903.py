def get_x_n(i):
    if i==1:
        return 1
    else:
        return get_x_n(i-1)+4

def get_y_n_(i):
    if i==1:
        return 1
    else:
        return get_y_n(i-1)+3

def two(n):
    return 1/2**n



#Tests
# print(two(1),two(2),two(3),two(4),two(5))
