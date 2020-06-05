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

## 4. Import variants

### a. `import <module-name>` 
* first checks sys.modules if the module exists already
* if not it is loaded
* then a symbol is added to the global namespace of the importing file
* this symbol references the module object in sys.modules

### b. `import <module_name> as <alias>`
* check sys.modules and loads reference if required
* a symbol with alias name is added which references the module in sys modules

### c. `from <module_name> import <object-name>`
* is math is sys.modules if not load it and insert reference
* add a symbol for object name in global namespace referencing `<module-name>.<object-name>`
* the module name is not in the global namespace
* we can do this using the alias method as well

In every case when an object from a module has to be referenced the entire module has to be loaded to sys.modules.

Using `from <module> import *` is usually a bad idea since it'll completely pollute the namespace since the namespace will have the object names loaded and not `<module>.<object_name>`

## 5. Reloading modules
* we can force python to reimport by deleting the objects from sys.modules and import it again
* but this can lead to problems since other files that have reference to the module already imported don't have it's address updated in the namespace since the object reference is in the global namespace
* instead we can use the `importlib` module for functions related to module
* the reload function in importlib reloads the module but the address of the object is kept the same 

## 6. The `__main__`
* the `__name__` property of a file is set to `__main__` if it is is the entry point for execution of the program
* when you call functions of other modules from a function the value of `__name__` in the module will be the file name
* We can check what the `__name__` attribute is set to and find out whether we are executing the function or calling it from another file, this can be used to run functions from modules

## 7. Module varieties
Python modules may reside in 
* the built-ins
* in files on disk
* pre compiled
* in zip archives
* rest api's
* databases
* we just have to make custom finders and loaders for each case 

