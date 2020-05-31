import sys
import os.path
import types
import sys



def import_(module_name,module_file,module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]
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

    return sys.modules[module_name]

print("Running custom importer")
