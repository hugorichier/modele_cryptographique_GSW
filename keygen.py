from util import *
from math import ceil, log2
import numpy as np

class GSWKeys:
    def __init__(self, k, q, t, e, A, B, datatype):
        self.n = k
        self.q = q
        self.l = ceil(log2(q))
        self.m = self.n * self.l
        self.SK = t
        self.e = e
        self.A = A
        self.PK = B
        self.datatype = datatype

def keygen(k):
    #Si k ≤ 28, le programme utilise np.int64 comme datatype pour toutes les opérations de vecteurs et matrices
    #ce qui raccurci beaucoup le temps de calcul. Quand k > 28, on a de l'over-flow donc on utilise
    #l'arithmétique de python.
    if k > 29:
        datatype = 'object'
    else:
        datatype = np.int64
    # choisie un nombre premier au hasard [q]
    stat("Creation du module")
    q = generateSophieGermainPrime(k)
    l = ceil(log2(q))
    print(" "*12 + "q = %d" % q)

    # le vecteur secret [s] de dimension (n-1),
    # la clé secrete [t] de dimension n
    #
    # le vecteur erreur [e] de dimension m
    #
    # la martice [A] (n-1)×m
    #
    # la lé publique [B] est ( A )
    # ( sA+e )
    #
    stat("Creation de la clé secrete")
    n = k
    m = n*l
    #vecteur secret s
    s = np.random.randint(q, size=n-1, dtype=np.int64).astype(datatype)
    t = np.append(s, 1)
    stat("Creéation du vecteur erreur")
    e = np.rint(np.random.normal(scale=1.0, size=m)).astype(np.int).astype(datatype)
    stat("Création de la matrice A")
    A = np.random.randint(q, size=(n-1, m), dtype=np.int64).astype(datatype)
    stat("Création de la clé publique")
    B = np.vstack((-A, np.dot(s, A) + e)) % q
    check = np.dot(t, B) % q
    okay = np.all(check == (e % q))
    if okay:
        stat("keygen effectué avec succés") # t B ⋅ = e
    else:
        stat("\x1B[31;1mKeygen echec\x1B[0m") # t B ⋅ = e
    return GSWKeys(k, q, t, e, A, B, datatype)