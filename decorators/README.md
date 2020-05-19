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
	
## 3. Stacking decorators

* you can decorate a function with multiple decorators but the order with which you do this makes a huge difference in the output 
* can use both the normal return function and reassign to label method or the `@` notation 
* if make sure all the stacked decorators use wraps within them or the docstrings will get polluted
* the decorator in the top is called first and goes deeper into the stack or nesting 

## 4. Decorators with parameters

* use the decorator factory design nesting the decorator function in another closure that takes parameters to give context 
* using the @notation we are first constructing a decorator of the specified type passing the parameters to the decorator factory and then using it to decorate our function 
* don't give parameters to the decorator function definition because it will screw up the parameter order 

## 5. Decorators and classes

* the decorators can also be used to decorate the class methods and he `__call__` methods in  a class
* the classes can be used as decorators by using the `__init__` to act as the decorator factory and the `__call__` to act as the decorator because init is called only the first time and the 
  class data members set by init are available to the call method 
* so we can use a class rather than using closures


## 5. Applications of decorator 

Lets take a look at couple of applications for which we can use the decorator pattern 
*  make timers
*  counter and logger type things
*  used for checking constraints authentication and other kinds of checking before running a function or calling an api
*  it can be used for memoization or implementing a cache of sorts where the closure keeps track of values according to a specified metric 
*  there is a builtin function that can be used for memoization in functools called the lru_cache
	

