# 1. First order functions 

## 1. Introduction 

* can be defined as anything that can be passed to a function as argument
* all the things we've  seen till now are first class
* functions are first class objects as well
* higher order functions either take function as an argument or return a function as an argument
  
## 2. Doc strings and annotations 
* we can document a function using doc strings PEP 257
* If the first line in the function body is a string it will be interpreted as a doc String
* multi line strings literals can be used as well
* the doc strings are stored in the `__doc__` this can be accesses using the dot notation or using the kelp function 
* we can annotate the function with its arguments and returns as well
* `def func(a : <doc_1> ,b : <doc_2> ) -> <return_doc>`
* these are not stored in the `__doc__`  and can only be accessed using help()
* you can use any expression in an annotation using function concatenate, this expression will be evaluated when the function is defined 
* they are stored in the `__annotations__` property, it is a dictionary with keys as the parameter names 
* sphinx can be used for documentation automation
* type hints can be used for type checking using tools 

   
