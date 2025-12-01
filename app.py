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
    ["🏠 Accueil", "📚 Théorie", "📖 Ressources", "✏️ Exercices", "📈 Upload & Analyse", "ℹ️ À propos"],
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
        st.metric("✏️ Exercices", "7", "Pratiques")
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
            st.write("Explorez des ressources PDF, vidéos et datasets pour pratiquer et approfondir vos compétences.")
            
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
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎓 Cours en ligne", "🎬 Vidéos", "📄 PDFs", "📊 Datasets"])

    
    with tab1:
        st.markdown("### Formations complètes")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### 🎓 Mathworks
            
            Cours Gratuits
            
            [Introduction à la maintenance prédictive →](https://fr.mathworks.com/discovery/predictive-maintenance.html)
            [Série de vidéos sur la maintenance prédictive →](https://fr.mathworks.com/videos/series/predictive-maintenance-tech-talk-series.html)
            [Predictive Maintenance Toolbox →](https://fr.mathworks.com/videos/predictive-maintenance-toolbox-overview-1519682269879.html)
            [Predictive Maintenance: Prognostics and Health Monitoring →](https://fr.mathworks.com/videos/predictive-maintenance-with-matlab-120998.html)
            [Predictive Maintenance with MATLAB: A Data-Based Approach Overview →](https://fr.mathworks.com/videos/predictive-maintenance-with-matlab-a-data-based-approach-1635953744450.html)
            [Predictive Maintenance Toolbox — Examples →](https://fr.mathworks.com/help/predmaint/examples.html)
            [Des jumeaux numériques pour la maintenance prédictive →](https://fr.mathworks.com/campaigns/offers/next/digital-twins-for-predictive-maintenance.html)
            """)
        
        with col2:
            st.markdown("""
            #### 🎓 Udemy

            Cours Payants
       
            - [predictive-maintenance →](https://www.udemy.com/course/master-in-predictive-maintenance/)
            - [preventive-maintenance-basics →](https://www.udemy.com/course/preventive-maintenance-basics/)
            - [Cours Machine Learning →](https://www.udemy.com/course/predictive-maintenance-with-iot-and-machine-learning/)
            """)
    
    with tab2:
        st.markdown("### Tutoriels YouTube")
        st.markdown("""
        - 🎬 [Explication de la maintenance prédictive](https://www.youtube.com/watch?v=2_o1SDy6__U&t=21s&pp=ygUXbWFpbnRlbmFuY2UgcHLDqWRpY3RpdmU%3D)
        - 🎬 [Getting Started with Predictive Maintenance](https://www.youtube.com/watch?v=RmVWKLbLq2Y&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_)
        - 🎬 [Identifying Condition Indicators | Predictive Maintenance](https://www.youtube.com/watch?v=pcXr8I2QvHw&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_&index=2)
        - 🎬[Estimating Remaining Useful Life (RUL) for Prognostics | Predictive Maintenance](https://www.youtube.com/watch?v=Dd_4rbWYgI4&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_&index=3)
        - 🎬[Feature Extraction Using Diagnostic Feature Designer | Predictive Maintenance](https://www.youtube.com/watch?v=oDd7aEmRNpI&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_&index=4)
        - 🎬[What is a Digital Twin?](https://www.youtube.com/watch?v=cfbKR48nSyQ&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_&index=5)
        - 🎬[Predictive Maintenance with MATLAB A Prognostics Case Study](https://www.youtube.com/watch?v=9QUM5jtB0t4&list=PLldSvyce5wd7kKt0p4hUT9FTH66NZat1_&index=6)
        - 🎬[Predictive Maintenance & IoT](https://www.youtube.com/watch?v=glX3_OBtX-Q)
        - 🎬[EP2 - Analyse vibratoire - mesure et exploitation des resultats](https://www.youtube.com/watch?v=-fqQOW9sz2U)
        - 🎬[What is a Vibration Sensor?](https://www.youtube.com/watch?v=3KsRjnn83T0)
        - 🎬[Thermographie infrarouge](https://youtube.com/shorts/x20Vibr2yhE?si=KEPkBrk1BueUphtW)
        - 🎬[C_MAPSS Predictive Maintenance](https://www.youtube.com/watch?v=_jaXkoeygko)
        - 🎬[Turbo Engine RUL Prediction: A Machine Learning Approach](https://www.youtube.com/watch?v=5PKvOZU6RGQ&t=958s)
        - 🎬[Understanding Predictive Maintenance (serie des videos)](https://www.youtube.com/watch?v=xbRrC2_nAJQ)
        """)
    
    with tab3:
        st.markdown("[Ressources PDF →](https://drive.google.com/drive/folders/1VAjV-7u9YLm3CSw-CJ9mVapuozQis6hP?usp=sharing)")
    with tab4:
        st.markdown("## 📊 Jeux de données pour la maintenance prédictive")
        st.markdown("""
        1️⃣ **NASA — C-MAPSS (Turbofan Engine RUL)**  
        - Usage : estimation du RUL, modèles séquentiels (LSTM, survival regression…)  
        - Format : fichiers texte / CSV (train / test / truth)  
        - Idéal pour : features time-series, segmentation  
        - [Télécharger / Source officielle](https://data.nasa.gov/dataset/)  
    
        2️⃣ **Kaggle / miroirs du C-MAPSS**  
        - Usage : ZIP/CSV prêt à l’emploi + notebooks Python  
        - [Télécharger sur Kaggle](https://www.kaggle.com/datasets/)  
    
        3️⃣ **FEMTO / PRONOSTIA — Roulements run-to-failure**  
        - Usage : données vibratoires de roulements, RUL des roulements  
        - Format : .mat / .txt / zip  
        - [Télécharger / NASA PCoE](https://data.nasa.gov/dataset/) | [GitHub / Kaggle miroirs](https://github.com/)  
    
        4️⃣ **IMS Bearings (University of Cincinnati)**  
        - Usage : essais de roulements (vibrations), diagnostics et RUL  
        - Format : zip avec séries temporelles (wav/txt)  
        - [Data.gov / IMS](https://data.gov/)  
    
        5️⃣ **IEEE PHM 2012 — Bearing dataset**  
        - Usage : challenge PHM 2012, reproductions comparables  
        - Format : zip / CSV / mat  
        - [GitHub](https://github.com/) | [Kaggle](https://www.kaggle.com/)  
    
        6️⃣ **IEEE PHM / autres jeux (batteries, turbomachines)**  
        - Usage : tests multi-composants, challenges PHM  
        - [Kaggle](https://www.kaggle.com/) | [NASA PCoE](https://data.nasa.gov/dataset//)
        """)


# EXERCICES
elif section == "✏️ Exercices":
    st.title("✏️ Exercices et Cas Pratiques")
    st.markdown("### Testez vos connaissances avec des exercices interactifs")
    
    # ===================== Niveau 0 =====================
    with st.expander("🟦 Théorie simple"):
        st.markdown("#### Exercice 1 : Objectif de la maintenance prédictive")
        reponse0_1 = st.radio("Quelle est la fonction principale ?", 
                              ("Réparer après panne", "Entretien planifié", "Anticiper les pannes"), key="n0_1")
        if st.button("Vérifier Exercice 1 (N0)", key="btn_n0_1"):
            if reponse0_1 == "Anticiper les pannes":
                st.success("✅ Correct !")
            else:
                st.error("❌ Ce n'est pas correct.")
        
        st.markdown("#### Exercice 2 : Exemple simple")
        reponse0_2 = st.radio("Si une voiture fait un bruit suspect, quelle action illustre la maintenance prédictive ?", 
                              ("Ignorer", "Aller chez le mécanicien avant panne", "Réparer après panne"), key="n0_2")
        if st.button("Vérifier Exercice 2 (N0)", key="btn_n0_2"):
            if reponse0_2 == "Aller chez le mécanicien avant panne":
                st.success("✅ Exact !")
            else:
                st.error("❌ Mauvaise réponse.")

    # ===================== Niveau 1 =====================
    with st.expander("🟩 Types de maintenance"):
        st.markdown("#### Exercice 1 : Identifier la maintenance corrective")
        reponse1_1 = st.radio("Intervient après panne ?", ("Corrective", "Préventive", "Prédictive"), key="n1_1")
        if st.button("Vérifier Exercice 1 (N1)", key="btn_n1_1"):
            if reponse1_1 == "Corrective":
                st.success("✅ Correct !")
            else:
                st.error("❌ Non, après panne = corrective.")
        
        st.markdown("#### Exercice 2 : Identifier la maintenance prédictive")
        reponse1_2 = st.radio("Basée sur l'analyse des capteurs ?", ("Corrective", "Préventive", "Prédictive"), key="n1_2")
        if st.button("Vérifier Exercice 2 (N1)", key="btn_n1_2"):
            if reponse1_2 == "Prédictive":
                st.success("✅ Correct !")
            else:
                st.error("❌ Mauvaise réponse.")

    # ===================== Niveau 2 =====================
    with st.expander("🟨 Capteurs & Données"):
        st.markdown("#### Exercice 1 : Identifier les anomalies de température")
        temp_data = [70, 72, 71, 74, 78, 80, 72, 71, 69, 82]
        st.write(temp_data)
        anomalies = st.multiselect("Indices (>75°C) ?", options=list(range(len(temp_data))), key="n2_1")
        reponse2_1 = [4,5,5,9]
        if st.button("Vérifier Exercice 1 (N2)", key="btn_n2_1"):
            if set(anomalies) == set([4,5,9]):
                st.success("✅ Correct !")
            else:
                st.error("❌ Indices corrects : 4, 5, 9")
        
        st.markdown("#### Exercice 2 : Choisir le bon capteur")
        reponse2_2 = st.radio("Pour détecter une surcharge moteur ?", 
                              ("Capteur de pression", "Capteur de courant", "Capteur acoustique"), key="n2_2")
        if st.button("Vérifier Exercice 2 (N2)", key="btn_n2_2"):
            if reponse2_2 == "Capteur de courant":
                st.success("✅ Correct !")
            else:
                st.error("❌ Le courant indique la surcharge moteur.")

    # ===================== Niveau 3 =====================
    with st.expander("🟧 Analyse de données"):
        st.markdown("#### Exercice 1 : Détection de pics")
        jours = pd.date_range(start="2025-12-01", periods=15)
        vibration = np.random.normal(5, 1, 15)
        vibration[3] = 7
        vibration[10] = 8
        df = pd.DataFrame({"Jour": jours, "Vibration": vibration})
        st.write(df)
        anomalies3_1 = st.multiselect("Sélectionnez les jours avec vibration >6", 
                                      options=df['Jour'].dt.strftime('%Y-%m-%d').tolist(), key="n3_1")
        reponse3_1 = ["2025-12-04","2025-12-11"]
        if st.button("Vérifier Exercice 1 (N3)", key="btn_n3_1"):
            if set(anomalies3_1) == set(reponse3_1):
                st.success("✅ Correct !")
            else:
                st.error(f"❌ Les jours corrects : {', '.join(reponse3_1)}")
        
        st.markdown("#### Exercice 2 : Calcul simple")
        st.markdown("Mesures : [5,6,7,8,5], Calculer la moyenne")
        moyenne_input = st.number_input("Moyenne :", min_value=0.0, step=0.1, key="n3_2")
        if st.button("Vérifier Exercice 2 (N3)", key="btn_n3_2"):
            if abs(moyenne_input-6.2)<0.01:
                st.success("✅ Correct !")
            else:
                st.error("❌ La moyenne correcte = 6.2")


        # ===================== Niveau 4 =====================
    with st.expander("🟥 KPI & Calcul"):
        st.markdown("#### Exercice 1 : Calcul MTBF et MTTR")
        # ✅ Affichage des données
        nb_pannes = 5
        temps_fonctionnement = 500
        temps_reparation = 25
        st.write(f"**Données :** Nombre de pannes = {nb_pannes}, Temps de fonctionnement = {temps_fonctionnement} h, Temps de réparation = {temps_reparation} h")
        
        # Formules
        st.markdown("""
        **Formules :**  
        - MTBF = Temps total de fonctionnement / Nombre de pannes  
        - MTTR = Temps total de réparation / Nombre de pannes
        """)
        
        mtbf_input = st.number_input("MTBF (heures) :", key="n4_1")
        mttr_input = st.number_input("MTTR (heures) :", key="n4_2")
        
        if st.button("Vérifier Exercice 1 (N4)", key="btn_n4_1"):
            mtbf_correct = temps_fonctionnement / nb_pannes
            mttr_correct = temps_reparation / nb_pannes
            if mtbf_input == mtbf_correct and mttr_input == mttr_correct:
                st.success("✅ Correct !")
            else:
                st.error(f"❌ Réponses correctes : MTBF = {mtbf_correct} h, MTTR = {mttr_correct} h")
    
        st.markdown("#### Exercice 2 : Calcul Disponibilité")
        st.write("**Formule :** Disponibilité = (Temps de fonctionnement - Temps de réparation) / Temps de fonctionnement × 100")
        
        dispo_input = st.number_input("Disponibilité (%) :", key="n4_3")
        
        if st.button("Vérifier Exercice 2 (N4)", key="btn_n4_2"):
            dispo_correct = (temps_fonctionnement - temps_reparation) / temps_fonctionnement * 100
            if abs(dispo_input - dispo_correct) < 0.5:
                st.success("✅ Correct !")
            else:
                st.error(f"❌ Disponibilité correcte = {round(dispo_correct,1)}%")
    
    # ===================== Niveau 5 =====================
    with st.expander("🟪 Prédiction de panne"):
        st.markdown("#### Exercice 1 : Vérification seuils")
        # ✅ Affichage des données
        vibration, temperature, courant = 7, 78, 5
        st.write(f"**Données :** Vibration = {vibration} mm/s, Température = {temperature} °C, Courant = {courant} A")
        
        # Formules / seuils
        st.markdown("""
        **Seuils critiques :**  
        - Vibration > 6 mm/s → risque de panne  
        - Température > 75 °C → risque de panne  
        - Courant > 6 A → risque de surcharge
        """)
        
        prediction = st.radio("La machine va-t-elle tomber en panne ?", ("Oui","Non"), key="n5_1")
    
        if st.button("Vérifier Exercice 1 (N5)", key="btn_n5_1"):
            if vibration > 6 or temperature > 75 or courant > 6:
                if prediction == "Oui":
                    st.success("✅ Correct ! La machine présente des signes de défaillance.")
                else:
                    st.error("❌ La machine dépasse les seuils critiques !")
            else:
                if prediction == "Non":
                    st.success("✅ Correct, la machine est normale.")
                else:
                    st.error("❌ Aucun seuil critique n'est dépassé.")
    
        st.markdown("#### Exercice 2 : Analyse multi-capteurs")
        vibration, temperature, courant = 5, 70, 7
        st.write(f"**Données :** Vibration = {vibration} mm/s, Température = {temperature} °C, Courant = {courant} A")
        
        st.markdown("""
        **Seuils critiques :**  
        - Vibration > 6 mm/s  
        - Température > 75 °C  
        - Courant > 6 A
        """)
    
        prediction2 = st.radio("Panne probable ?", ("Oui","Non"), key="n5_2")
    
        if st.button("Vérifier Exercice 2 (N5)", key="btn_n5_2"):
            if courant > 6:
                if prediction2 == "Oui":
                    st.success("✅ Correct ! Courant > seuil critique.")
                else:
                    st.error("❌ Le courant dépasse le seuil critique.")
            else:
                if prediction2 == "Non":
                    st.success("✅ Correct, tout est normal.")
                else:
                    st.error("❌ Aucun paramètre critique n'est dépassé.")
    # ===================== Niveau 6 =====================
    with st.expander("🛠️ Problème complet — Analyse IoT d'une machine"):
        st.markdown("#### Contexte :")
        st.markdown("""
        Une usine a mis en place un système IoT sur une ligne de production.  
        Les capteurs mesurent :
        - Vibration (mm/s)
        - Température (°C)
        - Courant (A)
        
        Les mesures collectées sur 5 jours sont les suivantes :
        """)
        
        import pandas as pd
        data = {
            "Jour": ["J1", "J2", "J3", "J4", "J5"],
            "Vibration (mm/s)": [5.1, 6.5, 7.0, 5.8, 6.2],
            "Température (°C)": [72, 76, 80, 74, 78],
            "Courant (A)": [5.0, 6.2, 6.8, 5.5, 6.1],
            "Temps de fonctionnement (h)": [24, 24, 24, 24, 24],
            "Temps de réparation (h)": [0, 1, 2, 0, 1]
        }
        df = pd.DataFrame(data)
        st.dataframe(df)
        
        st.markdown("""
        **Seuils critiques :**
        - Vibration > 6 mm/s  
        - Température > 75 °C  
        - Courant > 6 A
        """)
        
        st.markdown("#### Questions :")
        
        # Question 1 : Identifier les jours critiques
        jours_critique = st.multiselect(
            "Sélectionnez les jours où au moins un capteur dépasse le seuil :",
            options=df["Jour"].tolist()
        )
        
        # Question 2 : Calcul MTBF et MTTR pour la ligne
        mtbf_input = st.number_input("MTBF total (heures) :", key="n6_prob_mtbf")
        mttr_input = st.number_input("MTTR total (heures) :", key="n6_prob_mttr")
        
        if st.button("Vérifier l'exercice (N6)", key="btn_n6_prob"):
            # Points critiques : J2, J3, J5
            correct_jours = ["J2", "J3", "J5"]
            mtbf_correct = df["Temps de fonctionnement (h)"].sum() / 3  # 3 pannes
            mttr_correct = df["Temps de réparation (h)"].sum() / 3
            
            # Vérification
            if set(jours_critique) == set(correct_jours):
                st.success("✅ Correct ! Jours critiques identifiés.")
                st.info("💡 J2, J3, J5 ont au moins un capteur dépassant le seuil.")
            else:
                st.error(f"❌ Les jours corrects sont : {', '.join(correct_jours)}")
            
            if mtbf_input == mtbf_correct and mttr_input == mttr_correct:
                st.success(f"✅ MTBF et MTTR corrects ! MTBF={mtbf_correct} h, MTTR={mttr_correct} h")
                st.info("💡 Formules : MTBF = Temps total / Nombre de pannes | MTTR = Temps réparation total / Nombre de pannes")
            else:
                st.error(f"❌ Vérifiez vos calculs : MTBF={mtbf_correct} h, MTTR={mttr_correct} h")



# ===================== UPLOAD & ANALYSE =====================
# ===================== UPLOAD & ANALYSE =====================
elif section == "📈 Upload & Analyse":
    st.title("📈 Upload & Analyse de Données")
    st.markdown("### Importez votre dataset et votre modèle pour analyser vos données de maintenance")
    
    tab1, tab2, tab3 = st.tabs(["📊 Upload Dataset", "🤖 Upload Modèle", "📈 Analyse & Résultats"])
    
    # ==================== TAB 1 : Upload Dataset ====================
    with tab1:
        st.markdown("### 📊 Importez vos données")
        
        uploaded_file = st.file_uploader(
            "Choisissez un fichier CSV",
            type=['csv'],
            help="Fichier CSV contenant les données des capteurs (vibration, température, courant, etc.)",
            key="dataset_upload"
        )
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success(f"✅ Fichier chargé avec succès ! ({len(df)} lignes, {len(df.columns)} colonnes)")
                
                # Aperçu des données
                st.markdown("#### 🔍 Aperçu des données")
                st.dataframe(df.head(10), use_container_width=True)
                
                # Informations sur le dataset
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("📊 Lignes", len(df))
                with col2:
                    st.metric("📋 Colonnes", len(df.columns))
                with col3:
                    st.metric("❌ Valeurs manquantes", df.isnull().sum().sum())
                with col4:
                    st.metric("💾 Taille", f"{uploaded_file.size / 1024:.1f} KB")
                
                # Statistiques descriptives
                with st.expander("📊 Statistiques descriptives"):
                    st.dataframe(df.describe(), use_container_width=True)
                
                # Stocker dans session_state
                st.session_state['dataset'] = df
                st.session_state['dataset_loaded'] = True
                
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement du fichier : {str(e)}")
        else:
            st.info("👆 Veuillez importer un fichier CSV pour commencer l'analyse")
    
# ==================== TAB 2 : Upload Modèle ====================# ===================== UPLOAD & ANALYSE =====================

elif section == "📈 Upload & Analyse":
    st.title("📈 Upload & Analyse de Données")
    st.markdown("### Importez votre dataset et votre modèle pour analyser vos données de maintenance")
    
    tab1, tab2, tab3 = st.tabs(["📊 Upload Dataset", "🤖 Upload Modèle", "📈 Analyse & Résultats"])
    
    # ==================== TAB 1 : Upload Dataset ====================
    with tab1:
        st.markdown("### 📊 Importez vos données")
        
        uploaded_file = st.file_uploader(
            "Choisissez un fichier CSV",
            type=['csv'],
            help="Fichier CSV contenant les données des capteurs (vibration, température, courant, etc.)",
            key="dataset_upload"
        )
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.success(f"✅ Fichier chargé avec succès ! ({len(df)} lignes, {len(df.columns)} colonnes)")
                
                # Aperçu des données
                st.markdown("#### 🔍 Aperçu des données")
                st.dataframe(df.head(10), use_container_width=True)
                
                # Informations sur le dataset
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("📊 Lignes", len(df))
                with col2:
                    st.metric("📋 Colonnes", len(df.columns))
                with col3:
                    st.metric("❌ Valeurs manquantes", df.isnull().sum().sum())
                with col4:
                    st.metric("💾 Taille", f"{uploaded_file.size / 1024:.1f} KB")
                
                # Statistiques descriptives
                with st.expander("📊 Statistiques descriptives"):
                    st.dataframe(df.describe(), use_container_width=True)
                
                # Stocker dans session_state
                st.session_state['dataset'] = df
                st.session_state['dataset_loaded'] = True
                
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement du fichier : {str(e)}")
        else:
            st.info("👆 Veuillez importer un fichier CSV pour commencer l'analyse")
    
    # ==================== TAB 2 : Upload Modèle ====================
    with tab2:
        st.markdown("### 🤖 Importez votre modèle entraîné")
        
        uploaded_model = st.file_uploader(
            "Choisissez un fichier modèle (.pkl, .h5, .joblib)",
            type=['pkl', 'h5', 'joblib'],
            help="Modèle entraîné pour la prédiction de RUL ou détection d'anomalies",
            key="model_upload"
        )
        
        if uploaded_model is not None:
            try:
                import pickle
                import joblib
                
                # Charger le modèle selon l'extension
                if uploaded_model.name.endswith('.pkl'):
                    model = pickle.load(uploaded_model)
                elif uploaded_model.name.endswith('.joblib'):
                    model = joblib.load(uploaded_model)
                elif uploaded_model.name.endswith('.h5'):
                    st.warning("⚠️ Pour les modèles .h5, TensorFlow/Keras doit être installé")
                    # from tensorflow import keras
                    # model = keras.models.load_model(uploaded_model)
                
                st.success(f"✅ Modèle chargé avec succès : {uploaded_model.name}")
                st.info(f"📦 Type de modèle : {type(model).__name__}")
                
                # Stocker dans session_state
                st.session_state['model'] = model
                st.session_state['model_loaded'] = True
                
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement du modèle : {str(e)}")
        else:
            st.info("👆 Veuillez importer un modèle pour effectuer des prédictions")
    
    # ==================== TAB 3 : Analyse & Résultats ====================
    with tab3:
        st.markdown("### 📈 Analyse des données et prédictions")
        
        # Vérifier si dataset et modèle sont chargés
        if 'dataset_loaded' not in st.session_state or not st.session_state['dataset_loaded']:
            st.warning("⚠️ Veuillez d'abord charger un dataset dans l'onglet 'Upload Dataset'")
            st.stop()
        
        df = st.session_state['dataset']
        
        # ========== VISUALISATION DES DONNÉES ==========
        st.markdown("#### 📊 Visualisation des données")
        
        # Sélection des colonnes à visualiser
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        
        if len(numeric_cols) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
                selected_feature = st.selectbox(
                    "Sélectionnez une variable à visualiser",
                    options=numeric_cols,
                    key="viz_feature"
                )
            
            with col2:
                chart_type = st.selectbox(
                    "Type de graphique",
                    options=["Ligne", "Histogramme", "Box Plot"],
                    key="chart_type"
                )
            
            # Créer le graphique
            if chart_type == "Ligne":
                fig = px.line(
                    df,
                    y=selected_feature,
                    title=f"Évolution de {selected_feature}",
                    labels={'index': 'Index', selected_feature: selected_feature}
                )
            elif chart_type == "Histogramme":
                fig = px.histogram(
                    df,
                    x=selected_feature,
                    title=f"Distribution de {selected_feature}",
                    nbins=30
                )
            else:  # Box Plot
                fig = px.box(
                    df,
                    y=selected_feature,
                    title=f"Box Plot de {selected_feature}"
                )
            
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # ========== CALCUL DES KPIs ==========
        st.markdown("#### 📊 Calcul des KPIs de Maintenance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### Paramètres pour calcul MTBF/MTTR")
            nb_pannes = st.number_input("Nombre de pannes", min_value=1, value=5, step=1)
            temps_fonctionnement = st.number_input("Temps total de fonctionnement (h)", min_value=1, value=500, step=10)
            temps_reparation = st.number_input("Temps total de réparation (h)", min_value=0, value=25, step=1)
        
        with col2:
            if st.button("🔢 Calculer les KPIs", type="primary"):
                # Calculs
                mtbf = temps_fonctionnement / nb_pannes
                mttr = temps_reparation / nb_pannes
                disponibilite = (mtbf / (mtbf + mttr)) * 100
                
                # Affichage des résultats
                st.markdown("##### ✅ Résultats")
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("⏱️ MTBF", f"{mtbf:.1f} h")
                with col_b:
                    st.metric("🔧 MTTR", f"{mttr:.1f} h")
                with col_c:
                    st.metric("⚙️ Disponibilité", f"{disponibilite:.1f} %")
                
                # Stocker dans session_state
                st.session_state['kpis'] = {
                    'mtbf': mtbf,
                    'mttr': mttr,
                    'disponibilite': disponibilite
                }
        
        st.markdown("---")
        
        # ========== PRÉDICTION RUL ==========
        st.markdown("#### 🔮 Prédiction du RUL (Remaining Useful Life)")
        
        if 'model_loaded' in st.session_state and st.session_state['model_loaded']:
            model = st.session_state['model']
            
            st.info("💡 Assurez-vous que vos données sont prétraitées de la même manière que lors de l'entraînement du modèle")
            
            if st.button("🚀 Lancer la prédiction RUL", type="primary"):
                try:
                    # Prédiction (adapter selon votre modèle)
                    # Exemple simplifié : prédire sur tout le dataset
                    predictions = model.predict(df[numeric_cols])
                    
                    # Ajouter les prédictions au DataFrame
                    df['RUL_Predicted'] = predictions
                    
                    st.success("✅ Prédictions effectuées avec succès !")
                    
                    # Affichage des résultats
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("📊 RUL Moyen", f"{predictions.mean():.2f}")
                        st.metric("📉 RUL Min", f"{predictions.min():.2f}")
                    
                    with col2:
                        st.metric("📈 RUL Max", f"{predictions.max():.2f}")
                        st.metric("📊 Écart-type", f"{predictions.std():.2f}")
                    
                    # Graphique des prédictions
                    fig = px.line(
                        df,
                        y='RUL_Predicted',
                        title="Évolution du RUL Prédit",
                        labels={'index': 'Index', 'RUL_Predicted': 'RUL (cycles)'}
                    )
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Téléchargement des résultats
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Télécharger les résultats (CSV)",
                        data=csv,
                        file_name="predictions_RUL.csv",
                        mime="text/csv"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
                    st.info("💡 Vérifiez que les colonnes du dataset correspondent aux features attendues par le modèle")
        else:
            st.warning("⚠️ Veuillez d'abord charger un modèle dans l'onglet 'Upload Modèle'")
        
        # ========== DÉTECTION D'ANOMALIES ==========
        st.markdown("---")
        st.markdown("#### 🚨 Détection d'Anomalies")
        
        if len(numeric_cols) > 0:
            anomaly_feature = st.selectbox(
                "Sélectionnez la variable pour détecter les anomalies",
                options=numeric_cols,
                key="anomaly_feature"
            )
            
            threshold = st.slider(
                "Définir le seuil (écart-type)",
                min_value=1.0,
                max_value=5.0,
                value=3.0,
                step=0.1
            )
            
            if st.button("🔍 Détecter les anomalies", type="primary"):
                # Calcul des anomalies basé sur l'écart-type
                mean = df[anomaly_feature].mean()
                std = df[anomaly_feature].std()
                
                df['Anomaly'] = (df[anomaly_feature] > mean + threshold * std) | \
                                (df[anomaly_feature] < mean - threshold * std)
                
                nb_anomalies = df['Anomaly'].sum()
                
                st.metric("🚨 Nombre d'anomalies détectées", nb_anomalies)
                
                # Visualisation
                fig = go.Figure()
                
                # Points normaux
                fig.add_trace(go.Scatter(
                    x=df[~df['Anomaly']].index,
                    y=df[~df['Anomaly']][anomaly_feature],
                    mode='markers',
                    name='Normal',
                    marker=dict(color='blue', size=5)
                ))
                
                # Points anomalies
                fig.add_trace(go.Scatter(
                    x=df[df['Anomaly']].index,
                    y=df[df['Anomaly']][anomaly_feature],
                    mode='markers',
                    name='Anomalie',
                    marker=dict(color='red', size=8, symbol='x')
                ))
                
                # Lignes de seuil
                fig.add_hline(y=mean + threshold * std, line_dash="dash", line_color="red", annotation_text="Seuil haut")
                fig.add_hline(y=mean - threshold * std, line_dash="dash", line_color="red", annotation_text="Seuil bas")
                
                fig.update_layout(
                    title=f"Détection d'anomalies - {anomaly_feature}",
                    xaxis_title="Index",
                    yaxis_title=anomaly_feature,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Afficher les anomalies
                if nb_anomalies > 0:
                    with st.expander("📋 Détails des anomalies détectées"):
                        st.dataframe(df[df['Anomaly']], use_container_width=True)
        
        # ========== PRÉDICTION RUL ==========
        st.markdown("#### 🔮 Prédiction du RUL (Remaining Useful Life)")
        
        if 'model_loaded' in st.session_state and st.session_state['model_loaded']:
            model = st.session_state['model']
            
            st.info("💡 Assurez-vous que vos données sont prétraitées de la même manière que lors de l'entraînement du modèle")
            
            if st.button("🚀 Lancer la prédiction RUL", type="primary"):
                try:
                    # Prédiction (adapter selon votre modèle)
                    # Exemple simplifié : prédire sur tout le dataset
                    predictions = model.predict(df[numeric_cols])
                    
                    # Ajouter les prédictions au DataFrame
                    df['RUL_Predicted'] = predictions
                    
                    st.success("✅ Prédictions effectuées avec succès !")
                    
                    # Affichage des résultats
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("📊 RUL Moyen", f"{predictions.mean():.2f}")
                        st.metric("📉 RUL Min", f"{predictions.min():.2f}")
                    
                    with col2:
                        st.metric("📈 RUL Max", f"{predictions.max():.2f}")
                        st.metric("📊 Écart-type", f"{predictions.std():.2f}")
                    
                    # Graphique des prédictions
                    fig = px.line(
                        df,
                        y='RUL_Predicted',
                        title="Évolution du RUL Prédit",
                        labels={'index': 'Index', 'RUL_Predicted': 'RUL (cycles)'}
                    )
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Téléchargement des résultats
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Télécharger les résultats (CSV)",
                        data=csv,
                        file_name="predictions_RUL.csv",
                        mime="text/csv"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Erreur lors de la prédiction : {str(e)}")
                    st.info("💡 Vérifiez que les colonnes du dataset correspondent aux features attendues par le modèle")
        else:
            st.warning("⚠️ Veuillez d'abord charger un modèle dans l'onglet 'Upload Modèle'")
        
        # ========== DÉTECTION D'ANOMALIES ==========
        st.markdown("---")
        st.markdown("#### 🚨 Détection d'Anomalies")
        
        if len(numeric_cols) > 0:
            anomaly_feature = st.selectbox(
                "Sélectionnez la variable pour détecter les anomalies",
                options=numeric_cols,
                key="anomaly_feature"
            )
            
            threshold = st.slider(
                "Définir le seuil (écart-type)",
                min_value=1.0,
                max_value=5.0,
                value=3.0,
                step=0.1
            )
            
            if st.button("🔍 Détecter les anomalies", type="primary"):
                # Calcul des anomalies basé sur l'écart-type
                mean = df[anomaly_feature].mean()
                std = df[anomaly_feature].std()
                
                df['Anomaly'] = (df[anomaly_feature] > mean + threshold * std) | \
                                (df[anomaly_feature] < mean - threshold * std)
                
                nb_anomalies = df['Anomaly'].sum()
                
                st.metric("🚨 Nombre d'anomalies détectées", nb_anomalies)
                
                # Visualisation
                fig = go.Figure()
                
                # Points normaux
                fig.add_trace(go.Scatter(
                    x=df[~df['Anomaly']].index,
                    y=df[~df['Anomaly']][anomaly_feature],
                    mode='markers',
                    name='Normal',
                    marker=dict(color='blue', size=5)
                ))
                
                # Points anomalies
                fig.add_trace(go.Scatter(
                    x=df[df['Anomaly']].index,
                    y=df[df['Anomaly']][anomaly_feature],
                    mode='markers',
                    name='Anomalie',
                    marker=dict(color='red', size=8, symbol='x')
                ))
                
                # Lignes de seuil
                fig.add_hline(y=mean + threshold * std, line_dash="dash", line_color="red", annotation_text="Seuil haut")
                fig.add_hline(y=mean - threshold * std, line_dash="dash", line_color="red", annotation_text="Seuil bas")
                
                fig.update_layout(
                    title=f"Détection d'anomalies - {anomaly_feature}",
                    xaxis_title="Index",
                    yaxis_title=anomaly_feature,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Afficher les anomalies
                if nb_anomalies > 0:
                    with st.expander("📋 Détails des anomalies détectées"):
                        st.dataframe(df[df['Anomaly']], use_container_width=True)
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
            "7 exercices avec correction automatique",
            "Visualisations Plotly interactives",
            "PDF, vidéos et datasets"
        ]
        
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


























































