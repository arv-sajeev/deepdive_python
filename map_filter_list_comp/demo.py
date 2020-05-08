def sq(x):
    return x**2

l = [1,2,3,4]

l2 = list(map(sq,l))

def is_even(x):
    return x%2

l3  = list(filter(is_even,l))
