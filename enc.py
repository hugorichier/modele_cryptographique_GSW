from util import *
import numpy as np
from scipy.linalg import block_diag

def buildGadget(l, n):
    # la matrice [G] de dimension n×m
    g = 2**np.arange(l)
    return block_diag(*[g for null in range(n)])

def encrypt(keys, message):
    stat("chiffrement du message")
    # la matrice R de dimension m×m
    #
    # ciphertext (message chiffré) matrice n×m
    #
    R = np.random.randint(2, size=(keys.m, keys.m), dtype=np.int64).astype(keys.datatype)
    G = buildGadget(keys.l, keys.n)
    #C=B.R+µ×G mod(q)
    return (np.dot(keys.PK, R) + message*G) % keys.q