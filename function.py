def LINEARTWO1DUP(x, he):
    return 'LINEARTWO1DUP', x / he

def LINEARTWO1DDOWN(x, he):
    return 'LINEARTWO1DDOWN', 1 - x / he

def LINEARTWO1DUPDOT(x, he):
    return 1 / he

def LINEARTWO1DDOWNDOT(x, he):
    return - 1 / he
