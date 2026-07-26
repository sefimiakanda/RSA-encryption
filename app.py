import streamlit as st
from rsa_core import generer_cles, chiffrer, dechiffrer

st.set_page_config(page_title="Démonstration RSA", page_icon="🔐", layout="wide")

st.title("🔐 Démonstration Interactive de l'Algorithme RSA")
st.markdown("Cette application permet de comprendre et de tester le chiffrement asymétrique RSA pas à pas.")

# Sidebar pour les paramètres
st.sidebar.header("Paramètres de génération")
bits = st.sidebar.slider("Taille des nombres (bits)", min_value=6, max_value=16, value=8, 
                         help="Attention : des valeurs trop grandes ralentissent le calcul sans librairie optimisée.")

if "cles_generees" not in st.session_state or st.sidebar.button("Générer de nouvelles clés"):
    with st.spinner("Génération des nombres premiers p et q..."):
        pub, priv, p, q, phi = generer_cles(bits)
        st.session_state.pub = pub
        st.session_state.priv = priv
        st.session_state.p = p
        st.session_state.q = q
        st.session_state.phi = phi
        st.session_state.cles_generees = True

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔑 1. Les Clés et Paramètres")
    st.write(f"**Nombre premier p :** `{st.session_state.p}`")
    st.write(f"**Nombre premier q :** `{st.session_state.q}`")
    st.write(f"**Module n (p × q) :** `{st.session_state.pub[1]}`")
    st.write(f"**Indicateur d'Euler φ(n) :** `{st.session_state.phi}`")
    st.success(f"**Clé Publique (e, n) :** `{st.session_state.pub}`")
    st.error(f"**Clé Privée (d, n) :** `{st.session_state.priv}`")

with col2:
    st.subheader("💬 2. Chiffrement & Déchiffrement")
    message = st.text_input("Message à chiffrer :", "Bonjour RSA")
    
    if st.button("Lancer le traitement"):
        if message:
            texte_chiffre = chiffrer(message, st.session_state.pub)
            texte_dechiffre = dechiffrer(texte_chiffre, st.session_state.priv)
            
            st.write("**Message chiffré (représentation numérique) :**")
            st.code(str(texte_chiffre))
            
            st.write("**Message déchiffré :**")
            st.success(texte_dechiffre)
        else:
            st.warning("Veuillez entrer un message.")