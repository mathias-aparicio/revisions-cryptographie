import random
import sys
from math import sqrt
from common import *

####################
# Q9
####################

# input: n bits
# output: e,d,N



def gen_rsa(n):
    
    # Générer deux nombres premiers p et q de n bits
    #p = gen_prime(n)
    #q = gen_prime(n)
    p = 87222764591130348284198066328471788089288705695954038754793548121312436353661
    q = 89521726413814395569841037041228051618985824982332173596851301969087772919299
    while p == q:  # p et q doivent être différents
        q = gen_prime(n)

    # Calculer N = p*q
    N = p * q

    # Calculer la fonction phi = (p-1)*(q-1)
    phi = (p - 1) * (q - 1)

    

    # Choisir un entier e tel que 1 < e < phi et pgcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    
    while pgcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Inverse modulaire de e sous phi
    d = inverse_modulaire(e, phi)

    return e, d, N


    
####################
# Q10
####################    
    
# e exponent
# N modulo
# m message
# output: c
# message/cipher sous forme de nombre
def enc_rsa(m, e, N):
    c = expo_modulaire_fast(e, m, N)
    return c


# d exponent
# N modulo
# c cipher 
# output m   
# message/cipher sous forme de nombre
def dec_rsa(c, d, N):
    m = expo_modulaire_fast(d, c, N)
    return m

####################
# Q11
####################

# e exponent
# N modulo
# m message sous forme de texte
# output: c sous forme de nombre
def RSAcipher(e,N,m):
    m_int = str_to_int(m)
    return enc_rsa(m_int, e, N)

# d exponent
# N modulo
# c cipher sous forme de nombre
# output: m message sous forme de texte
def RSAdecipher(d,N,c):
    m_int = dec_rsa(c, d, N)
    return int_to_str(m_int)


####################
# Q13
####################

# d exponent
# N modulo
# m message sous forme de texte
# output: sig
def RSAsignature(d,N,m):
    m_int = str_to_int(m)
    return enc_rsa(m_int, d, N) 

# e exponent
# N modulo
# m message sous forme de texte
# sig signature
# output: bool verifie si signature valide
# true = valid
def RSAverification(e,N,m,sig):
    m_int = str_to_int(m)
    return dec_rsa(sig, e, N) == m_int