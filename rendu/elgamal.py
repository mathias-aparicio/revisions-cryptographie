from random import randint
import sys
from math import sqrt
import common

####################
# Q14
####################

# retourne p g 
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.
def gen_elgamal_pg(n):
    p = common.gen_prime(n)
    return [p, 3]
    
####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2) 
# pk =  g^sk [p]
# output: [sk,pk]
def gen_elgamal_sk_pk(p,g):
    sk = randint(3, p-2)
    pk = common.expo_modulaire_fast(sk, g, p)
    return [sk, pk]

####################
# Q16
####################
    
# pk_a,sk_a,pk_b,sk_b sont les cles publiques prive de A B modulo p
# retourne le secret partage par A et B
def gen_elgamal_get_secret(pk_a,sk_a,pk_b,sk_b,p):
    secret_1 = common.expo_modulaire_fast(sk_a, pk_b, p)
    secret_2 = common.expo_modulaire_fast(sk_b, pk_a, p)
    assert(secret_1 == secret_2)
    return secret_1

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de charactere c en binaire  répresentant c 
# contrainte: secret plus grand que message 
def enc_elgamal(m,secret,p):
    """
    entree : m message, secret cle prive, p premier
    sortie : c chiffre avec c = g^m * secret mod p
    """
    int_m = common.str_to_int(m)  
    return common.expo_modulaire_fast(1, int_m*secret, p) # m*secret mod p

# print("binaire enc_elgamal(abc, abcde, 9) :", enc_elgamal(26, gen_elgamal_get_secret(12), 29))

# dechiffrement du message c avec le secret
# output: chaine de charactere m 
# cotrainte: secret plus grand que message
def dec_elgamal(c,secret,p):      
    inv_secret = common.inverse_modulaire(secret, p)
    return common.expo_modulaire_fast(1, c*inv_secret, p)

####################
# Q19
####################
 
# retourne la signature [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte     
def elgamalsignature(g,p,sk,m):
    #k_pub = common.expo_modulaire_fast(sk, g, p)
    print("")
    ke = 2
    while common.pgcd(ke,p-1) != 1:
        ke = randint(2,p-2)
    m_int = common.str_to_int(m)
    r = common.expo_modulaire_fast(ke, g, p)
    inv_ke = common.inverse_modulaire(ke, p)
    s = common.expo_modulaire_fast(1, (m_int - sk *r)*inv_ke, p-1)
    return [r,s]
    
#print(elgamalsignature(2,29,12,26))

# r,s signature
# pk cle publique utilise pour vérfier la signature de message m
# m sous forme de texte 
# output: bool verifie si signature valide
# true = valid  
def elgamalverification(g,p,r,s,m,pk):
    m_int = common.str_to_int(m)
    y = common.expo_modulaire_fast(r, pk, p)
    z = common.expo_modulaire_fast(s, r, p)
    t = common.expo_modulaire_fast(1, y*z, p)
    alpha_x = common.expo_modulaire_fast(m_int, g, p)
    return t == alpha_x


#sig = elgamalsignature(d, N, m)
#print("Signature valide sur message 1:", elgamalverification(e, N, m, sig))
#print("Signature valide sur message 2:", elgamalverification(e, N, "Je suis une tartiflette", sig))