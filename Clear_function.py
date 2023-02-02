from os import system, name

# In order for this functionality to work in pycharm, "Emulate terminal in output console" has to be enabled.


def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

clear()

