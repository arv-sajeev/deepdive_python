default_log_dict  = {}
default_memo_dict = {}

def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)  # copying metadata
    def inner(*args,**kwargs):
        start  = perf_counter()
        ret    = fn(*args,**kwargs)
        end    = perf_counter()
        e_time = end - start

        args = [str(arg) for arg in args]
        kwargs = ["{0} = {1}".format(k,v) for (k,v) in kwargs.items()]
        args_list = args+kwargs
        args_str  = ",".join(args_list)
        print("Calling {0} with parameters {1} took ::{2}".format(fn.__name__,args_str,e_time))
        return ret
    return inner


def logged(fn,log_dict=default_log_dict):
    from datetime import datetime,timezone
    from functools import wraps
    count = 0
    @wraps(fn)
    def inner(*args,**kwargs):
        nonlocal count
        dt = datetime.now(timezone.utc)
        ret = fn(*args,**kwargs)
        count += 1
        log_dict[fn.__name__] = count
        print("Function :: {0} called at :: {1} \n\thas been called {2} times".format(fn.__name__,dt,log_dict[fn.__name__]))
        return ret
    return inner   

def memoize(fn,memo_dict=default_memo_dict):
    from functools import wraps
    wraps(fn)
    def inner(n):
        if n not in memo_dict:
            print("Had to populate the memo")
            memo_dict[n] = fn(n)
        return memo_dict[n]
    return inner 


@logged
@memoize
def recursive_fib(n):
    if (n < 2):
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

def loop_fib(n):
    a = 1
    b = 1
    for i in range(3,n+1):
       a,b = b,a+b
    return b
@logged
@timed
def fibo1(n):
   return loop_fib(n)

@logged
@timed
def fibo2(n):
   return recursive_fib(n)


 
