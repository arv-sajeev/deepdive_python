import gc
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def obj_by_id(obj_id):
    for obj in gc.get_objects():
        if id(obj) == obj_id:
            return "object exists"
    return "Not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A : self : {0}, b : {1}'.format(hex(id(self)),hex(id(self.b))))

class B:
    def __init__(self,a):
        self.a = a
        print('B : self : {0}, a : {1}'.format(hex(id(self)),hex(id(self.a))))

gc.disable()

my_var = A()

