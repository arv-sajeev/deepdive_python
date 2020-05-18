# 1. Introduction 

* If a variable is used in a code block but not defined there and is not a global variable either it is called a free variable. 
* A closure is a way to bind data and a function sort of like keeping the context of the function 

## 2. Returning inner functions

* when we return an inner function we are returning the closure of the function complete with its context
* closure is implemented using python cells as an intermediary object, to share the variable between two different scopes 
* the cell will point to the actual object and the other variables can access this using an indirect reference
* so a closure can be thought of as a function plus an extended scope that contains free variables
* the free variables value is the object the cell points to, so python looks up the cell object and then whatever the cell is pointing to
* we can use the introspection tools to inspect a function, `fn.__code__.co_freevars` and `fn.__closure__` this gives the cell implementation 

* every time we run a function a new scope is created, if the function creates a closure a new closure is created every time as well 

* we can share scopes by returning inner functions together to get the same closures
* the closure is created when the function is created but the values are evaluated only when the functions are called
* so be careful when using closures

## 3.Nested closure

* you can nest closures, just in case you haven't guessed by now

## 4.Closure application 

* we can use closures as a sort of alternative for implementing class variables in functions instead of classes
* counters loggers and other stuff
 
