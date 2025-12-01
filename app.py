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
    st.markdown("### Suivez le parcours complet pour passer de 0% → expert en maintenance prédictive")
    st.markdown("Utilisez les expanders pour naviguer niveau par niveau. Chaque bloc contient explications, exemples et notions clés.")

    # Niveaux 0 & 1
    with st.expander("🟦 Niveau 0 — Comprendre (Intro)  & 🟩 Niveau 1 — Types de maintenance", expanded=True):
        st.markdown("## 🟦 Niveau 0 — Comprendre simplement : c’est quoi la maintenance prédictive ?")
        st.markdown("""
        La maintenance prédictive permet de **prévoir** qu’une machine va tomber en panne **avant** que cela arrive.
        
        ➤ Elle utilise : **capteurs, données, algorithmes**.  
        ➤ Objectif : éviter les pannes, économiser de l'argent, augmenter la sécurité.
        """)
        st.markdown("**Exemple simple :**")
        st.markdown("- Ta voiture fait un bruit inhabituel → tu vas chez le mécanicien.")
        st.markdown("- Une machine industrielle a des capteurs qui détectent ce bruit → un algorithme prévient les techniciens avant la panne.")
        st.info("Astuce : Pense toujours 'données → décision'.")

        st.markdown("---")
        st.markdown("## 🟩 Niveau 1 — Les 3 types de maintenance")
        st.markdown("**1️⃣ Corrective** : intervenir après la panne → coûte cher, arrête la production.")
        st.markdown("**2️⃣ Préventive** : entretien planifié → parfois inutile (basée sur calendrier).")
        st.markdown("**3️⃣ Prédictive** : basée sur l’analyse de données → meilleure stratégie moderne.")
        st.success("Pourquoi choisir la prédictive ? Réduction des coûts, optimisation des interventions, meilleure disponibilité.")

    # Niveaux 2 & 3
    with st.expander("🟨 Niveau 2 — Capteurs & données  & 🟧 Niveau 3 — Analyse des données", expanded=False):
        st.markdown("## 🟨 Niveau 2 — Capteurs & données")
        st.markdown("Les capteurs sont les « yeux » de la machine. Ils fournissent les mesures nécessaires pour détecter les anomalies.")
        st.markdown("### Capteurs courants :")
        st.markdown("- 🌊 **Vibration** → roulements, déséquilibre")
        st.markdown("- 🌡️ **Température** → surchauffe")
        st.markdown("- ⚡ **Courant électrique** → surcharge moteur")
        st.markdown("- 🔊 **Acoustique / Ultrasons** → fuites d’air, fissures")
        st.markdown("- 🧰 **Pression** → hydraulique / pneumatique")
        st.markdown("- 💧 **Humidité** → moteurs et transformateurs")
        st.markdown("### Notions importantes : fréquence d'échantillonnage, bruit, intervalle de mesure, qualité des données.")
        st.info("Bonnes pratiques : calibrer les capteurs, vérifier les données manquantes et filtrer le bruit.")

        st.markdown("---")
        st.markdown("## 🟧 Niveau 3 — Analyse des données (Data Analysis)")
        st.markdown("Pour exploiter les capteurs, on applique :")
        st.markdown("- **Statistiques** : moyenne, variance, tendance")
        st.markdown("- **Détection de pics** : identifier pannes imminentes")
        st.markdown("- **Visualisations** : histogrammes, spectres, courbes temporelles")
        st.markdown("- **Analyse des signatures vibratoires** : repérer l’usure de roulements, déséquilibres")
        st.info("Exercice : collecter 1000 échantillons vibration et tracer l'histogramme + FFT pour repérer fréquences anormales.")

    # Niveaux 4 & 5
    with st.expander("🟥 Niveau 4 — ML & IA  & 🟪 Niveau 5 — Modèles avancés (Deep Learning)", expanded=False):
        st.markdown("## 🟥 Niveau 4 — Le Machine Learning & l’IA en maintenance")
        st.markdown("Méthodes principales :")
        st.markdown("1️⃣ **Régression** → prédire une valeur (ex: température future)")
        st.markdown("2️⃣ **Classification** → déterminer l'état (normal / anomalie)")
        st.markdown("3️⃣ **Clustering** → détecter comportements anormaux sans étiquette")
        st.markdown("4️⃣ **Anomaly detection** → repérer pannes inconnues")
        st.markdown("### Workflow ML basique : collecte → nettoyage → features → split → entraînement → évaluation → déploiement")
        st.info("Start simple : modèles linéaires / arbres, puis évoluer vers modèles plus complexes si besoin.")

        st.markdown("---")
        st.markdown("## 🟪 Niveau 5 — Modèles avancés (Deep Learning)")
        st.markdown("Pour signaux complexes et séries temporelles :")
        st.markdown("- **CNN** : pour extraire motifs locaux (ex : spectrogrammes vibratoires)")
        st.markdown("- **LSTM / GRU** : pour dépendances temporelles sur séries longues")
        st.markdown("- **Auto-encoders** : pour détection d'anomalie non supervisée")
        st.markdown("Astuce : transformer signal en spectrogramme + utiliser CNN = très efficace pour vibrations complexes.")
        st.success("Rappel : commencer par baseline simple avant d'utiliser du deep learning coûteux en données et calcul.")

    # Niveaux 6 & 7
    with st.expander("🟫 Niveau 6 — Architecture IoT  & 🟦 Niveau 7 — Workflow usine réel", expanded=False):
        st.markdown("## 🟫 Niveau 6 — Architecture IoT")
        st.markdown("Composants d'un système complet :")
        st.markdown("- 📡 **Capteurs** → acquisition")
        st.markdown("- 🧠 **Edge computing** (Raspberry Pi, microcontrôleur) → prétraitement, filtrage, calcul léger")
        st.markdown("- ☁️ **Cloud** (AWS, Azure, GCP) → stockage, entraînement modèles, pipeline")
        st.markdown("- 📊 **Tableau de bord** (Power BI, Grafana, Streamlit) → visualisation & alerting")
        st.info("Design tip : faire du pré-traitement en edge réduit latence et coût réseau.")

        st.markdown("---")
        st.markdown("## 🟦 Niveau 7 — Workflow réel dans une usine")
        st.markdown("Étapes pratiques :")
        st.markdown("1. **Collecte des données** (synchronisation horodatage)")
        st.markdown("2. **Nettoyage** (gestion valeurs manquantes, outliers)")
        st.markdown("3. **Feature engineering** (RMS, crest factor, énergie spectrale…)")
        st.markdown("4. **Entraînement du modèle** (choix métriques : précision, recall, F1, AUC)")
        st.markdown("5. **Détection des anomalies** en temps réel")
        st.markdown("6. **Envoi d’alertes** (emails, SMS, systèmes de ticket)")
        st.markdown("7. **Planification de la maintenance** (ordres de travail optimisés)")
        st.markdown("8. **Suivi des KPI** et rétroaction pour améliorer le modèle")
        st.success("Important : intégrer le retour terrain (techniciens) pour améliorer la qualité des labels et la précision.")

    # Niveaux 8 & 9
    with st.expander("🟫 Niveau 8 — KPI essentiels  & 🟩 Niveau 9 — Cas pratiques", expanded=False):
        st.markdown("## 🟫 Niveau 8 — KPI essentiels")
        st.markdown("- **MTBF** : Mean Time Between Failures (temps moyen entre pannes)")
        st.markdown("- **MTTR** : Mean Time To Repair (temps moyen de réparation)")
        st.markdown("- **Disponibilité** : A = MTBF / (MTBF + MTTR)")
        st.markdown("- **Taux d’anomalies détectées**")
        st.markdown("- **Coût d’arrêt de production**")
        st.info("Suivre ces KPI permet d'évaluer l'impact économique de la maintenance prédictive.")

        st.markdown("---")
        st.markdown("## 🟩 Niveau 9 — Cas pratiques (idées de projets)")
        st.markdown("- Détection de défaillance d’un moteur (vibration + courant)")
        st.markdown("- Analyse vibratoire d’un roulement (FFT + features temporelles)")
        st.markdown("- Tracking de température d’un four industriel (détection dérive)")
        st.markdown("- Analyse acoustique de compresseur (classif. par spectrogramme)")
        st.markdown("- Modèle prédictif pour lignes d'assemblage (combinaison capteurs)")
        st.info("Conseil : pour chaque cas pratique, définir dataset, métrique d'évaluation, et seuil d'alerte opérationnel.")

    # Optionnel : bouton pour télécharger le plan complet en PDF (si tu veux l'ajouter plus tard)
    st.markdown("---")
    st.markdown("**Besoin d'ajouts ?** Si tu veux, je peux :")
    st.markdown("- transformer chaque niveau en une leçon avec mini-exercices interactifs")
    st.markdown("- ajouter un quiz par niveau et un suivi de progression")
    st.markdown("- convertir ce parcours en PDF téléchargeable")

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






