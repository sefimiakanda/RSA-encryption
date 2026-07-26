# 🔐 Projet RSA - Implémentation Pédagogique en Python & Web App

Ce projet propose une implémentation complète, transparente et *from scratch* (sans bibliothèques cryptographiques externes) de l'algorithme de chiffrement asymétrique **RSA** (Rivest-Shamir-Adleman) en Python. Il est accompagné d'une interface web interactive développée avec Streamlit pour visualiser la génération des clés, le chiffrement et le déchiffrement en direct.

---

## 🚀 Fonctionnalités du Projet

- **Génération complète des clés RSA** :
  - Génération de nombres premiers aléatoires $p$ et $q$.
  - Test de primalité (Miller-Rabin simplifié).
  - Calcul du module $n$ et de l'indicateur d'Euler $\phi(n)$.
  - Détermination de l'exposant public $e$ et calcul de l'exposant privé $d$ via l'**algorithme d'Euclide étendu**.
- **Chiffrement & Déchiffrement** : Conversion des caractères en entiers et application de l'arithmétique modulaire.
- **Interface Web Interactive (Streamlit)** : Permet de tester le système en temps réel avec des paramètres ajustables.

---

## 📂 Structure du Projet

```text
├── rsa_core.py      # Cœur mathématique et algorithmique de RSA
├── app.py           # Interface web interactive (Streamlit)
└── requirements.txt # Dépendances du projet
```

## 📦 Installation et Utilisation
1. Prérequis
Assurez-vous d'avoir installé Python (version 3.8 ou supérieure) sur votre machine.

2. Cloner le dépôt et installer les dépendances
Ouvrez votre terminal et exécutez les commandes suivantes :

```
# Cloner le projet (remplacez l'URL par la vôtre)
git clone [https://github.com/votre-nom/projet-rsa.git](https://github.com/votre-nom/projet-rsa.git)
cd projet-rsa

# Installer les dépendances requises
pip install -r requirements.txt
```
3. Lancer l'application web
```
streamlit run app.py
```
## 🧮 Explications Mathématiques et Théoriques de RSA

Le chiffrement RSA repose sur la difficulté mathématique de la factorisation de grands nombres entiers (le produit de deux grands nombres premiers).

1. Génération des Clés
### Choisir deux grands nombres premiers distincts : $p$ et $q$.
### Calculer le module $n$ :$$n = p \times q$$
(Ce module $n$ fait partie de la clé publique et de la clé privée. Sa taille en bits définit la robustesse du chiffrement).
### Calculer l'indicateur d'Euler $\phi(n)$ :$$\phi(n) = (p - 1)(q - 1)$$

### Choisir l'exposant public $e$ :
On choisit un entier $e$ tel que $1 < e < \phi(n)$ et qui soit premier avec $\phi(n)$ (c'est-à-dire $\text{PGCD}(e, \phi(n)) = 1$). Généralement, on utilise la valeur standard 65537.
### Calculer l'exposant privé $d$ :
On calcule l'inverse modulaire de $e$ modulo $\phi(n)$ à l'aide de l'algorithme d'Euclide étendu :$$e \times d \equiv 1 \pmod{\phi(n)}$$
## Clé Publique : $(e, n)$ — Diffusée à tout le monde pour chiffrer les messages.
## Clé Privée : $(d, n)$ — Gardée secrète pour déchiffrer les messages.
2. Le Chiffrement
Pour chiffrer un message clair $m$ (converti préalablement en un entier numérique tel que $0 \le m < n$), l'émetteur utilise la clé publique $(e, n)$ :
$$c = m^e \pmod n$$
Le résultat $c$ est le texte chiffré.
3. Le Déchiffrement
Pour retrouver le message original $m$ à partir du texte chiffré $c$, le destinataire utilise sa clé privée $(d, n)$ :
$$m = c^d \pmod n$$

## ⚠️ Avertissement Éducatif
Ce projet est à but purement éducatif. L'implémentation de RSA proposée ici (en Python pur sans surcouche optimisée, avec de petits nombres premiers générés à des fins de démonstration) ne doit en aucun cas être utilisée dans un contexte de production ou pour sécuriser des données sensibles réelles.
