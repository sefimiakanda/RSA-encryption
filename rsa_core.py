import random

def est_premier(n, k=5):
    """Test de primalité de Miller-Rabin simplifié pour l'exemple."""
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def generer_nombre_premier(longueur=8):
    """Génère un nombre premier aléatoire d'une certaine longueur en bits."""
    while True:
        p = random.getrandbits(longueur)
        # S'assurer qu'il est impair et de la bonne taille
        p |= (1 << longueur - 1) | 1
        if est_premier(p):
            return p

def pgcd_etendu(a, b):
    """Algorithme d'Euclide étendu pour trouver l'inverse modulaire."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = pgcd_etendu(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def inverse_modulaire(e, phi):
    """Calcule l'inverse modulaire de e modulo phi."""
    gcd, x, y = pgcd_etendu(e, phi)
    if gcd != 1:
        raise Exception("L'inverse modulaire n'existe pas")
    return x % phi

def generer_cles(longueur_bits=8):
    """Génère une paire de clés RSA (publique, privée)."""
    p = generer_nombre_premier(longueur_bits)
    q = generer_nombre_premier(longueur_bits)
    while p == q:
        q = generer_nombre_premier(longueur_bits)
        
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choix classique de l'exposant public e
    e = 65537
    if phi <= e:
        e = 3
        while pgcd_etendu(e, phi)[0] != 1:
            e += 2
            
    d = inverse_modulaire(e, phi)
    
    return ((e, n), (d, n), p, q, phi)

def chiffrer(message_clair, cle_publique):
    e, n = cle_publique
    # Convertit chaque caractère en entier, puis applique m^e mod n
    return [pow(ord(char), e, n) for char in message_clair]

def dechiffrer(message_chiffre, cle_privee):
    d, n = cle_privee
    # Applique c^d mod n, puis reconvertit en caractère
    return "".join([chr(pow(char, d, n)) for char in message_chiffre])