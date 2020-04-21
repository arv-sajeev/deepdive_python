# The Garbage collector 

## 1. Introduction 

* In python most of the cleanup is done by the python memory manager usng the number of references to an object. 
Objects are cleaned up when their reference count is 0. 
* This works for most cases but for circular references the count never reaches 0. 
* The garbage collector module takes care of cleaning up of circular references
* It is by default turned on but can be explicilty turned off for performance requirements and control it programmatically using the `gc` module

## 2. Caveat

* the gc module works fine for almost all cases but for python v.3.4 < it sometimes does not cleanup for a special case
* if even one of the objects has a destructor it would mean that their was importance in the order that the objects dextructors are called
* the gc thus marks this uncollectable and does not process it, resulting in a memory leak

## 3. Work with it 

* use the script demo1.py to learn more
* execute it from the command line using
* exec(open("demo1.py").read())
* it contains code to set up a circular reference with classes A and B 
* disables the gc
* use the `ref_count` and `obj_by_id` to find reference count and whether gc is keeping track of it 
* you can run gc manually using gc.collect()
* you can enable it using gc.enable()


