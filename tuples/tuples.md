# Tuples 

They are basically read only lists, the position of values has meaning. 
* They are containers
* order matters
* can be heterogeneous
* indexable
* iterable
* immutable
* fixed length
* fixed order
* it's used as a data record
* we are guaranteed the data and data structure will never change 

## 1. Named tuples

* a method to make code more readable, instead of using classes for simple data records
  without methods embedded
* also the tuples will be immutable
* so we can use tuples to implement simple data structures 
* `namedtuples` are a subclass of tuple `from collections import namedtuple` namedtuple is  
* an instance of the returned class will still be a tuple
* namedtuple needs the classname we want to use and the sequence of field names 
* the field names cannot start with an underscore
* field names can be passed as sequences like lists or tuples or a single string separated by whitespace or commas
* it also sets up the eq and repr functions
* also we can instantiate a tuple calling keyword args
* we can access data using field names in addition to the normal tuple data access methods
  like index, slicing etc.
* the field names are stored in `_fields` 
* a named tuple can be used to create a dictionary using `as_dict`

## 2. Modifying and extending 

* you can't actually change the values inside a tuple so we can create a new tuple with the modified values 
* the easiest way is use `_replace` using keyword names to specify the values that we want to modify
*  extending tuples means appending the one or more fields of tuples 
* get the fields of the original tuple using the `_fields` property and add to it now use this to set up extend and create a new tuple


## 3. Documentation in tuples

* just override the `__doc__` values of things you want to document
* namedtuple doesn't provide any method to define default value, the two methods used are 
* using a prototypeo

## 4. Tuples as an alt dictionary
* from python 3.6 onwards using `dict.keys()` will give the keys back in the order that they were inserted in. This applies to the values as well
* so create a namedtuple with the keys use this prototype to fill in the values of the dict
* 
