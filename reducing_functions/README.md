# Introduction

Functions that recombine an iterable recursively ending up with a single return value are called reducing functions or aggregators or folding functions, finding the maximum value of a function or average are examples 

## 1. Reducing functions in python 

* Python implements the reduce function that  will handle any iterable
* it is in the functools module 
* reduce works on any iterable 
* there are many builtin reducing functions like min,max,any,sum etc.

## 2. The reduce initializer

* the reduce function has a third optional parameter initializer,which is used to handle the case when the iterable is empty
* it adds a default in the case the iterable is empty 
* choose defaults properly since it will effect the value of the reduce function for all cases

 

