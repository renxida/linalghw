modulus = 11
rooted = 5

def a(x):
    return x[0]
def b(x):
    return x[1]

def mul(x, y):
    a_ret = a(x) * a(y) + rooted * b(x) * b(y)
    b_ret = a(x) * b(y) + b(x) * a(y)
    return (a_ret % modulus, b_ret % modulus)

def add(x, y):
    return tuple((xx + yy) % modulus for xx, yy in zip(x, y))

def neg(x):
    return tuple(-xx % modulus for xx in x)

from itertools import product
from itertools import combinations_with_replacement as cwr

ALL_ELEMENTS = lambda m: list(product(range(m), repeat = 2))
ZERO = (0,0)
ONE  = (1,0)

def test_rule_combi(rule, r):
    # identity(x_1...x_r) returns true if the x satisfy the identity.
    # this function returns true if all identities are satisfied.
    for elements in cwr(ALL_ELEMENTS, r=r):
        if not rule(*elements):
            return False
    return True




def rule_C1(a, c):
    if a == c:
        return True
    for b in ALL_ELEMENTS:
        if add(a, b) == add(c, b) and a != b:
            print('cancellation (+) failed: {a} + {b} = {c} + {b} but {a} != {c}'.format(
                        a=a, b=b, c=c
                    )
                 )
            return False
        if b != (0,0) and mul(a, b) == mul(c, b) and a != b:
            print('cancellation (*) failed: {a} * {b} = {c} * {b} but {a} != {c}'.format(
                        a=a, b=b, c=c
                    )
                 )
            return False
    return True

def rule_C2(a, b):
    return mul(a, ZERO) == ZERO and \
           mul(neg(a), b) == mul(a, neg(b)) and \
           mul(neg(a), b) == neg(mul(a, b)) and \
           mul(a, b) == mul(neg(a) , neg(b))



def test_rule_permu(rule, r):
    for elements in product(ALL_ELEMENTS(modulus), repeat=r):
        if not rule(*elements):
            return False
    return True

def rule_distrib(a, b, c):
    return mul(a, add(b, c)) == add(mul(a, b), mul(a, c))


def find_zero_divisor():
    m = modulus
    for a, b in cwr(product(range(1, m), repeat = 2) ,2):
        if mul(a, b) == ZERO:
            print('found: {a} * {b} == 0'.format(a=a, b=b))
    print('done')
