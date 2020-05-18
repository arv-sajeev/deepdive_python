
# Here is a counter function using closures 
def counter(init=0,inc=1):
    count=init
    def inner():
        nonlocal count
        count+= inc
        return count
    return inner

# Here is a logger that logs the number of times a function is used

def logger(fn,log_dict):
    count = 0;
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        print("called the {0} for the {1}th time ".format(fn.__name__,count))
        fn(args,kwargs)
        log_dict[fn.__name__] = count
    return inner       
    
