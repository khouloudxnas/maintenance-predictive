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
    with st.expander("🟩 Niveau 1 — Les 3 types de maintenance", expanded=True):
        st.markdown("## 🟩 Niveau 1 — Corrective, Préventive, Prédictive")
    
        st.markdown("""
        Dans une usine, il existe trois types principaux de maintenance.  
        Chacun a ses avantages et inconvénients.
    
        ---
    
        ### 🔴 1) Maintenance Corrective
        → On intervient **après la panne**  
        ⚠️ Inconvénients :
        - Très coûteuse (arrêts imprévus, pièces à changer rapidement)  
        - Arrêt complet de la production  
        - Risque de détérioration d'autres machines  
    
        ➤ Exemple : un moteur qui s'arrête soudainement et nécessite une réparation d'urgence.
    
        ---
    
        ### 🟡 2) Maintenance Préventive
        → Entretien planifié sur **un calendrier fixe**  
        ⚠️ Limitations :
        - Parfois inutile si la machine est encore en bon état  
        - Planification rigide, pas toujours adaptée aux variations de production  
    
        ➤ Exemple : changer une pièce tous les 6 mois, même si elle est encore fonctionnelle.
    
        ---
    
        ### 🟢 3) Maintenance Prédictive
        → Basée sur l’analyse des **données collectées par les capteurs**  
        ✔️ Avantages :
        - Optimise les interventions (on répare seulement si nécessaire)  
        - Évite les arrêts non planifiés  
        - Réduit les coûts et augmente la durée de vie des équipements  
    
        ➤ Exemple : un capteur détecte une vibration anormale → l’algorithme prévoit une panne → le technicien intervient à temps.
    
        ---
    
        🌟 **À retenir :**
        - Corrective = réagir après la panne  
        - Préventive = suivre un calendrier fixe  
        - Prédictive = anticiper grâce aux données et capteurs
        """)
    
        st.info("💡 Conseil : La maintenance prédictive est la stratégie moderne la plus efficace pour les industries.")


    # -------------------- NIVEAU 2 --------------------
    with st.expander("🟨 Niveau 2 — Capteurs & Données", expanded=True):
        st.markdown("## 🟨 Niveau 2 — Capteurs utilisés en maintenance prédictive")
    
        st.markdown("""
        Pour **anticiper les pannes**, il est crucial de mesurer l'état des machines.  
        Les capteurs sont les **yeux et les oreilles** des équipements industriels.
    
        ---
    
        ### 🌊 Capteur de vibrations
        - Détecte déséquilibres, usure des roulements, désalignements  
        - Permet d’identifier une défaillance mécanique imminente
    
        ### 🌡️ Capteur de température
        - Surveille la surchauffe des moteurs, transformateurs ou machines  
        - Les anomalies thermiques précèdent souvent les pannes
    
        ### ⚡ Capteur de courant électrique
        - Détecte surcharge moteur ou anomalies électriques  
        - Utile pour prévenir les courts-circuits ou surconsommation
    
        ### 🔊 Capteur acoustique / ultrasons
        - Détecte fissures, fuites d’air ou de gaz, bruits anormaux  
        - Permet une maintenance avant l’apparition de dommages visibles
    
        ### 🧰 Capteur de pression
        - Surveille systèmes hydrauliques ou pneumatiques  
        - Permet de détecter fuites ou baisse de performance
    
        ### 💧 Capteur d’humidité
        - Surveille l’humidité dans moteurs ou transformateurs  
        - Prévient la corrosion et les courts-circuits
    
        ---
    
        ### Notions essentielles à connaître
        - **Fréquence d’échantillonnage** : combien de fois les données sont relevées  
        - **Bruit du signal** : perturbations qui peuvent fausser les mesures  
        - **Intervalle de mesure** : période entre deux relevés successifs  
        - **Qualité des données** : données fiables = meilleure prédiction
        """)
    
        st.info("🎯 Une bonne prédiction = données propres + capteurs bien choisis")


    # -------------------- NIVEAU 3 --------------------
    with st.expander("🟧 Niveau 3 — Analyse de données (Data Analysis)", expanded=True):
        st.markdown("## 🟧 Niveau 3 — Analyse des données")
    
        st.markdown("""
        Pour exploiter pleinement les mesures des capteurs, il est essentiel de **transformer les signaux bruts en informations utiles**.
    
        ---
    
        ### Méthodes principales
    
        - 📊 **Statistiques**
          - Calcul de la moyenne, variance, tendances
          - Permet de comprendre le comportement normal des machines
    
        - 🔺 **Détection de pics**
          - Identifier les anomalies soudaines ou événements inhabituels
          - Exemple : un pic de vibration indiquant un roulement qui se détériore
    
        - 📈 **Courbes temporelles**
          - Visualiser l’évolution des mesures dans le temps
          - Identifier les patterns et cycles de dégradation
    
        - 🎧 **Analyse vibratoire**
          - Étude des signatures vibratoires des composants
          - Détection des déséquilibres ou des pièces usées
    
        - 📉 **FFT / Analyse fréquentielle**
          - Convertit le signal temporel en spectre de fréquence
          - Permet de repérer des fréquences caractéristiques de défaillance
    
        ---
    
        ### Objectif
        Transformer les **signaux bruts → en informations → puis en décisions** pour la maintenance.
        """)
    
        st.info("🧠 La Data Analysis est indispensable avant d'appliquer du Machine Learning.")


    # -------------------- NIVEAU 4 --------------------
    with st.expander("🟥 Niveau 4 — Machine Learning & IA", expanded=True):
        st.markdown("## 🟥 Niveau 4 — Machine Learning pour la maintenance prédictive")
    
        st.markdown("""
        La **maintenance prédictive moderne** utilise le Machine Learning (ML) pour **anticiper les pannes**.  
        Les algorithmes apprennent à reconnaître les comportements normaux et à détecter les anomalies.
    
        ---
    
        ### Méthodes ML principales
    
        1️⃣ **Régression**
           - Prédire des valeurs continues (ex. température future, usure d’un roulement)
           - Exemple : prévoir si un moteur va dépasser une limite critique
    
        2️⃣ **Classification**
           - Déterminer l’état de la machine : normal / anomalie
           - Exemple : classifier un signal vibratoire comme sain ou défectueux
    
        3️⃣ **Clustering**
           - Regrouper des comportements inconnus ou similaires
           - Exemple : identifier des modes de fonctionnement inhabituels
    
        4️⃣ **Détection d’anomalies**
           - Repérer des pannes rares ou inédites
           - Exemple : alerte automatique pour une vibration jamais vue auparavant
    
        ---
    
        ### Workflow typique d’un projet ML
        1. **Collecte des données** des capteurs  
        2. **Nettoyage** et prétraitement  
        3. **Feature engineering** (extraction de caractéristiques pertinentes)  
        4. **Entraînement du modèle** sur données historiques  
        5. **Test et validation**  
        6. **Déploiement** pour la détection en temps réel
    
        """)
    
        st.info("🤖 Le Machine Learning permet de transformer les données brutes en décisions intelligentes et actions préventives.")


    # -------------------- NIVEAU 5 --------------------
    with st.expander("🟪 Niveau 5 — Modèles avancés (Deep Learning)", expanded=True):
        st.markdown("## 🟪 Niveau 5 — Deep Learning pour la maintenance prédictive")
    
        st.markdown("""
        Quand les signaux deviennent complexes ou volumineux, le **Deep Learning (DL)** est idéal.  
        Il peut apprendre des patterns très subtils que le ML classique ne détecte pas.
    
        ---
    
        ### Modèles DL courants
    
        - **CNN (Convolutional Neural Networks)**
          - Utilisés pour les **images et spectrogrammes vibratoires**
          - Exemple : analyser la signature vibratoire d’un moteur
    
        - **LSTM / GRU (Long Short-Term Memory / Gated Recurrent Unit)**
          - Séries temporelles longues
          - Exemple : prédire la température ou la vibration sur plusieurs jours
    
        - **Auto-encoders**
          - Détection d’anomalies sans étiquettes (non-supervisé)
          - Exemple : repérer un comportement jamais observé dans les données
    
        ---
    
        ### Avantages et limites
        - ✅ Très puissant pour des signaux complexes
        - ✅ Capable de détecter des anomalies subtiles
        - ❌ Besoin de **grandes quantités de données**
        - ❌ Plus coûteux en calcul
    
        """)
    
        st.info("🌟 Astuce : utiliser DL uniquement pour des signaux complexes ou de très grandes installations industrielles.")


    # -------------------- NIVEAU 6 --------------------
    with st.expander("🟫 Niveau 6 — Architecture IoT", expanded=True):
        st.markdown("## 🟫 Niveau 6 — Architecture IoT complète pour la maintenance prédictive")
    
        st.markdown("""
        Une installation de maintenance prédictive moderne repose sur une **architecture IoT**.  
        Chaque composant a un rôle clé pour collecter, traiter et analyser les données en temps réel.
    
        ---
    
        ### 1) 📡 Capteurs
        - Capturent les signaux physiques : vibration, température, courant, acoustique, pression…
        - Qualité et fréquence d’échantillonnage cruciales pour de bonnes prédictions
        - Exemples : accéléromètres, thermocouples, capteurs de courant, microphones
    
        ### 2) 🧠 Edge Computing (Raspberry Pi / Microcontrôleur)
        - Prétraitement des données à proximité de la machine
        - Nettoyage, filtrage, réduction du bruit
        - Exécution de mini-modèles ML pour détection rapide d’anomalies
        - Réduit la latence et la charge réseau
    
        ### 3) ☁️ Cloud (AWS, Azure, GCP)
        - Stockage centralisé de grandes quantités de données
        - Entraînement de modèles ML/DL complexes
        - Analyse globale et corrélation entre machines et sites
        - Facilite l’accès aux historiques et aux KPI
    
        ### 4) 📊 Dashboard (Power BI, Grafana, Streamlit)
        - Visualisation des données en temps réel
        - Suivi des indicateurs clés : MTBF, MTTR, disponibilité, anomalies
        - Alertes et recommandations pour la maintenance proactive
    
        ---
    
        💡 **Astuce :** Prétraiter les données en edge permet de réduire le trafic réseau et la latence, tout en détectant rapidement les anomalies.
        """)


    # -------------------- NIVEAU 7 --------------------
