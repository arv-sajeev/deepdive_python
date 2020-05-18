# 1. Decorators 
The examples we saw in closure we take in a function as arguments and then add return a function that has extra functionality in addition to the additional functionalities of the original function, so we sort of are decorating the function.

*  decorator function takes a function as an argument and returns a closure
*  the closure uses optional positional and keyword args
*  runs some code in the closure and the calls the original function using the args passed
*  whatever is returned by that functional call

We can implement decorators using the return closure method, there is a dedicated notation to implement decorators 

## 2. The `@` notation 

* use using the @notation does the operation of passing the function as parameter end returning 
 the closure but this is done during the definition of the function
* doing this while introspecting the returned closure the name and docstring will be of the inner function of the decorator unless explicitly changed in the decorator
* the `functool.wraps` function in the functools module can be used to 
* the wraps function is itself a decorator, it does the copying metadata work 
* use the wraps decorator with the original function as parameter and use the `@` notation just before the definition of the inner function

## 3. Applications of decorator 

Lets take a look at couple of applications for which we can use the decorator pattern 
*  make timers
*  counter and logger type things
*  
	

