from keygen import keygen
from enc import encrypt
from dec import decrypt

keys = keygen(24)
for a,b in [(1,5), (10,19), (21,72)]:

    #a,b et a_b sont les messages à chiffrer
    #ca, ca et ca_cb sont les résultats de ce chiffrement
    ca = encrypt(keys, a)
    cb = encrypt(keys, b)
    a_b = a + b
    ca_cb = (ca + cb) % keys.q
    d_ca_cb = decrypt(keys, ca_cb)

    #Resultats du test
    print(" "*12 + "Message attendu %d" % a_b)
    print(" "*12 + "Message recu %d" % d_ca_cb)
    if a_b == d_ca_cb:
        print(" "*12 + "\x1B[32;1mSuccès\x1B[0m")
    else:
        print(" "*12 + "\x1B[31;1mEchec\x1B[0m")

ca = encrypt(keys, a)
cb = encrypt(keys, b)
a_b = a + a + a + b + b + b
ca_cb = (ca + ca + ca + cb + cb + cb) % keys.q
d_ca_cb = decrypt(keys, ca_cb)
print(" "*12 + "Message attendu %d" % a_b)
print(" "*12 + "Message recu %d" % d_ca_cb)
if a_b == d_ca_cb:
    print(" "*12 + "\x1B[32;1mSuccès\x1B[0m")
else:
    print(" "*12 + "\x1B[31;1mEchec\x1B[0m")