with st.expander("🟦 Niveau 7 — Workflow réel en usine", expanded=True):
        st.markdown("## 🟦 Niveau 7 — Workflow complet d’un projet de maintenance prédictive en usine")
    
        st.markdown("""
        Dans une usine moderne, la maintenance prédictive suit un **processus structuré** pour garantir la fiabilité et réduire les coûts.  
    
        ### Étapes principales :
    
        1️⃣ **Collecte des données**
        - Capteurs installés sur machines
        - Mesures de vibration, température, courant, acoustique, pression…
        - Transmission des données vers un serveur ou edge device
    
        2️⃣ **Nettoyage des données**
        - Suppression des valeurs aberrantes (outliers)
        - Gestion des valeurs manquantes
        - Filtrage du bruit pour améliorer la qualité
    
        3️⃣ **Feature Engineering**
        - Extraction de caractéristiques pertinentes : RMS, kurtosis, moyenne mobile…
        - Transformation des signaux bruts en informations exploitables
    
        4️⃣ **Entraînement ML / IA**
        - Modèles supervisés ou non supervisés
        - Régression, classification, clustering, détection d’anomalies
        - Validation et test pour s’assurer de la fiabilité
    
        5️⃣ **Détection d’anomalies**
        - Identification des comportements anormaux ou des signes précurseurs de panne
        - Détection en temps réel ou batch selon l’infrastructure
    
        6️⃣ **Envoi d’alertes**
        - Notifications aux techniciens ou planificateurs
        - SMS, email, dashboard, applications mobiles
    
        7️⃣ **Planification de maintenance**
        - Décision basée sur les alertes et le calendrier
        - Optimisation des interventions pour éviter les arrêts non planifiés
    
        8️⃣ **Suivi des KPI**
        - MTBF, MTTR, disponibilité, taux d’anomalies
        - Analyse continue pour améliorer le processus
        """)
    
        st.success("🎯 Retenir : c’est le cycle complet d’un système industriel moderne, combinant capteurs, données, IA et actions concrètes.")

    # -------------------- NIVEAU 8 --------------------
    with st.expander("🟫 Niveau 8 — KPI essentiels", expanded=True):
        st.markdown("## 🟫 Niveau 8 — Les indicateurs clés de la maintenance prédictive")
    
        st.markdown("""
        Les **KPI (Key Performance Indicators)** permettent de mesurer la performance et l’efficacité de la maintenance.  
    
        ### Principaux KPI :
    
        - ⏱️ **MTBF (Mean Time Between Failures)**  
          → Temps moyen entre deux pannes d’une machine  
          **Exemple :** Une machine tombe en panne 4 fois sur 400 h → MTBF = 400 / 4 = 100 h
    
        - 🔧 **MTTR (Mean Time To Repair)**  
          → Temps moyen nécessaire pour réparer une panne  
          **Exemple :** Temps total de réparation = 20 h, 4 pannes → MTTR = 20 / 4 = 5 h
    
        - ⚙️ **Disponibilité**  
          → Pourcentage de temps où la machine est opérationnelle  
          **Formule :** Disponibilité = MTBF / (MTBF + MTTR)  
          **Exemple :** 100 / (100 + 5) ≈ 95.2%
    
        - 📉 **Taux d’anomalies**  
          → Proportion des incidents détectés par le système prédictif  
          **Objectif :** Identifier et réduire les anomalies avant panne
    
        - 💸 **Coût d’arrêt de production**  
          → Évalue l’impact financier d’une panne ou d’un arrêt programmé
        """)
    
        st.info("🎯 Retenir : Suivre ces KPI permet de prouver l’efficacité du système et d’optimiser la maintenance.")


    # -------------------- NIVEAU 9 --------------------
    with st.expander("🟩 Niveau 9 — Cas pratiques", expanded=True):
        st.markdown("## 🟩 Niveau 9 — Cas pratiques inspirés du réel")
    
        st.markdown("""
        ### Exemples concrets de maintenance prédictive :
    
        - 🔧 **Défaillance moteur**  
          → Mesures : vibrations + courant  
          → Objectif : détecter l'usure des roulements avant panne  
    
        - 🎧 **Analyse acoustique de compresseurs**  
          → Mesures : bruit, ultrasons  
          → Objectif : repérer fuites d'air ou anomalies mécaniques  
    
        - 🔥 **Suivi de température de fours industriels**  
          → Mesures : capteurs thermiques  
          → Objectif : anticiper surchauffe ou dysfonctionnement  
    
        - ⚙️ **Roulements et pièces rotatives**  
          → Mesures : analyse FFT + signatures vibratoires  
          → Objectif : prévoir la défaillance avant arrêt de production  
    
        - 🏭 **Lignes d'assemblage multi-capteurs**  
          → Mesures : vibration, courant, température, pression  
          → Objectif : construire un modèle prédictif pour l'ensemble de la ligne
    
        💡 Chaque cas peut être considéré comme un mini-projet : collecte de données, nettoyage, analyse, modèle prédictif et suivi KPI.
        """)
    
        st.success("🌟 Astuce : Ces mini-projets sont parfaits pour pratiquer Python, Plotly et Machine Learning en maintenance prédictive.")



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















