from random import randint
import sys
from math import sqrt


####################
# Q1
####################

# retourne le pgcd de deux entiers naturels
def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb
def euclide_ext(a,b):
    # Coefficients de Bezout pour (a, 0) et (0, b)
    u1, v1, u2, v2 = 1, 0, 0, 1
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        u1, u2 = u2, u1 - q * u2
        v1, v2 = v2, v1 - q * v2
    return u1*a+v1*b, u1, v1
    
####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(a,N):
    d, u, v = euclide_ext(a, N)
    if pgcd(a, N) != 1:
        return None  # Pas d'inverse modulaire si a et N ne sont pas premiers entre eux
    else:
        return u % N

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
def expo_modulaire(e,b,n):
    result = 1
    count_mult = 0  # Compter les multiplications
    while e != 0:
        result = result * b
        count_mult += 1
        e -= 1
    print('count_mult:', count_mult)

####################
# Q4
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
# O(log(e)) operations
def expo_modulaire_fast(e,b,n):
    result = 1
    count_mult = 0  # Compter les multiplications
    count_mod = 0  # Compter les modulos

    while e > 0:
        if e & 1:  # Si le bit le plus à droite de e est 1
            result = (result * b) % n
            count_mod += 1
        b = (b * b) % n
        count_mod += 1
        e >>= 1  # Décalage des bits de e à droite
        count_mult += 1

    #print(f"Nombre d'opérations de multiplication: {count_mult}")
    #print(f"Nombre d'opérations de modulo: {count_mod}")
    return result

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    L = [True if (i % 2 == 1  and i > 2) else False for i in range (n+1) ]
    L[1] = False
    i = 3
    result = []
    while i*i <= n+1:
        if L[i]:
            result.append(i)
            for j in range (i*i, n, 2*i):
                L[j]= False
        i += 1
    for nb in range(len(L)):
        if L[nb]:
            result.append(nb)
    return result
        
####################
# Q6
####################

# input: n  
# input: t number of tests
# test if prime according to fermat
# output: bool if prime 
def test_fermat(n,t):
    # random number generator between a and b
    #x = random.randint(a,b)
    nb_test_ok = 0
    deja_teste = []
    for test in range(t):
        a = randint(1, n-1)
        while a in deja_teste:
            a = randint(1, n-1)
        deja_teste.append(a)
    
        exp_mod_a = expo_modulaire_fast(n-1,a,n)
        if exp_mod_a == 1: 
            nb_test_ok += 1
    return nb_test_ok / t > .5

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test 
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    r = 0
    while n % 2 == 0 and n != 0:
        r += 1
        n //= 2
    u = n
    return r,u 

####################
# Q8
####################

#n entier
#a entier dans [1,n-2]
#pgcd(a,n)=1
#retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a,n):
    # utilisez expo_modulaire_fast !
    r,u = find_ru(n-1)
    expo_mod_a = expo_modulaire_fast(u, a, n)
    cond_1 = expo_mod_a != 1
    cond_2 = True
    for i in range(r):
        if expo_modulaire_fast((2**i)*u, a, n) == n-1:
            cond_2 = False
            break
    return cond_1 and cond_2


#n entier a tester, t nombre de tests
#retourne True , si n est premier
#retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n,t):
    if n %2 == 0 and n > 2:
        return False
    a = randint(1, n-1)
    while (t != 0):
        if (temoin_rabin(a, n) == True):
            return False
        t-=1
        a = randint(1, n-1)

    return True 
            
# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)
def gen_prime(n):
    inf = 2**(n-1)
    sup = 2**(n)-1
    
    p = inf
    while not test_rabin(p, 10000):
        p = randint(inf, sup)

    return p

def gen_prime_in(inf, sup):
    
    p = randint(inf, sup)
    while not test_rabin(p, 10000):
        p = randint(inf, sup)

    return p
####################
# Helper functions for rsa/elgamal
####################

# Helper function
# convert str to int
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

# Helper function
# convert int to str
def int_to_str(c):
    s = ""
    q,r = divmod(c,256)
    s = s+str(chr(r))
    while q != 0:
        q,r = divmod(q,256)
        s = s+str(chr(r))
    return s
