import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configuration de la page
st.set_page_config(
    page_title="Maintenance Prédictive",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>

    /* ----- TITRES DES EXPANDERS EN BLANC ----- */
    .stExpander summary {
        color: white !important;      /* titre expander fermé */
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 15px 20px !important;
    }

    .stExpander[open] summary {
        color: white !important;      /* titre expander ouvert */
        border-bottom: 2px solid #D1D8E0;
        margin-bottom: 15px;
    }

    /* ----- COULEUR DU MOT NAVIGATION ----- */
    section[data-testid="stSidebar"] h1 {
        color: white !important;
    }

    /* Fond des expanders */
    .stExpander {
        background-color: #363333 !important;
        border-radius: 15px;
        border: 2px solid #D1D8E0 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 15px 0;
        transition: transform 0.3s ease;
    }

    .stExpander:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        border-color: #1E90FF !important;
    }
/* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
        padding: 25px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.3);
    }
</style>
""", unsafe_allow_html=True)





# Sidebar avec style amélioré
st.sidebar.markdown("# 🔧 Navigation")
st.sidebar.markdown("---")
section = st.sidebar.radio(
    "",
    ["🏠 Accueil", "📚 Théorie", "📖 Ressources", "✏️ Exercices", "ℹ️ À propos"],
    label_visibility="collapsed"
)

# Fonction helper pour créer des cards
def create_info_card(icon, title, content):
    st.markdown(f"""
    <div class="info-box">
        <h2>{icon} {title}</h2>
        <p style="font-size: 1.1rem; line-height: 1.6;">{content}</p>
    </div>
    """, unsafe_allow_html=True)

# ACCUEIL
if section == "🏠 Accueil":
    st.title("🔧Maintenance Prédictive")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Concepts", "5+", "Théoriques")
    with col2:
        st.metric("✏️ Exercices", "5", "Pratiques")
    with col3:
        st.metric("🔗 Ressources", "10+", "Liens utiles")
    
    st.markdown("---")
    
    create_info_card(
        "🎯",
        "Objectif",
        "Maîtriser la maintenance prédictive de A à Z grâce à une approche interactive et pratique."
    )
    
    st.subheader("🌟 Découvrez les sections")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("### 📚 Théorie")
            st.write("Explorez les concepts fondamentaux, les capteurs, les méthodes d'analyse et les KPI essentiels.")
            
        with st.container():
            st.markdown("### ✏️ Exercices")
            st.write("Mettez en pratique vos connaissances avec des exercices interactifs et des cas réels.")
    
    with col2:
        with st.container():
            st.markdown("### 📖 Ressources")
            st.write("Accédez à une sélection de cours, vidéos et articles pour approfondir vos connaissances.")
            
        with st.container():
            st.markdown("### ℹ️ À propos")
            st.write("Découvrez les objectifs du projet et les fonctionnalités principales.")

# THÉORIE — Parcours complet débutant → expert (2 niveaux par expander)
elif section == "📚 Théorie":
    st.title("📚 Théorie & Parcours : Débutant → Expert")
    st.markdown("### Formation complète pour apprendre la maintenance prédictive de 0% à expert.")

    # -------------------- NIVEAU 0 --------------------
   with st.expander("🟦 Niveau 0 — Comprendre simplement (Introduction)", expanded=True):
        st.markdown("## 🟦 Niveau 0 — C’est quoi la maintenance prédictive ?")
    
        st.markdown("""
        La maintenance prédictive est une **méthode moderne** qui permet de dire :
    
        > **“Cette machine risque de tomber en panne bientôt. Interviens maintenant pour éviter le problème.”**
    
        Elle transforme la maintenance classique en un système **intelligent**, basé sur l’anticipation plutôt que sur la réaction.
    
        ---
    
        ## 🔍 Pourquoi existe-t-elle ?
        Dans les usines, une panne peut :
        - arrêter toute la production,
        - coûter des milliers d'euros,
        - mettre les travailleurs en danger,
        - abîmer d’autres équipements.
    
        Les entreprises veulent donc **savoir à l’avance** si une machine va mal.
    
        C'est exactement ce que fait la maintenance prédictive.
    
        ---
    
        ## ⚙️ Comment ça fonctionne ?  
        La maintenance prédictive se base sur **3 éléments essentiels :**
    
        ### 1️⃣ Les capteurs  
        Ce sont des petits appareils placés sur les machines.
        Ils mesurent en continu :
        - vibrations,
        - température,
        - courant,
        - bruit,
        - pression…
    
        ➜ Ils servent de **sens** pour la machine : comme les yeux, les oreilles, la peau.
    
        ### 2️⃣ Les données  
        Toutes ces mesures sont envoyées vers un ordinateur.
    
        ➜ Cela crée un historique :  
        *“Normalement la machine vibre comme ça… mais aujourd’hui elle vibre un peu plus.”*
    
        ### 3️⃣ Les algorithmes (IA / Machine Learning)  
        Les algorithmes apprennent à reconnaître :
        - ce qui est **normal**,
        - ce qui est **anormal**,
        - et ce qui annonce une **future défaillance**.
    
        ➜ Ils envoient alors une alerte :  
        **“Attention, un roulement semble usé. Prévoir un remplacement dans 3 jours.”**
    
        ---
    
        ## 🎯 Les objectifs principaux
        La maintenance prédictive permet de :
        - ✔️ éviter les pannes
        - ✔️ réduire les coûts de maintenance
        - ✔️ améliorer la sécurité
        - ✔️ augmenter la durée de vie des machines
        - ✔️ optimiser le planning des techniciens
        - ✔️ éviter les arrêts soudains de production
    
        ---
    
        ## 🚗 Exemple simple pour bien comprendre
        **Ta voiture fait un bruit bizarre ➜ tu vas chez le mécanicien.**
    
        ➤ Tu as détecté un signe **avant** que la panne arrive.
    
        Dans une usine :
        - une machine fait un bruit anormal
        - un capteur sonore le détecte
        - un algorithme compare ce bruit aux anciens bruits
        - il voit que ce bruit annonce une défaillance
        - il prévient le technicien
    
        ➜ **C’est la même logique, mais 100% automatique et en continu.**
    
        ---
    
        ## 🧠 En résumé pour un débutant :
        - Une machine envoie des signaux  
        - Les capteurs les captent  
        - L’IA analyse ces signaux  
        - Elle prédit si une panne va arriver  
    
        👉 Résultat : on répare **avant** qu'il ne soit trop tard.
        """)
    
        st.info("🌟 À retenir : La maintenance prédictive = anticiper les pannes grâce aux capteurs, aux données et à l’IA.")

    # -------------------- NIVEAU 1 --------------------
    with st.expander("🟩 Niveau 1 — Les 3 types de maintenance"):
        st.markdown("## 🟩 Niveau 1 — Corrective, Préventive, Prédictive")
        st.markdown("""
        ### 🔴 1) Maintenance Corrective  
        → On répare **après** la panne  
        ❌ Très coûteux  
        ❌ Arrêt de production  

        ### 🟡 2) Maintenance Préventive  
        → Entretien basé sur un **calendrier fixe**  
        ⚠️ Peut être inutile (machine encore en bon état)

        ### 🟢 3) Maintenance Prédictive  
        → Basée sur les **données et capteurs**  
        ✔️ Optimise les interventions  
        ✔️ Évite arrêts non planifiés  
        ✔️ Économique et moderne
        """)

    # -------------------- NIVEAU 2 --------------------
    with st.expander("🟨 Niveau 2 — Capteurs & Données"):
        st.markdown("## 🟨 Niveau 2 — Capteurs utilisés en maintenance prédictive")
        st.markdown("""
        Les capteurs sont les **yeux et les oreilles** des machines.

        ### Capteurs courants :
        - 🌊 **Vibrations** → roulements, déséquilibre
        - 🌡️ **Température** → surchauffe
        - ⚡ **Courant** → surcharge moteur
        - 🔊 **Acoustique / Ultrasons** → fissures, fuites
        - 🧰 **Pression** → hydraulique / pneumatique
        - 💧 **Humidité** → moteurs, transformateurs

        ### Notions essentielles :
        - Fréquence d’échantillonnage  
        - Bruit du signal  
        - Intervalle de mesure  
        - Qualité des données  
        """)
        st.info("🎯 Une bonne prédiction = données propres + capteurs bien choisis.")

    # -------------------- NIVEAU 3 --------------------
    with st.expander("🟧 Niveau 3 — Analyse de données (Data Analysis)"):
        st.markdown("## 🟧 Niveau 3 — Analyse des données")
        st.markdown("""
        Pour exploiter les mesures, il faut analyser les signaux :

        ### Méthodes :
        - 📊 Statistiques : moyenne, variance, tendance  
        - 🔺 Détection de pics : anomalies brutales  
        - 📈 Courbes temporelles : évolution dans le temps  
        - 🎧 Analyse vibratoire : signatures de roulements  
        - 📉 FFT (spectre) : fréquences de défaillances

        ### Objectif :
        Transformer les signaux → en informations → en décisions.
        """)
        st.info("🧠 La data analysis est la base avant de faire du Machine Learning.")

    # -------------------- NIVEAU 4 --------------------
    with st.expander("🟥 Niveau 4 — Machine Learning & IA"):
        st.markdown("## 🟥 Niveau 4 — Machine Learning pour la maintenance")
        st.markdown("""
        Les algorithmes apprennent à reconnaître les pannes.

        ### Méthodes ML :
        1️⃣ **Régression** → prédire une valeur future  
        2️⃣ **Classification** → normal vs anormal  
        3️⃣ **Clustering** → grouper comportements inconnus  
        4️⃣ **Détection d’anomalies** → repérer pannes rares  

        ### Workflow ML :
        - collecte  
        - nettoyage  
        - features  
        - entraînement  
        - test  
        - déploiement  
        """)

    # -------------------- NIVEAU 5 --------------------
    with st.expander("🟪 Niveau 5 — Modèles avancés (Deep Learning)"):
        st.markdown("## 🟪 Niveau 5 — Deep Learning")
        st.markdown("""
        Pour signaux complexes :

        - **CNN** → images, spectrogrammes vibratoires  
        - **LSTM / GRU** → séries temporelles longues  
        - **Auto-encoders** → détection d’anomalies sans labels  

        Avantage : très puissant  
        Inconvénient : demande beaucoup de données
        """)
        st.info("🌟 À utiliser pour vibrations complexes ou très grandes installations.")

    # -------------------- NIVEAU 6 --------------------
    with st.expander("🟫 Niveau 6 — Architecture IoT"):
        st.markdown("## 🟫 Niveau 6 — Architecture IoT complète")
        st.markdown("""
        Un système complet comprend :

        ### 1) 📡 Capteurs  
        → acquisition des signaux

        ### 2) 🧠 Edge computing (Raspberry Pi / MCU)  
        → filtrage, prétraitement, mini-modèles

        ### 3) ☁️ Cloud (AWS, Azure, GCP)  
        → stockage, analyse, entraînement IA

        ### 4) 📊 Dashboard  
        → interface utilisateur : Power BI, Grafana, Streamlit
        """)
        st.info("💡 Prétraiter en edge permet de réduire le trafic réseau & latence.")

    # -------------------- NIVEAU 7 --------------------
    with st.expander("🟦 Niveau 7 — Workflow réel en usine"):
        st.markdown("## 🟦 Niveau 7 — Workflow d’un projet réel en usine")
        st.markdown("""
        1️⃣ Collecte des données  
        2️⃣ Nettoyage (outliers, valeurs manquantes)  
        3️⃣ Feature engineering (RMS, kurtosis…)  
        4️⃣ Entraînement ML/IA  
        5️⃣ Détection d’anomalies  
        6️⃣ Envoi d’alertes  
        7️⃣ Planification de maintenance  
        8️⃣ Suivi des KPI  
        """)
        st.success("🎯 C’est le cycle complet d’un système industriel moderne.")

    # -------------------- NIVEAU 8 --------------------
    with st.expander("🟫 Niveau 8 — KPI essentiels"):
        st.markdown("## 🟫 Niveau 8 — Les indicateurs clés")
        st.markdown("""
        - ⏱️ **MTBF** : temps moyen entre pannes  
        - 🔧 **MTTR** : temps moyen de réparation  
        - ⚙️ **Disponibilité** : MTBF / (MTBF + MTTR)  
        - 📉 **Taux d’anomalies**  
        - 💸 **Coût d’arrêt de production**

        Ces KPI mesurent l’impact réel de la maintenance prédictive.
        """)
        st.info("🎯 Suivre les KPI = prouver l’efficacité du système.")

    # -------------------- NIVEAU 9 --------------------
    with st.expander("🟩 Niveau 9 — Cas pratiques"):
        st.markdown("## 🟩 Niveau 9 — Cas pratiques inspirés du réel")
        st.markdown("""
        - 🔧 Défaillance moteur → vibrations + courant  
        - 🎧 Analyse acoustique → compresseurs  
        - 🔥 Suivi de température → fours industriels  
        - ⚙️ Roulements → analyse FFT + signatures  
        - 🏭 Lignes d'assemblage → prédiction multi-capteurs  

        Chaque cas = un mini-projet complet.
        """)
        st.success("Si tu veux, je peux transformer chaque cas en mini-project avec datasets + code Python.")



# RESSOURCES
elif section == "📖 Ressources":
    st.title("📖 Ressources & Liens Utiles")
    
    tab1, tab2, tab3 = st.tabs(["🎓 Cours en ligne", "🎬 Vidéos", "📄 Articles"])
    
    with tab1:
        st.markdown("### Formations complètes")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### 🎓 Coursera
            Formation complète sur la maintenance prédictive avec certificat.
            
            [Accéder au cours →](https://www.coursera.org/learn/predictive-maintenance)
            """)
        
        with col2:
            st.markdown("""
            #### 🎓 Udemy
            Multiples cours sur la maintenance prédictive, du débutant à l'expert.
            
            [Voir les cours →](https://www.udemy.com/topic/predictive-maintenance/)
            """)
    
    with tab2:
        st.markdown("### Tutoriels vidéo")
        st.markdown("""
        - 🎬 [Introduction à la Maintenance Prédictive](https://www.youtube.com/watch?v=example1)
        - 🎬 [Maintenance Prédictive et IoT](https://www.youtube.com/watch?v=example2)
        - 🎬 [Analyse des vibrations en pratique](https://www.youtube.com/watch?v=example3)
        """)
    
    with tab3:
        st.markdown("### Documentation et recherche")
        st.markdown("""
        - 📄 [Maintenance.org - Articles spécialisés](https://www.maintenance.org/)
        - 📄 [IEEE - Publications scientifiques](https://ieeexplore.ieee.org/Xplore/home.jsp)
        - 📄 [Guides pratiques et cas d'études](https://www.maintenance.org/guides)
        """)


# EXERCICES
elif section == "✏️ Exercices":
    st.title("✏️ Exercices et Cas Pratiques")
    st.markdown("### Testez vos connaissances avec des exercices interactifs")
    
    # Exercice 1
    with st.expander("📊 **Exercice 1 : Détection d'anomalies** - Identifiez les pics de vibration", expanded=True):
        st.markdown("#### Identifiez les jours où la vibration dépasse la valeur normale (> 6)")
        
        np.random.seed(42)
        jours = pd.date_range(start="2025-12-01", periods=30)
        vibration = np.random.normal(5, 1, 30)
        vibration[10] = 8
        vibration[25] = 7
        df = pd.DataFrame({"Jour": jours, "Vibration": vibration})
        
        # Graphique amélioré
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df["Jour"], 
            y=df["Vibration"],
            mode='lines+markers',
            name='Vibration',
            line=dict(color='#2E86DE', width=2),
            marker=dict(size=8)
        ))
        fig.add_hline(y=6, line_dash="dash", line_color="red", 
                     annotation_text="Seuil normal")
        fig.update_layout(
            title="Mesure de vibration sur 30 jours",
            xaxis_title="Jour",
            yaxis_title="Vibration (mm/s)",
            hovermode='x unified',
            plot_bgcolor='white'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        jours_anomalie = st.multiselect(
            "Sélectionnez les jours avec anomalie :", 
            options=df['Jour'].dt.strftime('%Y-%m-%d').tolist()
        )
        
        reponse_correcte = ["2025-12-11", "2025-12-26"]
        
        if jours_anomalie:
            if set(jours_anomalie) == set(reponse_correcte):
                st.success("✅ Excellent ! Vous avez identifié toutes les anomalies.")
                st.info("💡 Les jours 11 et 26 dépassent la vibration normale, indiquant des anomalies potentielles.")
            else:
                st.error(f"❌ Pas tout à fait. Les jours corrects sont : {', '.join(reponse_correcte)}")

    # Exercice 2
    with st.expander("🔢 **Exercice 2 : Calcul de KPI** - MTBF et MTTR"):
        st.markdown("""
        #### Calculez les indicateurs clés
        **Données :**
        - Nombre de pannes : 4
        - Temps total de fonctionnement : 400 h
        - Temps total de réparation : 20 h
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            mtbf_input = st.number_input("MTBF (heures) :", min_value=0.0, step=1.0)
        with col2:
            mttr_input = st.number_input("MTTR (heures) :", min_value=0.0, step=0.1)
        
        if st.button("🎯 Vérifier la réponse", key="ex2"):
            mtbf_correct = 400/4
            mttr_correct = 20/4
            if mtbf_input == mtbf_correct and mttr_input == mttr_correct:
                st.success("✅ Parfait ! Vos calculs sont corrects.")
                st.info(f"💡 **Formules :** MTBF = 400/4 = {mtbf_correct} h | MTTR = 20/4 = {mttr_correct} h")
            else:
                st.error(f"❌ Réessayez. **Indices :** MTBF = Temps total / Nombre de pannes | MTTR = Temps réparation / Nombre de pannes")

    # Exercice 3
    with st.expander("❓ **Exercice 3 : Quiz Théorique** - Testez vos connaissances"):
        st.markdown("#### Quel type de maintenance prévient les pannes grâce aux données de capteurs ?")
        
        reponse = st.radio(
            "Choisissez votre réponse :",
            ("Corrective", "Préventive", "Prédictive"),
            key="quiz1"
        )
        
        if st.button("🎯 Vérifier la réponse", key="ex3"):
            if reponse == "Prédictive":
                st.success("✅ Exact ! La maintenance prédictive est la bonne réponse.")
                st.info("💡 La maintenance prédictive utilise les données des capteurs pour détecter les anomalies avant la panne.")
            else:
                st.error("❌ Ce n'est pas la bonne réponse. Pensez au type de maintenance qui utilise l'analyse de données.")

    # Exercice 4
    with st.expander("🔮 **Exercice 4 : Prédiction de panne** - Analysez les mesures"):
        st.markdown("""
        #### Analysez les mesures et prédisez une panne
        
        **Mesures actuelles :**
        - Vibration : 7 mm/s
        - Température : 80°C
        - Courant : 5A
        
        **Seuils critiques :**
        - Vibration > 6 mm/s ⚠️
        - Température > 75°C ⚠️
        - Courant > 6A ⚠️
        """)
        
        prediction = st.radio(
            "La machine va-t-elle tomber en panne ?",
            ("Oui", "Non"),
            key="pred1"
        )
        
        if st.button("🎯 Vérifier la réponse", key="ex4"):
            if prediction == "Oui":
                st.success("✅ Correct ! La machine présente des signes de défaillance imminente.")
                st.info("💡 **Analyse :** Vibration = 7 > 6 ET Température = 80 > 75 → Panne probable")
            else:
                st.error("❌ Attention ! Relisez les valeurs et les seuils critiques.")

    # Exercice 5
    with st.expander("🏭 **Exercice 5 : Cas pratique complet** - Analyse de production"):
        st.markdown("""
        #### Analysez une ligne de production
        
        **Contexte :**
        - 3 arrêts en 100 heures
        - Temps d'arrêt total : 9 heures
        
        **Calculez :**
        1. Disponibilité (%)
        2. Fiabilité approximative (%)
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            dispo_input = st.number_input("Disponibilité (%) :", min_value=0.0, max_value=100.0, step=0.1)
        with col2:
            fiab_input = st.number_input("Fiabilité (%) :", min_value=0.0, max_value=100.0, step=0.1)
        
        if st.button("🎯 Vérifier la réponse", key="ex5"):
            dispo_correct = (100-9)/100*100
            fiab_correct = (100-9)/100*50
            
            if abs(dispo_input - dispo_correct) < 0.5 and abs(fiab_input - fiab_correct) < 0.5:
                st.success("✅ Excellent travail ! Vos calculs sont précis.")
                st.info(f"💡 **Formules :** Disponibilité = (100-9)/100×100 = {round(dispo_correct,1)}% | Fiabilité ≈ {round(fiab_correct,1)}%")
            else:
                st.error(f"❌ Pas tout à fait. **Aide :** Disponibilité = Temps de fonctionnement / Temps total")

# À PROPOS
elif section == "ℹ️ À propos":
    st.title("ℹ️ À propos du Portfolio")
    
    create_info_card(
        "🎯",
        "Mission",
        "Créer une ressource complète et interactive pour l'apprentissage de la maintenance prédictive, accessible à tous."
    )
    
    st.markdown("### 🌟 Objectifs du projet")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 📚 Éduquer
        Présenter les concepts clés de manière claire et structurée
        """)
    
    with col2:
        st.markdown("""
        #### ✏️ Pratiquer
        Proposer des exercices interactifs avec feedback immédiat
        """)
    
    with col3:
        st.markdown("""
        #### 🔗 Connecter
        Centraliser les meilleures ressources d'apprentissage
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚙️ Fonctionnalités principales")
    
    features = {
        "Fonctionnalité": ["Théorie interactive", "Exercices pratiques", "Graphiques dynamiques", "Ressources curées"],
        "Description": [
            "Concepts expliqués avec exemples",
            "5 exercices avec correction automatique",
            "Visualisations Plotly interactives",
            "Cours, vidéos et articles sélectionnés"
        ],
        "Statut": ["✅ Complet", "✅ Complet", "✅ Complet", "✅ Complet"]
    }
    
    df_features = pd.DataFrame(features)
    st.dataframe(df_features, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("### 👨‍💻 À propos de l'auteur")
    
    col1, col2 = st.columns([1, 2])
    
    with col2:
        st.markdown("""
        **NASRI KHOULOUD**  
        Étudiant(e) en Ingénierie Électrique
        
        Ce portfolio a été développé dans le cadre d'un projet pédagogique visant à 
        partager les connaissances sur la maintenance prédictive de manière interactive 
        et accessible.

        """)









