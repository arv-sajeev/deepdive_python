import platform as p
import sys

print(p.python_implementation())

# integer interning 

a = 256
b = 256
print(a is b)

a = 257
b = 257
print(a is b)
# string interning 

a = "hello_world"
b = "hello_world"
print(a is b)

a = "hello world"
b = "hello world"

print (a is b)

a = sys.intern("hello world")
b = sys.intern("hello world")
v = "hello world"
print(a is b)
print(a is v)

