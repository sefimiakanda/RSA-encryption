# 🔐 RSA - Implémentation Pédagogique en Python & Web App

Une implémentation complète et pédagogique de l'algorithme de chiffrement asymétrique **RSA (Rivest-Shamir-Adleman)** développée entièrement **from scratch**, sans utiliser de bibliothèque cryptographique externe.

Le projet est accompagné d'une interface web réalisée avec **Streamlit**, permettant de visualiser en temps réel la génération des clés, le chiffrement et le déchiffrement.

---

## 🚀 Fonctionnalités

- 🔑 Génération complète des clés RSA
  - Génération aléatoire de deux nombres premiers `p` et `q`
  - Test de primalité (Miller-Rabin simplifié)
  - Calcul de `n` et de `φ(n)`
  - Génération des clés publique et privée grâce à l'algorithme d'Euclide étendu

- 🔒 Chiffrement RSA
  - Conversion du message en valeurs numériques
  - Chiffrement par exponentiation modulaire

- 🔓 Déchiffrement RSA
  - Récupération du message original avec la clé privée

- 🌐 Interface Web Interactive
  - Développée avec **Streamlit**
  - Génération des clés en un clic
  - Chiffrement et déchiffrement en direct
  - Affichage des calculs principaux

---

# 📂 Structure du projet

```text
.
├── rsa_core.py       # Implémentation mathématique de RSA
├── app.py            # Interface Web Streamlit
└── requirements.txt  # Dépendances
```

---

# 📦 Installation

## 1. Cloner le dépôt

```bash
git clone https://github.com/votre-nom/projet-rsa.git
cd projet-rsa
```

## 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 3. Lancer l'application

```bash
streamlit run app.py
```

---

# 🧮 Comprendre RSA

RSA repose sur la difficulté de **factoriser le produit de deux très grands nombres premiers**.

Le système fonctionne en trois grandes étapes :

- Génération des clés
- Chiffrement
- Déchiffrement

---

# 🔑 1. Génération des clés

## Étape 1 : Choisir deux nombres premiers

```
p
q
```

avec :

- `p ≠ q`
- `p` et `q` sont premiers.

---

## Étape 2 : Calcul du module

```
n = p × q
```

Le nombre `n` appartient à la fois :

- à la clé publique ;
- à la clé privée.

La taille de `n` détermine le niveau de sécurité de RSA.

---

## Étape 3 : Calcul de l'indicateur d'Euler

```
φ(n) = (p − 1)(q − 1)
```

---

## Étape 4 : Choisir l'exposant public

Choisir un entier `e` tel que :

```
1 < e < φ(n)
```

et

```
PGCD(e, φ(n)) = 1
```

En pratique, la valeur la plus utilisée est :

```
e = 65537
```

---

## Étape 5 : Calcul de l'exposant privé

Calculer l'inverse modulaire de `e` modulo `φ(n)` :

```
e × d ≡ 1 (mod φ(n))
```

Cette opération est réalisée grâce à l'algorithme d'Euclide étendu.

---

## Clé publique

```
(e, n)
```

Elle peut être distribuée librement.

Elle sert à **chiffrer** les messages.

---

## Clé privée

```
(d, n)
```

Elle doit rester secrète.

Elle sert à **déchiffrer** les messages.

---

# 🔒 2. Chiffrement

Le message est d'abord converti en entier :

```
0 ≤ m < n
```

Puis le chiffrement est effectué avec la clé publique :

```
c = m^e mod n
```

où :

- `m` : message
- `e` : exposant public
- `n` : module
- `c` : message chiffré

---

# 🔓 3. Déchiffrement

Le destinataire applique la clé privée :

```
m = c^d mod n
```

où :

- `c` : message chiffré
- `d` : exposant privé
- `n` : module

Le message d'origine est alors retrouvé.

---

# 📚 Algorithmes implémentés

Le projet implémente notamment :

- Génération aléatoire de nombres premiers
- Test de primalité de Miller-Rabin
- PGCD (algorithme d'Euclide)
- Algorithme d'Euclide étendu
- Inverse modulaire
- Exponentiation modulaire rapide
- Génération des clés RSA
- Chiffrement RSA
- Déchiffrement RSA

---

# 🖥️ Interface Web

L'application Streamlit permet de :

- générer automatiquement des clés RSA ;
- afficher toutes les valeurs calculées (`p`, `q`, `n`, `φ(n)`, `e`, `d`) ;
- saisir un message ;
- chiffrer le message ;
- le déchiffrer instantanément.

---

# ⚠️ Avertissement

> **Ce projet est destiné uniquement à un usage pédagogique.**

Cette implémentation utilise de petits nombres premiers et une version simplifiée de certains algorithmes afin de faciliter leur compréhension.

Elle **ne doit pas être utilisée pour protéger des données réelles ou dans un environnement de production**.

---

# 👨‍💻 Technologies utilisées

- Python
- Streamlit
- Arithmétique modulaire
- Algorithme d'Euclide étendu
- Test de primalité Miller-Rabin
- RSA

---

# 📄 Licence

Ce projet est distribué à des fins d'apprentissage et d'expérimentation.
