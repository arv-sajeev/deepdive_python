print("{0} is up and running".format(__name__))


def print_dict(header,d):
    print("\n\n--------------------------------------------------\n")
    print("###########____{0}_____#################".format(header))

    for key,value in d.items():
        print(key,value)
    print("\n\n--------------------------------------------------\n")



print_dict("module1.args",globals())
