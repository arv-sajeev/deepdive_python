# Here is a logger that logs the number of times a function is used

default_dict = {}

def logger(fn,log_dict=default_dict):
    count = 0;
    def inner(*args,**kwargs):  # Note that here we are packing all the arguments to a tuple
        nonlocal count
        count += 1
        print(args)
        print(kwargs)
        print("called the {0} for the {1}th time ".format(fn.__name__,count))
        ret = fn(*args,**kwargs)
        log_dict[fn.__name__] = count
        return ret
    inner.__name__ = fn.__name__
    inner.__doc__  = fn.__doc__
    return inner       
    

@logger
def  say_heyyo(*args,**kwargs):
    print("Say Heyyo {0}".format(args[0]))
    
