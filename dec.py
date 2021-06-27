from util import *
from enc import buildGadget
import numpy as np

def decrypt(keys, ciphertext):
    stat("Déchiffrage du message")
    #s.C
    msg = np.dot(keys.SK, ciphertext) % keys.q
    g = buildGadget(keys.l, keys.n)
    #s.G
    sg = np.dot(keys.SK, g) % keys.q
    #raport s.C/s.G
    div = np.rint((msg / sg).astype(np.float)).astype(np.int64)
    modes = np.unique(div, return_counts=True)
    #creation du tuple avec les valeur de t et du rapport
    modes = sorted(zip(modes[0], modes[1]), key = lambda t: -t[1])
    best_num = 0
    best_dist = float('inf')

    for mu,count in modes:
        #calcule de la distance r.s.G - s.C
        dist = (mu*sg - msg) % keys.q
        dist = np.minimum(dist, keys.q - dist)
        #produit scalaire pour obtenir une valeur de distance et non pas un vecteur
        dist = np.dot(dist, dist)
        #recherche de la distance minimum
        if dist < best_dist:
            best_num = mu
            best_dist = dist
    return best_num