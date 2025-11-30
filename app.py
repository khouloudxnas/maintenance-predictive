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


# THÉORIE
elif section == "📚 Théorie":
    st.title("📚 Théorie & Concepts")
    
    st.markdown("### Explorez les concepts clés de la maintenance prédictive")
    
    with st.expander("🎯 **Introduction à la Maintenance Prédictive** - Qu'est-ce que c'est ?", expanded=True):
        st.markdown("""
        #### Qu'est-ce que la maintenance prédictive ?
        
        La maintenance prédictive vise à **prévoir les défaillances** d'une machine avant qu'elles ne surviennent.
        
        **Avantages clés :**
        - ✅ Réduction des coûts de maintenance
        - ✅ Amélioration de la disponibilité des équipements
        - ✅ Augmentation de la sécurité des installations
        - ✅ Optimisation de la planification
        """)
        st.markdown("🔗 [En savoir plus sur Wikipedia](https://fr.wikipedia.org/wiki/Maintenance_prédictive)")
    
    with st.expander("🔄 **Types de maintenance** - Corrective, Préventive, Prédictive"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🔴 Corrective")
            st.write("Intervention **après panne**")
            st.write("⚠️ Coûteux et imprévisible")
        
        with col2:
            st.markdown("#### 🟡 Préventive")
            st.write("Planifiée selon un **calendrier**")
            st.write("📅 Régulière mais parfois inutile")
        
        with col3:
            st.markdown("#### 🟢 Prédictive")
            st.write("Basée sur l'**analyse des données**")
            st.write("📊 Optimale et économique")
        
        st.markdown("---")
        st.markdown("🔗 [Article sur les types de maintenance](https://www.maintenance.org/types-de-maintenance)")
    
    with st.expander("📡 **Capteurs et mesures** - Les technologies de surveillance"):
        st.markdown("#### Les principaux capteurs utilisés :")
        
        sensors_data = {
            "Capteur": ["🌊 Vibration", "🌡️ Température", "⚡ Courant électrique", "🔊 Acoustique"],
            "Détecte": ["Déséquilibres, usure des roulements", "Surchauffe, friction", "Anomalies moteurs", "Fissures, fuites"],
            "Criticité": ["Élevée", "Moyenne", "Élevée", "Moyenne"]
        }
        
        df_sensors = pd.DataFrame(sensors_data)
        st.dataframe(df_sensors, use_container_width=True)
    
    with st.expander("🔬 **Méthodes d'analyse** - Comment analyser les données ?"):
        st.markdown("""
        #### Approches principales :
        
        1. **📊 Analyse statistique** : Étude des tendances et patterns historiques
        2. **🤖 Machine Learning** : Détection automatique des anomalies
        3. **📈 Analyse spectrale** : Analyse fréquentielle des vibrations
        4. **🌐 IoT** : Collecte et traitement des données en temps réel
        """)
        st.markdown("🔗 [Tutoriel Machine Learning Maintenance](https://www.coursera.org/learn/predictive-maintenance)")
    
    with st.expander("📊 **Indicateurs clés (KPI)** - Mesurer la performance"):
        st.markdown("#### Les KPI essentiels en maintenance :")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **⏱️ MTBF** (Mean Time Between Failures)
            - Temps moyen entre pannes
            - Mesure la fiabilité
            """)
            
            st.markdown("""
            **🔧 MTTR** (Mean Time To Repair)
            - Temps moyen de réparation
            - Mesure l'efficacité de maintenance
            """)
        
        with col2:
            st.markdown("""
            **✅ Disponibilité**
            - Proportion de temps opérationnel
            - Objectif : > 95%
            """)
            
            st.markdown("""
            **💯 Fiabilité**
            - Probabilité de bon fonctionnement
            - Essentielle pour la planification
            """)
        
        st.markdown("🔗 [Guide complet sur les KPI Maintenance](https://www.maintenance.org/indicateurs-KPI)")


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




