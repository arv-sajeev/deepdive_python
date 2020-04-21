def process(s):
    print ("Intial s address is s [{0}]".format(hex(id(s))))
    s = s + "poop"
    print ("Intial s address is s [{0}]".format(hex(id(s))))

def process_list(s):
    print ("Intial l address is  [{0}]".format(hex(id(s))))
    s.append("poop")
    print ("Intial l address is [{0}]".format(hex(id(s))))

def square(a):
    print ("In square")
    return a**2

def cube(a):
    print("In cube")
    return a**3

def select_function(fn_id):
    if (fn_id == 1):
        return square
    if (fn_id == 2):
        return cube


s = "adarsh"
print ("Intial s address is s [{0}]".format(hex(id(s))))
process(s)
s = [1,2,3]
print ("Intial l address is  [{0}]".format(hex(id(s))))
process_list(s)
f = select_function(1)
print(f(2))
print(select_function(2)(3))
