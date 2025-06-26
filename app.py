# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 13:15:53 2025

@author: jahop
"""

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# Configuración inicial
st.set_page_config(
    page_title="¡Soy tu próximo Crack para RappiCard!",
    layout="wide",
    page_icon="💳"
)

# Header impactante
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🚀 ¡Hola RappiCard México!")
    st.subheader("Encontraste al **Crack** que buscas para tu equipo de Data/GenAI/Tech")
    
with col2:
    # Puedes reemplazar esto con tu foto o un logo
    st.image("logo.jpg", width=450, use_column_width="auto") 

# Línea divisoria
st.markdown("---")

# Sección de motivación
st.header("💡 ¿Por qué yo?")
motivation = st.expander("Ver mi motivación para unirme al equipo", expanded=True)
with motivation:
    st.write("""
    - 🔥 **Apasionado por los datos** y su transformación en decisiones estratégicas
    - � **Team player** con experiencia trabajando en equipos multidisciplinarios
    - 🤖 **Entusiasmado con GenAI** y sus aplicaciones en fintech
    - 📈 **Metric-driven** con enfoque en impacto empresarial
    - 🇲🇽 **Conectado con el mercado mexicano** y sus particularidades
    """)

# Sección de posiciones
st.header("👔 Posición de interés")
position = st.radio(
    "Para cuál posición aplico:",
    ("Senior Data Engineer", "Junior BI Analyst", "Junior Data Scientist (entry level)"),
    horizontal=True
)

# Mostrar skills específicos según posición
st.subheader(f"🛠️ Skills para {position}")

if position == "Senior Data Engineer":
    skills = {
        "Tecnologías": ["Python", "SQL", "Spark", "Airflow", "AWS/GCP", "Data Lakes"],
        "Experiencia": ["5+ años en DE", "Arquitecturas de datos", "ETL optimizados", "CI/CD"],
        "Soft Skills": ["Liderazgo técnico", "Mentoría", "Comunicación con stakeholders"]
    }
elif position == "Junior BI Analyst":
    skills = {
        "Tecnologías": ["SQL", "Tableau/PowerBI", "Excel", "Python básico"],
        "Experiencia": ["2+ años en análisis", "Dashboards interactivos", "KPI tracking"],
        "Soft Skills": ["Storytelling con datos", "Trabajo en equipo", "Curiosidad analítica"]
    }
else:  # Junior Data Scientist
    skills = {
        "Tecnologías": ["Python", "ML básico", "Pandas", "Sklearn", "Visualización"],
        "Experiencia": ["Proyectos de DS", "Feature engineering", "Modelos básicos"],
        "Soft Skills": ["Aprendizaje rápido", "Resolución problemas", "Creatividad técnica"]
    }

# Mostrar skills en tabs
tab1, tab2, tab3 = st.tabs(["Tecnologías", "Experiencia", "Soft Skills"])
with tab1:
    st.dataframe(pd.DataFrame(skills["Tecnologías"], columns=["Tecnologías"]), hide_index=True)
with tab2:
    st.dataframe(pd.DataFrame(skills["Experiencia"], columns=["Experiencia"]), hide_index=True)
with tab3:
    st.dataframe(pd.DataFrame(skills["Soft Skills"], columns=["Soft Skills"]), hide_index=True)

# Sección de "Wow factor" - algo que llame poderosamente la atención
st.markdown("---")
st.header("✨ Mi 'Crack Factor' para RappiCard")

wow_factor = st.selectbox(
    "Qué te gustaría conocer de mí que me hace único:",
    [
        "Selecciona una opción",
        "Proyecto del que estoy más orgulloso",
        "Mi enfoque para resolver problemas complejos",
        "Cómo mantengo mis skills actualizados",
        "Mi contribución única al equipo"
    ]
)

if wow_factor == "Proyecto del que estoy más orgulloso":
    st.success("""
    **🚀 Sistema de recomendación para tarjetas de crédito**  
    - Desarrollé un MVP que aumentó la aceptación de tarjetas en un 15%  
    - Stack: Python + LightFM + AWS Lambda  
    - Implementé AB testing para validar resultados  
    """)
elif wow_factor == "Mi enfoque para resolver problemas complejos":
    st.info("""
    **🧠 Framework de 4 pasos:**  
    1. Entender el impacto empresarial  
    2. Romper el problema en componentes manejables  
    3. Prototipado rápido con métricas claras  
    4. Iteración basada en feedback de stakeholders  
    """)
elif wow_factor == "Cómo mantengo mis skills actualizados":
    st.warning("""
    **📚 Ritual de aprendizaje constante:**  
    - 2 horas semanales dedicadas a experimentar con GenAI  
    - Suscripción a arXiv para papers de vanguardia  
    - Participación activa en hackathons de fintech  
    """)
elif wow_factor == "Mi contribución única al equipo":
    st.success("""
    **💡 Combinación única de habilidades:**  
    - Background técnico + comprensión de negocio financiero  
    - Capacidad de traducir requerimientos técnicos a lenguaje comercial  
    - Energía positiva y mentalidad de crecimiento  
    """)

# Sección de contacto
st.markdown("---")
st.header("📩 ¡Contáctame!")
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Tu nombre", key="nombre")
with col2:
    st.text_input("Tu email", key="email")
with col3:
    st.text_input("Tu LinkedIn", key="linkedin")

if st.button("🚀 Enviar mi aplicación"):
    st.balloons()
    st.success("¡Gracias! Tu aplicación ha sido enviada. RappiCard estará en contacto pronto.")

# Easter egg - muestra un mensaje secreto al hacer click
if st.button("🔍 Pssst... haz click aquí"):
    st.markdown("""
    <style>
    .secret {
        font-size: 24px;
        color: #FF4B4B;
        font-weight: bold;
        text-align: center;
        border: 2px dashed #FF4B4B;
        padding: 20px;
        margin-top: 20px;
        border-radius: 10px;
    }
    </style>
    <div class="secret">
    ⚡ ¡Soy exactamente el perfil que buscan!<br>
    Agendemos una llamada para demostrarlo 😉<br>
    +52 56 1056-4095 | jahoperi@gmail.com
    </div>
    """, unsafe_allow_html=True)