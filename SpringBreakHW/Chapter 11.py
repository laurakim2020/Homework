#Question7
def dot_product(u, v):
    if len(u) != len(v):
        return 0
    return sum(i[0]*i[1] for i in zip(u, v))

print(dot_product([1, 1], [1, 1]))
print(dot_product([1, 2], [1, 4]))
print(dot_product([1, 2, 1], [1, 4, 3]))


#Question6
def scalar_mult(s, v):
    for i in range(len(v)):
        v[i]=v[i]*s
    return v

print(scalar_mult(5, [1, 2]))
print(scalar_mult(3, [1, 0, -1]))
print(scalar_mult(7, [3, 0, 5, 11, 2]))












