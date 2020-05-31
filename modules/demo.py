
print("{0} is up and running".format(__name__))


# how sys.module is used to cache
import sys
import os.path
import types
import sys
import importer



sys.modules['appi'] =   lambda :    print("adarsh")
import appi
appi
appi()
print("\n\n--------------------------------------------------\n")
# import module1
# module1.print_dict('main.globals',globals())

'''
module_name = "module1"
module_file = "module1.py"
module_path = "."

##### This part does what import does

module_rel_path = os.path.join(module_path,module_file)
module_abs_path = os.path.abspath(module_rel_path)

# Read the file
with open(module_rel_path,'r') as src_file:
    src_code = src_file.read()
#Create a module object
m           = types.ModuleType(module_name)
m.__file__  = module_abs_path

#set up a reference in sys.modules
sys.modules[module_name] = m

#compile the source code

obj_code = compile(src_code,filename = module_abs_path,mode='exec')

# assign the namespace of the 
exec(obj_code,m.__dict__)
'''

####### Import is done

m = importer.import_("module1","module1.py",".")
m.print_dict('main.globals',globals())

print("\n\n--------------------------------------------------\n")
