#  the int data type

* some languages have different types for different fixed length types 
* python can seamlessly use these without us knowing 
* theoretically only limited by the size of memory 
* larger numbers will use more memory and standard operators will take longer 

## 1. operators

* all operators between int returns int type, division returns float irrespective of whether it is perfectly divided
* `//`is integer division 
* a = b * (a // b) + (a % b)

## 2. constructors

* is and instance of the int class
* you can specify base from 2 - 36, default 10
* `bin() oct() hex()` to convert a number form its base to the other bases
* they will give strings with prefixes infront saying the base 
* so literal integers of the form a = 0b1010 or a = 0o01
* for other bases we need custom code 
* 36 is the max mase since pthon uses 0-9 and a-z for enconding 
* fraction module can be used to represent fractions in their denominator numerator form 

## 3. Fractions

## 4. Floats

## 5. float to int
* trunc() returns int portion 
* `int(<float>)` is sthe same operation 
* floor
* ceil
* round to the closest multiple of n round(x,n=0)
* use decimal to deal wih approximation issues in floats that use binary internal representation 

## 6. Decimal class

* they have a context that controls the aspects of working with decimals 
* this sets the precision during arithmetic operations and a rounding algorithm 
	* the context can be global or local 
	* decimal.getcontext() for global context
	* decimal.localcontext(ctx=None) returns a context manager which you can use with `with` to manage context
* use strings or tuples to make decimals 
	* `(<sign>,(digits,d1,d2,...dn),<exponent>)
	* context presision only effects the operations and not the constructor
	* Decimal(tuple)
	* performance considerations
	* not as easy to code
	* not al math functions exist for decimals 
	* takes much more memory 
	* much much slower than floats


	
