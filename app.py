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

elif section == "📚 Théorie":
    st.title("📚 Formation Complète : De Débutant à Expert")
    
    st.markdown("""
    ### 🎓 Parcours d'apprentissage progressif
    Suivez ce parcours étape par étape pour maîtriser la maintenance prédictive
    """)
    
    # ============ NIVEAU 1: DÉBUTANT ============
    st.markdown("---")
    st.markdown("## 🟢 NIVEAU 1 : Les Fondamentaux")
    
    with st.expander("📖 **Chapitre 1.1 : Qu'est-ce qu'une panne ?**", expanded=True):
        st.markdown("""
        #### 🔧 Comprendre les pannes industrielles
        
        Une **panne** est l'arrêt imprévu d'une machine qui l'empêche de fonctionner correctement.
        
        **Exemple concret :** Imaginez une voiture
        - ⚠️ **Panne soudaine** : Le moteur s'arrête sans prévenir sur l'autoroute
        - 🔴 **Conséquences** : Danger, coûts de dépannage, retard
        - 💡 **Et si on avait pu le prévoir ?** C'est là qu'intervient la maintenance prédictive !
        
        #### Types de pannes industrielles :
        
        | Type de panne | Description | Exemple | Coût moyen |
        |---------------|-------------|---------|------------|
        | 🔴 **Catastrophique** | Arrêt complet et brutal | Rupture d'arbre moteur | 50 000€ - 500 000€ |
        | 🟡 **Progressive** | Dégradation lente | Usure de roulement | 5 000€ - 50 000€ |
        | 🟠 **Intermittente** | Défaut par moments | Court-circuit électrique | 1 000€ - 20 000€ |
        | 🟢 **Mineure** | Fonctionne en mode dégradé | Fuite d'huile légère | 500€ - 5 000€ |
        
        **💰 Impact économique d'une panne non planifiée :**
        - Coût de réparation d'urgence : **×3 à ×5** plus cher
        - Perte de production : **10 000€ à 100 000€ par heure** (selon l'industrie)
        - Impact sur les livraisons clients : **Pénalités contractuelles**
        """)
        
        st.info("🎯 **Point clé :** Une panne coûte 3 à 5 fois plus cher qu'une intervention planifiée !")
    
    with st.expander("📖 **Chapitre 1.2 : Les 3 stratégies de maintenance**"):
        st.markdown("""
        #### Comment gérer les pannes ? 3 approches possibles
        """)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 🔴 Maintenance CORRECTIVE
            **"On répare quand ça casse"**
            
            **Principe :**
            - Attendre la panne
            - Réparer en urgence
            
            **Avantages :**
            - ✅ Pas de planification nécessaire
            - ✅ Utilisation maximale des pièces
            
            **Inconvénients :**
            - ❌ Pannes imprévisibles
            - ❌ Coûts très élevés
            - ❌ Risques de sécurité
            - ❌ Arrêts de production
            
            **Coût annuel :** 100 000€
            **Disponibilité :** 75%
            
            🏭 **Utilisé pour :** Équipements non critiques (ventilateur de bureau)
            """)
        
        with col2:
            st.markdown("""
            ### 🟡 Maintenance PRÉVENTIVE
            **"On change selon le calendrier"**
            
            **Principe :**
            - Interventions programmées
            - Remplacement périodique
            
            **Avantages :**
            - ✅ Pannes réduites
            - ✅ Planification possible
            - ✅ Meilleure sécurité
            
            **Inconvénients :**
            - ❌ Changements parfois inutiles
            - ❌ Coût des pièces neuves
            - ❌ Arrêts planifiés fréquents
            
            **Coût annuel :** 70 000€
            **Disponibilité :** 85%
            
            🏭 **Utilisé pour :** Équipements standards (pompes, compresseurs)
            """)
        
        with col3:
            st.markdown("""
            ### 🟢 Maintenance PRÉDICTIVE
            **"On intervient au bon moment"**
            
            **Principe :**
            - Surveillance continue
            - Intervention basée sur l'état réel
            
            **Avantages :**
            - ✅ Interventions optimales
            - ✅ Réduction des coûts
            - ✅ Disponibilité maximale
            - ✅ Planification précise
            
            **Inconvénients :**
            - ⚠️ Investissement initial
            - ⚠️ Compétences requises
            
            **Coût annuel :** 40 000€
            **Disponibilité :** 95%+
            
            🏭 **Utilisé pour :** Équipements critiques (turbines, robots)
            """)
        
        st.markdown("---")
        st.markdown("""
        #### 📊 Comparaison chiffrée sur 1 machine pendant 5 ans
        
        | Critère | Corrective | Préventive | Prédictive |
        |---------|-----------|-----------|------------|
        | **Coût total 5 ans** | 500 000€ | 350 000€ | 250 000€ |
        | **Nombre de pannes** | 25 | 8 | 3 |
        | **Temps d'arrêt** | 500h | 200h | 50h |
        | **Disponibilité** | 75% | 85% | 95% |
        | **ROI** | - | 30% | 50% |
        
        💡 **Conclusion :** La maintenance prédictive permet d'économiser **250 000€ sur 5 ans** !
        """)
    
    with st.expander("📖 **Chapitre 1.3 : Principe de la maintenance prédictive**"):
        st.markdown("""
        #### 🎯 Comment ça marche concrètement ?
        
        La maintenance prédictive repose sur **4 étapes simples** :
        
        ```
        1. 📡 MESURER           →  2. 📊 ANALYSER
           ↑                                    ↓
        4. 🔧 INTERVENIR      ←  3. 🚨 ALERTER
        ```
        
        #### Exemple concret : Un moteur électrique
        
        **🏭 Situation :** Moteur critique d'une chaîne de production
        
        **1️⃣ MESURER (Capteurs installés)**
        - 🌡️ Température : 65°C (normale : 60°C ± 5°C)
        - 🌊 Vibration : 3.2 mm/s (normale : < 2.8 mm/s)
        - ⚡ Courant : 42A (normal : 38A ± 2A)
        - 🔊 Bruit : 78 dB (normal : < 75 dB)
        
        **2️⃣ ANALYSER (Intelligence Artificielle)**
        ```
        Algorithme détecte :
        - ⚠️ Vibrations anormales : +14% en 2 semaines
        - ⚠️ Température en hausse : +5°C en 1 mois
        - ⚠️ Consommation électrique : +10%
        
        → Diagnostic IA : Usure probable du roulement avant
        → Probabilité de panne : 85% dans 15-20 jours
        ```
        
        **3️⃣ ALERTER (Notification automatique)**
        - 📧 Email au responsable maintenance
        - 📱 SMS si criticité élevée
        - 📋 Ticket créé automatiquement
        - 📅 Fenêtre d'intervention suggérée : 12-18 jours
        
        **4️⃣ INTERVENIR (Action planifiée)**
        - 🗓️ Intervention planifiée le jour 16 (pendant arrêt production)
        - 🛠️ Pièces commandées à l'avance (roulement : 350€)
        - ⏱️ Durée d'intervention : 2h (vs 12h en panne d'urgence)
        - 💰 Coût total : 800€ (vs 8 000€ en panne)
        
        #### 💡 Résultat :
        - ✅ Panne évitée
        - ✅ Production non impactée
        - ✅ Économie : 7 200€
        - ✅ Sécurité préservée
        """)
    
    # ============ NIVEAU 2: INTERMÉDIAIRE ============
    st.markdown("---")
    st.markdown("## 🟡 NIVEAU 2 : Technologies et Capteurs")
    
    with st.expander("📖 **Chapitre 2.1 : Les capteurs - Les yeux de vos machines**"):
        st.markdown("""
        #### 🔬 Comment surveiller une machine ?
        
        Une machine industrielle émet des **signaux** qui révèlent son état de santé.
        Les capteurs sont comme des **médecins** qui examinent le patient en continu.
        
        ---
        
        ### 🌊 Capteur de VIBRATION
        **Ce qu'il mesure :** Les oscillations et mouvements de la machine
        
        **Pourquoi c'est important ?**
        - Une machine en bon état vibre de façon régulière et prévisible
        - Une anomalie (usure, déséquilibre) crée des vibrations inhabituelles
        
        **Défauts détectés :**
        - 🔧 Roulements usés (90% de fiabilité de détection)
        - ⚖️ Déséquilibre du rotor
        - 🔩 Desserrage de fixations
        - ⚙️ Défaut d'alignement
        - 🦷 Usure d'engrenages
        
        **Mesures :**
        - Accélération (m/s²)
        - Vélocité (mm/s) ← **Plus utilisé**
        - Déplacement (μm)
        
        **Exemple concret :**
        ```
        Roulement sain     : 1.5 mm/s
        Usure légère       : 2.8 mm/s → ⚠️ Surveiller
        Usure avancée      : 4.5 mm/s → 🚨 Planifier intervention
        Défaillance proche : 7.2 mm/s → 🔴 Urgent !
        ```
        
        **Prix :** 200€ - 2 000€ selon la précision
        
        ---
        
        ### 🌡️ Capteur de TEMPÉRATURE
        **Ce qu'il mesure :** La chaleur émise par la machine
        
        **Pourquoi c'est important ?**
        - L'usure et la friction créent de la chaleur excessive
        - Une surchauffe indique un problème de lubrification ou de charge
        
        **Défauts détectés :**
        - 🛢️ Manque de lubrification
        - 🔥 Friction excessive
        - ⚡ Surcharge électrique
        - ❄️ Problème de refroidissement
        
        **Types de capteurs :**
        - **Thermocouple** : Contact direct, précis (±0.5°C)
        - **Infrarouge** : Sans contact, rapide
        - **RTD** : Très haute précision (±0.1°C)
        
        **Exemple concret :**
        ```
        Moteur électrique :
        Température normale  : 60°C ± 5°C
        Échauffement léger   : 70°C → ⚠️ Vérifier lubrification
        Surchauffe           : 85°C → 🚨 Arrêt requis
        Critique             : 95°C → 🔴 Risque d'incendie
        ```
        
        **Prix :** 20€ - 500€
        
        ---
        
        ### ⚡ Capteur de COURANT électrique
        **Ce qu'il mesure :** La consommation électrique des moteurs
        
        **Pourquoi c'est important ?**
        - Un moteur qui force consomme plus
        - Les anomalies électriques précèdent souvent les pannes mécaniques
        
        **Défauts détectés :**
        - 🔌 Court-circuit
        - 🔋 Surcharge mécanique
        - ⚙️ Déséquilibre des phases
        - 🔄 Défaut de roulement (détection précoce)
        
        **Mesures :**
        - Intensité (Ampères)
        - Tension (Volts)
        - Puissance (Watts)
        - Facteur de puissance
        
        **Exemple concret :**
        ```
        Pompe industrielle (moteur 15 kW) :
        Courant nominal      : 28A
        Variation normale    : ±2A
        Pompe encrassée      : 32A → ⚠️ Maintenance préventive
        Roulement défectueux : 35A avec pics → 🚨 Intervention
        Blocage imminent     : 42A → 🔴 Arrêt immédiat
        ```
        
        **Prix :** 100€ - 1 000€
        
        ---
        
        ### 🔊 Capteur ACOUSTIQUE (Ultrasons)
        **Ce qu'il mesure :** Les sons et ultrasons émis par la machine
        
        **Pourquoi c'est important ?**
        - Certains défauts créent des bruits avant d'être visibles
        - Les ultrasons détectent des fuites invisibles
        
        **Défauts détectés :**
        - 💨 Fuites d'air comprimé
        - 💧 Fuites de fluides
        - ⚡ Décharges électriques (effet couronne)
        - 🔩 Fissures naissantes
        
        **Exemple concret :**
        ```
        Circuit d'air comprimé :
        Niveau normal    : 35 dB
        Petite fuite     : 45 dB → ⚠️ Perte d'énergie 500€/an
        Fuite importante : 60 dB → 🚨 Perte 5 000€/an
        Rupture proche   : 75 dB → 🔴 Arrêt système
        ```
        
        **Prix :** 300€ - 3 000€
        
        ---
        
        ### 🎯 Tableau récapitulatif : Quel capteur pour quel problème ?
        
        | Problème à détecter | Capteur prioritaire | Capteur secondaire | Délai de prévision |
        |---------------------|--------------------|--------------------|-------------------|
        | Usure de roulement | 🌊 Vibration | 🌡️ Température | 2-8 semaines |
        | Problème de lubrification | 🌡️ Température | 🌊 Vibration | 1-4 semaines |
        | Surcharge mécanique | ⚡ Courant | 🌊 Vibration | 3-10 jours |
        | Déséquilibre rotor | 🌊 Vibration | ⚡ Courant | 2-6 semaines |
        | Fuite d'air | 🔊 Acoustique | - | Immédiat |
        | Défaut électrique | ⚡ Courant | 🌡️ Température | 1-3 semaines |
        
        ---
        
        ### 💰 Coût d'un système de surveillance complet
        
        **Pour 1 machine critique :**
        - Capteurs (×4 types) : 1 500€
        - Installation : 800€
        - Passerelle IoT : 600€
        - Logiciel (abonnement/an) : 1 200€
        - **Total 1ère année : 4 100€**
        - **Années suivantes : 1 200€/an**
        
        **ROI moyen : 6-12 mois** (via économies sur pannes évitées)
        """)
    
    with st.expander("📖 **Chapitre 2.2 : L'IoT Industriel - Connecter vos machines**"):
        st.markdown("""
        #### 🌐 Qu'est-ce que l'IoT Industriel (IIoT) ?
        
        **IoT = Internet of Things = Internet des Objets**
        **IIoT = Industrial IoT = Machines industrielles connectées à Internet**
        
        ---
        
        ### 🔄 Le parcours de la donnée : Du capteur au décideur
        
        ```
        MACHINE                 TRANSMISSION             ANALYSE                 ACTION
        ───────                ─────────────            ────────               ───────
        
        🏭 Moteur              🛰️ Réseau               ☁️ Cloud                👨‍💼 Décision
           │                      │                       │                       │
           ├─ 🌊 Vibrations       │                       │                       │
           ├─ 🌡️ Température   ──┤ WiFi/4G/LoRa      ─→ 🤖 IA Analyse       ─→ 📧 Email
           ├─ ⚡ Courant          │                       │                       📱 SMS
           └─ 🔊 Bruit            │                       ├─ Détection anomalie  🔧 Planification
                                  │                       ├─ Prédiction panne
                                  └─ Passerelle IoT      └─ Calcul durée vie
        ```
        
        ---
        
        ### 📡 Technologies de transmission
        
        | Technologie | Portée | Débit | Coût | Usage industriel |
        |-------------|--------|-------|------|------------------|
        | **WiFi** | 50m | ⚡⚡⚡ Élevé | €€ | Ateliers, bureaux |
        | **4G/5G** | Illimité | ⚡⚡⚡ Élevé | €€€ | Sites distants, mobilité |
        | **LoRaWAN** | 10km | ⚡ Faible | € | Capteurs batteries, extérieur |
        | **Ethernet** | 100m | ⚡⚡⚡ Très élevé | €€ | Machines fixes, fiabilité max |
        | **ModBus** | 1km | ⚡⚡ Moyen | € | Standard industriel |
        
        ---
        
        ### 🏗️ Architecture d'un système IIoT
        
        **Niveau 1 : CAPTEURS** (Terrain)
        - Collecte des données brutes
        - Fréquence : 1 à 1000 mesures/seconde
        
        **Niveau 2 : PASSERELLE IoT** (Edge Computing)
        - Prétraitement des données
        - Filtrage et agrégation
        - Premier niveau d'alerte
        - Stockage local temporaire
        
        **Niveau 3 : CLOUD** (Serveurs distants)
        - Stockage massif de données
        - Calculs complexes d'IA
        - Tableaux de bord
        - Historiques longue durée
        
        **Niveau 4 : UTILISATEURS**
        - 📱 Application mobile
        - 💻 Dashboard web
        - 📊 Rapports automatiques
        - 🔔 Alertes personnalisées
        
        ---
        
        ### 📊 Flux de données en temps réel
        
        **Exemple : 10 machines surveillées**
        
        ```
        Par seconde :
        - 10 machines × 4 capteurs = 40 mesures/seconde
        - 40 mesures × 60 secondes = 2 400 mesures/minute
        - 2 400 × 60 minutes = 144 000 mesures/heure
        - 144 000 × 24 heures = 3,5 millions mesures/jour
        
        Stockage :
        - 1 mesure ≈ 50 octets
        - 3,5 millions × 50 octets = 175 Mo/jour
        - 175 Mo × 365 jours = 64 Go/an
        ```
        
        💡 **Cloud nécessaire pour gérer ces volumes !**
        
        ---
        
        ### 🔒 Sécurité IIoT : Points essentiels
        
        #### Risques :
        - 🚨 Cyberattaques (piratage de machines)
        - 🔓 Vol de données de production
        - 💥 Sabotage industriel
        
        #### Protections :
        - 🔐 **Chiffrement** : Données cryptées end-to-end
        - 🛡️ **Firewall industriel** : Isolation réseau OT/IT
        - 🔑 **Authentification** : Accès par certificats
        - 📝 **Traçabilité** : Logs de toutes les actions
        - 🔄 **Mises à jour** : Patches de sécurité réguliers
        
        ---
        
        ### 💰 Coûts d'une infrastructure IIoT
        
        **Pour 20 machines :**
        
        | Composant | Prix unitaire | Quantité | Total |
        |-----------|---------------|----------|-------|
        | Capteurs multi-paramètres | 800€ | 20 | 16 000€ |
        | Passerelles IoT | 1 200€ | 4 | 4 800€ |
        | Installation | 500€ | 20 | 10 000€ |
        | Logiciel Cloud (an) | 150€/machine | 20 | 3 000€/an |
        | **TOTAL initial** | | | **30 800€** |
        | **Coût annuel** | | | **3 000€** |
        
        **ROI :**
        - Réduction pannes : -40% → **Économie : 50 000€/an**
        - Retour sur investissement : **< 8 mois**
        """)
    
    # ============ NIVEAU 3: AVANCÉ ============
    st.markdown("---")
    st.markdown("## 🔴 NIVEAU 3 : Intelligence Artificielle et Analyse")
    
    with st.expander("📖 **Chapitre 3.1 : Machine Learning pour la maintenance - Les algorithmes**"):
        st.markdown("""
        #### 🤖 Comment l'IA détecte les anomalies ?
        
        Le Machine Learning permet à un ordinateur **d'apprendre tout seul** à reconnaître les pannes.
        
        ---
        
        ### 📚 Les 3 types d'apprentissage
        
        #### 1️⃣ APPRENTISSAGE SUPERVISÉ
        **Principe :** On montre des exemples à l'IA avec les réponses
        
        **Exemple :**
        ```
        Enseignement à l'IA :
        
        Exemple 1: Vibration=2mm/s, Temp=65°C → Machine SAINE ✅
        Exemple 2: Vibration=5mm/s, Temp=85°C → Machine DÉFAILLANTE ❌
        Exemple 3: Vibration=3mm/s, Temp=70°C → Machine ATTENTION ⚠️
        ... (des milliers d'exemples)
        
        Après apprentissage, l'IA peut prédire :
        Nouvelle mesure: Vibration=4.5mm/s, Temp=82°C
        → Prédiction IA: Machine DÉFAILLANTE à 87% ❌
        ```
        
        **Algorithmes utilisés :**
        - 🌳 **Random Forest** (Forêt aléatoire)
          - Précision : 85-92%
          - Temps de calcul : Rapide
          - Idéal pour : Classification de défauts
          
        - 🧠 **Neural Networks** (Réseaux de neurones)
          - Précision : 90-97%
          - Temps de calcul : Lent
          - Idéal pour : Patterns complexes
          
        - 📐 **SVM** (Support Vector Machine)
          - Précision : 82-89%
          - Temps de calcul : Moyen
          - Idéal pour : Petits datasets
        
        ---
        
        #### 2️⃣ APPRENTISSAGE NON SUPERVISÉ
        **Principe :** L'IA trouve elle-même les anomalies sans exemples
        
        **Exemple :**
        ```
        L'IA analyse 1 an de données normales:
        - Vibration moyenne : 2.2mm/s ± 0.4
        - Température moyenne : 63°C ± 3
        
        Un jour, l'IA détecte :
        - Vibration : 4.8mm/s → +118% de la normale ! 🚨
        - Température : 78°C → +24% de la normale ! 🚨
        
        → ANOMALIE détectée automatiquement
        ```
        
        **Algorithmes utilisés :**
        - 📊 **Isolation Forest**
          - Détecte les points aberrants
          - Fiabilité : 80-88%
          
        - 🎯 **K-Means Clustering**
          - Regroupe les comportements similaires
          - Détecte ce qui sort des groupes
          
        - 🔍 **Autoencoders**
          - Réseau de neurones spécialisé
          - Apprend la "normalité"
          - Précision : 88-94%
        
        ---
        
        #### 3️⃣ DEEP LEARNING (Apprentissage profond)
        **Principe :** Réseaux de neurones très complexes, imitent le cerveau humain
        
        **Avantages :**
        - 🎯 Précision exceptionnelle : 95-99%
        - 🔮 Détecte des patterns invisibles à l'œil humain
        - 📈 S'améliore avec plus de données
        
        **Inconvénients :**
        - 💻 Très gourmand en calcul (GPU nécessaire)
        - 📚 Besoin de milliers d'exemples
        - ⏱️ Apprentissage long (heures à jours)
        
        **Architectures populaires :**
        - **LSTM** : Pour données temporelles (vibrations dans le temps)
        - **CNN** : Pour images (thermographie infrarouge)
        - **Transformers** : Pour patterns complexes multi-capteurs
        
        ---
        
        ### 📊 Comparaison pratique des algorithmes
        
        | Algorithme | Précision | Données nécessaires | Temps calcul | Coût serveur | Cas d'usage |
        |------------|-----------|---------------------|--------------|--------------|-------------|
        | **Random Forest** | ⭐⭐⭐⭐ 88% | 1 000+ exemples | ⚡ Rapide | € | PME, débutants |
        | **SVM** | ⭐⭐⭐ 85% | 500+ exemples | ⚡⚡ Moyen | € | Classification binaire |
        | **Isolation Forest** | ⭐⭐⭐ 83% | 500+ exemples | ⚡ Rapide | € | Détection anomalies |
        | **Neural Networks** | ⭐⭐⭐⭐⭐ 94% | 5 000+ exemples | ⚡⚡⚡ Lent | €€ | Patterns complexes |
        | **LSTM** | ⭐⭐⭐⭐⭐ 96% | 10 000+ exemples | ⚡⚡⚡ Très lent | €€€ | Séries temporelles |
        
        ---
        
        ### 🔬 Exemple concret : Prédiction de panne de roulement
        
        **Dataset :**
        - 1 an de surveillance
        - 3 roulements tombés en panne (avec données avant-panne)
        - 50 roulements sains
        - 4 capteurs × 10 mesures/min = 2,1 millions de mesures
        
        **Étapes de l'IA :**
        
        ```
        1. PRÉPARATION DES DONNÉES (1 semaine)
           - Nettoyage (suppression valeurs aberrantes)
           - Normalisation (mise à l'échelle 0-1)
           - Feature engineering (calcul de moyennes, écarts-types)
        
        2. APPRENTISSAGE (2 jours sur GPU)
           - Random Forest : 10 000 arbres

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

