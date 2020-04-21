# Object mutability

## 1. Introduction 
	* Changing the data inside an object is called modifying the internal state or mutating the object
	* so an object whose internal state can be changed is called mutable and that cannot be changed is called immutable
	* so by this definition int, float, booleans are all immutable since we never modify internal state but just assign a new object for modification 
	* strings,tuples and frozen sets, and user defined classes
	* mutable objects - lists,sets,dictionaries, and user defined classes
	* putting mutable objects within immutable objects, like lists within a tuple is stupid.
	* when using .append we are modifying the lists internal structure
	* but when using list + s we are creating a new object with the specified value
	* immutable objects are safe from uninteded sie effects
	* when using lists which are mutable dont use append when you dont want to mutate the original list
	* all function arguments are passed by reference

## 2.Shared reference and mutability
	* the concept of two variables referencing the same object in memory
	* python's memiry manager automatically decides to reuse references to values that more than one variable has
	* this is safe since all these objects are immutable, so its sort of safe
	* shared references to mutable objects is probably not a good ides 
	* the memory manager doesn't do shared references automatically for mutable objects

## 3. Variable equality
	* we can compare two variables using 
	* equality of memeory address (using the is operator or not is) dot use this cause its not always true
	* using the objects state (using the == operator or !=)
	* the python memory manager uses shared references to assign the None object
	
## 4. Everything is an object
	* every thing is an object, even functions, 
	* you can use `help(<class-name>)` to fin documentation of in built classes
