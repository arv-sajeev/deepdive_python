from functools import reduce
l = [1,2,3,4,5,6,6,7,8,9]

min_value = lambda a,b : a if a <b else b
max_value = lambda a,b : a if a >b else b
add       = lambda a,b : a+b

def _reduce(fn,sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result,x)
    return result 
