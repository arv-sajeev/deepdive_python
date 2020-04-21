# Python optimizations


## 1. Version of python 
	* There are multiple versions of python dependinig on what language it is implemented in
	* CPython which you probably will have if its a GNU distribution written in C
	* Jython in Java
	* IronPython written in C#
	* PyPy written in RPython which is a statically type version of Python wriiten in C designed to write interpreters

## 2. Interning 
	* reusing objects on demand
	* at startup Python pre load a global list of integers from -5 to 256
	* any time an integer is references in that range it will be made to that global list
	* The integers in this range are singleton objects
	* The small integers show up often and low startup overhead and memory wastage

## 3. String interning 

	* some strings are interned but not all 
	* all strings that fit the identifier definiton are interned 
	* variable names, function names, class names keywords etc
	* anything that fits the format as well
	* its all about optimization, it makes string equality mush more faster 
	* you can force tring to be internes using a = sys.intern('the quick brown fox')
	* you could use it for reducing memory overhead

## 4. Peephole optimization 
	
	* a vareity of optimizations that occur during compile time 
	* numerical calculations that are repeated 
	* constant expressions that are less than 20 characters
	* tradeof of memory and speed
	* in membership tests mutables are replaced to immutables `set ->frozen tests,list-> tuples`
	* set membership is much faster that list or tuple since it uses hashmap internallly
	* 
