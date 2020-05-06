def func(x : "Mandatory postional argument",
          y : "optional positional" = 1,
          z : "optional positional" = 2,
          *args : "variale postitional",
          kw1 : "Mandatory keyword argument ",
          kw2 : "Optional keyword argument" = 23,
          **kwargs : "provide extra kw here") -> "just a demo function":
    """ Lots of attributes but does nothing"""

    print("Hey yo")
