# 1. Introduction

They are simply another way to create functions also called anonymous functions
* the format is `lambda [parameter list }: expression ` the expression returns a function object 
* it can be assigned to a variable, or passed as an argument 
* they are all function objects that are not named 
## 2. Constraints
* the body of  lambda is limited to a single expression 
* NO assignments
* no annotations
* the expression must be a single line of code 
 
## 3. Using lambdas for sorting 

* the sorted function has the syntax `sorted(iterable,/,*/key=None,reverse=false)`
* in key for sorted we can give a lambda to calculate a value to sort by 
* you can also give a function that takes one argument and returns a value
* sorted in python is implemented as a stable sort 

##  
