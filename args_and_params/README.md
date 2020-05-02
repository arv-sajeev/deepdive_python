# Parameters vs arguments

* when you define a function the variables in the signature are called parameters, these are nothing but local variables 

* the values you pass to a function when you call it are called arguments, these are passed by reference, so take care of passing mutable variables 

* you could call em whatever you want 

## Positional and keyword arguments

* positional arguments are the ones that you usually use
* you could give default values assigning the parameter with the default value in the signature
* if a positional parameter is given a default value,rest of the positional params following it must be given default values as well
* in keyword arguments give the names of the parameters in the function call instead of using position to pass 
* once you use a keyword argument all arguments after must be named too


## Packed values

* The act of splitting packed values into individual variables contained in a list or tuple
* a , b = 10 ,20
* a , b is a tuple so is 10,20
* a , b = b, a, this is alright since the entire rhs is evaluated before assignments to lhs are made
* when you unpack a dict it is the keys that are unpacked
* dictionaries and sets are unordered so unpacking will be random as well

## Extended unpacking

* `a,*b = l`, unpacks the first element to a and the rest of the iterable is unpacked into b
* you can also put unpack for last `a,*b, c = 1,2,3,4,4` 
* we can also use it in the left hand side of the rhs
* using rhs `[*l1,*l2]` we can unpack the any iterable, for unordered it probably wont have meaning 
* we can unpack the key-value pairs of dictionaries by using the `**` operator 
* same keys will have their values overwritten using the above operator 

## nested unpacking

* `a,b,(c,d) = [1,2,[3,4]] and we'll get all the elements jsust look you''ll understand
* you could do all this stuff using slicing but that is for lists only usually

## we can use the unpacking idea for variable argument functions

* the unpacking will be done to a tuple
* so we just add a *args to have variable number of argument funcitons
* it exhausts positional arguments
* so no positional arguments after
* good way for zero division check `x and y/x`
* you can unpack arguments into the parameters using *l in the function call



##Keyword args

* we can make keyword arguments mandatory by exhausting the positional arguments by using *args in the signature, all the parameters that follow it are mandatoyr keyword arguments
* 

