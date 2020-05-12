# 1.Introduction 

The portion of the code where a name binding is defined is called the scope, the information about scopes are stored in namespaces, sort of a table that holds the scopes and bindings. 

* global scope is essentially the module scope in a single scope only
* there is no truly global other some of the built-in globally available objects 
* scope hierarchy can be as follows
* scopes have a nested hierarchy structure stuff in higher level scopes are visible to the deeper nested  scopes 
* defining names in the inner scope masks the definitions from the higher scopes 

## 2. The local scope

* the variables declared in a function are not created until the function is called
* each time the function is called a new scope is created 
* variables defined in a function are 
* we can tell python that a variable is meant to be scoped in the global scope using the global keyword 
* when python encounters  a function definition at compile-time it will scan for any labels that have values assigned to them, if not labelled as global it will be assigned to the local scope
* variables that are referenced but not assigned anywhere in the function will not be local and python will try to resolve them during runtime looking for them in enclosing scopes 
* python does not have variables that go in and out of scope within code blocks it only has scopes for functions, modules, and built-ins

## 3. Non-local scopes 

* in python we can define functions within other functions so there can be local scopes nested within other local scopes
* both functions will have access to the global and builtin scopes but the nested function will have access to the enclosing scope which is now known as a non-local scope 
* modifying global variables can be done by simply referencing it using the global keyword using the scope
* for modifying non-local variables that are in the enclosing scope, we have to explicitly tell python otherwise it will mask the higher level using `nonlocal` keyword 
* non-local works in a sort of chained way, but global is a one shot to the global scope
 
