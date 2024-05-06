import random
import sys
from math import sqrt
from common import *
from rsa import *

####################
# Q20
####################
def smallN_attack(e, N, c):
    # Trouver les facteurs premiers de N
    for p in range(2, int(sqrt(N)) + 1):
        if N % p == 0:
            q = N // p
            break
    else:
        return "N n'est pas un nombre composé de deux facteurs premiers"


    # Calculer la fonction d'Euler phi(N)
    phi = (p - 1) * (q - 1)

    # Trouver la clé privée d
    d = inverse_modulaire(e, phi)

    # Déchiffrer le message avec la clé privée d
    m = RSAdecipher(d,N,c)

    return m


####################
# Q21
####################
def commonFactor_attack(e1, N1, c1, e2, N2):
    # Trouver le PGCD de N1 et N2, qui est le facteur commun p
    p = pgcd(N1, N2)
    if p == 1:
        raise ValueError("N1 et N2 n'ont pas de facteur commun")

    q = N1 // p
    phi = (p - 1) * (q - 1)
    d1 = inverse_modulaire(e1, phi)
    m = RSAdecipher(d1, N1, c1)

    return m  


####################
# Q22
####################
def resteChinois(e_123, n_1, c_1, n_2, c_2, n_3, c_3):
    N = n_1 * n_2 * n_3

    N1 = N // n_1
    N2 = N // n_2
    N3 = N // n_3

    u1 = inverse_modulaire(N1, n_1)
    u2 = inverse_modulaire(N2, n_2)
    u3 = inverse_modulaire(N3, n_3)

    c = (c_1 * N1 * u1 + c_2 * N2 * u2 + c_3 * N3 * u3) % N

    m = c**(1/e_123) # On suppose que e_123 est petit
    return int_to_str(int(m))


    
####################
# Q23
####################
# todo
