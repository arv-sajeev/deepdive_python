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
