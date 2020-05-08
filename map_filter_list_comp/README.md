#Introduction 
 
* a function that takes a function as parameter or returns a function as return value are called higher order functions


## 1.map
* the map function, `map(func,*iterables)` where `*iterables` is a variable number of iterable objects 

* func is a function that takes as many arguments as there are iterables objects

* map will then return an iterator that calculates the function applied to each element of the iterables 

* the iterator stops as soon as one of the iterables  is exhausted so unequal length iterables can be used

* the iterable returned has to be made to a list to access it 

## 2,filter

* it takes a single iterable and processes it with the function provided to decide which to retain 
* `filter(func,iterable)`

## 3.zip 

* it is a first order function that takes a list of iterables and makes a list of tuples combining the index wise elements of each iterable

* it only works until at least one of the iterables exhausts

* the zip function is a generator function so unless you change it to a list we cant use the same variable to access the comprehension after using up the entire iterable you can use list to save it into a list rather than use a generator 

## 4. List comprehension as an alternative for map 

* `[x**2 for x in l]` is the 
* use zip when you want to use list comprehension on multiple iterables  
* using the `[fact(x) for x in tange(10)]` we get an actual list as the result of the comprehension instead if we use (fact(x) for x in range(10)) it returns a generator object
* we can use list comprehension on more than one iterable using zip on the iterables 
* we can also do the function of a filter by giving an if function after the zip  
