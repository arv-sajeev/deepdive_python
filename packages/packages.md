# Packages

Packages are modules that can contain other modules or packages, its a way of grouping similar modules together.

* if a module is a package, it must have a value set for `__path__` 
* they are typically file system entities, but they don;t have to exclusively be
* when a module within a package is imported the package is imported as well

## File based packages

* packages paths are created using the file system directories and files
* a package typically consists of a directory with its nested modules or packages
* an `__init__.py` to implement the code for the package
* the path will be absolute path of the directory

## Why packages??
* for code organization and ease of use
* for splitting code across modules and storing these related modules as a single unit
* easier to write, test, debug
* use relative imports in the `__init__.py` for better compatibility when changing names of parent package
* use `__all__` to select which names to add to the namespace when imported

## Namespace packages
* they may contain modules 
* may contain nested regular packages 
* but do not contain `__init__.py`
* These directories are implicitly made into special types of packages
* you can add modules and packages from zip files by adding the paths of the zips using `sys.path.append`
