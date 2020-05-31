# Modules Packages and namespaces 

Modules are objects of type Module and are used for organizing code and namespaces

## 1. What is a module 

It is a just  an object of type module, it is loaded when import is called and will be visible in globals(), and act as a container of global variables and has an execution environment associated with it 

## 2. Importing modules

* unlike other languages like C where modules are compiled and linked during compile time - in python import is done during runtime

* the module keeps track of the code that is pointed to by the module

* the `sys` module has a few attributes that defines where python is going to look for modules sys.prefix points to where most of the builtin are stored , while creating a venv  the prefix is changed the `exec_prefix` hold the path to the main directories that hold all the modules 

* when you import a module, python will search for the module in the  contained sys.path
* if not found it will fail 
* there is also the sys.modules which acts as a cache to see if the module has been imported - if so it simply uses the reference in there otherwise
* other wise it create a new module object
* loads the source code after searching for the module in the sys.path
* adds an entry into sys.modules with name as key
* the code is also compiled and executed so anything that is not a definition gets executed
* it generally only happens once for a program, if imported twice it doesn't execute it again

## 3. Imports and importlib

* finding where the code is the most complicated part
* importlib is a package that we can use for importing functionality
* `<mod_vairable> = importlib.import_module(<mod_name>)`
* modules can be builtins, in python files, in zip files, in wheels
* for working with such a large variety of formats the importer is quite complex
* it has two part the **finders** and the **loaders**
* the finders are used to find where the requested modules source code resides 
* finders return the modules spec 
* you can find the finders with `sys.meta_path`
* we can add a path to the default paths by using `sys.path.append(<new_path>)`

