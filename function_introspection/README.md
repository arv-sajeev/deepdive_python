# Function introspection 



* Functions are first class objects
* so they have their own default attributes and we can attach attributes to then as well
* we can look at the attributes of any first class object by using the `dir` function
* we can use these attributes to introspect the function 
* an attribute that is callable is called a method 


## 1.`inspect` module

* the inspect module has many functions that can be used to introspect a function 
* `isfunction()` and `ismethod()` to find if method or function 
* you can introspect the source code using `inspect.getsosurce(<routine_name>)`   
* `inspect.getmodule()`, `inspect.signature()`
* some python builtin functions can define postional only arguments  

