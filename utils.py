from time import time
from random import randint
start = None

def stat(msg):
    #fonction de stat pour avoir une idée du temps pris par les étapes du programme
    global start
    now = time()
    if start is None:
        start = now
    print("\x1B[2m%10.4f %s\x1B[0m" % (now-start, msg))


def is_prime(p):
    #verification du nombre premier
    if p == 2:
        return True
    if p < 2 or p % 2 == 0:
        return False
    for n in range(3, int(p ** 0.5) + 2, 2):
        if p % n == 0:
            return False
    return True

def gen_prime(b):
    #retourne un nombre premier
    p = randint(2**(b-1), 2**b)
    while not is_prime(p):
        p = randint(2**(b-1), 2**b)
    return p

def generateSophieGermainPrime(k):
    #retourne un nombre premier de Sophie Germain avec k bits
    p = gen_prime(k-1)
    sp = 2*p + 1
    while not is_prime(sp):
        p = gen_prime(k-1)
        sp = 2*p + 1
    return p

def generateSafePrime(k):
    #retourne un nombre premier sûr avec k bits
    p = gen_prime(k-1)
    sp = 2*p + 1
    while not is_prime(sp):
        p = gen_prime(k-1)
        sp = 2*p + 1
    return sp
