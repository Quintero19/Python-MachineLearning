import streamlit as st
import pandas as pd
import pydeck as pdk
st.set_page_config(
    page_title="Fórmula 1 Dashboard",
    page_icon="🏁",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    [data-testid="stApp"] {
        background-image: url("https://wallpapers.com/images/hd/formula-1-race-car-4k-laptop-car-9g4sq4up0z6ssc3p.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.85);
    }

    h1, h2, h3, .st-bb {
        color: #f5f5f5;
    }

    .stSelectbox > div {
        border: 2px solid red;
        border-radius: 8px;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .css-1d391kg {
        font-size: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title('🏎️ Menú F1')
menu = st.sidebar.selectbox('Ir a:', ['Inicio', 'Pilotos', 'Escuderías', 'Estadísticas', 'Circuitos'])

if menu == 'Inicio':
    st.title('🏁 Bienvenido al Mundo de la Fórmula 1')
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg", width=200)
    st.markdown("""
    **La Fórmula 1** es el máximo nivel del automovilismo mundial. Conoce a los pilotos más rápidos, las escuderías más legendarias y las pistas más desafiantes del planeta.

    Usa el menú lateral para navegar por la información.
    """)
    st.video("https://youtu.be/3BEHQEiDgW0?si=CPdZFEeAf3azchjb")

elif menu == 'Pilotos':
    st.header('👨‍✈️ Pilotos Destacados de 2024')

    pilotos = [
        {
            "nombre": "Max Verstappen",
            "escuderia": "Red Bull",
            "pais": "Países Bajos",
            "titulos": 3,
            "foto": "https://img.redbull.com/images/c_crop,x_3162,y_0,h_5464,w_3279/c_fill,w_400,h_660/q_auto:low,f_auto/redbullcom/2022/5/5/sor22gddafi4ribmje9p/max-verstappen-header"
        },
        {
            "nombre": "Lewis Hamilton",
            "escuderia": "Mercedes",
            "pais": "Reino Unido",
            "titulos": 7,
            "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_8xsYHwn7ceW23mTVmzLqqxAyOy1NL90Jnw&s"
        },
        {
            "nombre": "Charles Leclerc",
            "escuderia": "Ferrari",
            "pais": "Mónaco",
            "titulos": 0,
            "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0SUBi87al4nvRbXuP5RYGQkRAOz9MRYvCZg&s"
        },
        {
            "nombre": "Fernando Alonso",
            "escuderia": "Aston Martin",
            "pais": "España",
            "titulos": 2,
            "foto": "https://media.formula1.com/image/upload/f_auto/q_auto/v1741268869/content/dam/fom-website/drivers/2025Drivers/alonso.png"
        }
    ]

    for piloto in pilotos:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(piloto["foto"], width=120)
        with col2:
            st.subheader(piloto["nombre"])
            st.markdown(f"**Escudería:** {piloto['escuderia']}")
            st.markdown(f"**País:** {piloto['pais']}")
            st.markdown(f"**Títulos:** {piloto['titulos']}")
        st.markdown("---")

elif menu == 'Escuderías':
    st.header("🏎️ Estadísticas por Escudería")
    escuderias_data = {
        "Escudería": ["Red Bull", "Ferrari", "Mercedes", "Aston Martin"],
        "Victorias 2024": [3, 1, 0, 0],
        "Pilotos Principales": ["Verstappen, Pérez", "Leclerc, Sainz", "Hamilton, Russell", "Alonso, Stroll"]
    }
    df_esc = pd.DataFrame(escuderias_data)
    st.dataframe(df_esc)
    st.bar_chart(df_esc.set_index("Escudería")["Victorias 2024"])

elif menu == 'Estadísticas':
    st.header('📊 Estadísticas Temporada 2024')
    try:
        df = pd.read_csv("f1_2024_resultados.csv")
        st.subheader("🏆 Resultados recientes")
        st.dataframe(df)
        st.subheader("⏱️ Vueltas más rápidas por carrera")
        st.bar_chart(df.set_index("Carrera")["Vuelta_Rapida_s"])
    except FileNotFoundError:
        st.error("Archivo 'f1_2024_resultados.csv' no encontrado.")

elif menu == 'Circuitos':
    st.header('🌍 Circuitos del Calendario F1 2024')

    # Datos principales de los circuitos 2024
    circuitos = [
        {"Circuito": "Bahrain Intl", "GP": "Baréin", "lat": 26.0325, "lon": 50.5106, "País": "Bahréin"},
        {"Circuito": "Jeddah Corniche", "GP": "Arabia Saudita", "lat": 21.6339, "lon": 39.0036, "País": "Arabia Saudita"},
        {"Circuito": "Albert Park", "GP": "Australia", "lat": -37.8497, "lon": 144.9689, "País": "Australia"},
        {"Circuito": "Suzuka", "GP": "Japón", "lat": 34.8431, "lon": 136.5400, "País": "Japón"},
        {"Circuito": "Shanghai Intl", "GP": "China", "lat": 31.3380, "lon": 121.2368, "País": "China"},
        {"Circuito": "Miami Int'l Autodrome", "GP": "Miami", "lat": 25.9585, "lon": -80.2381, "País": "EE.UU."},
        {"Circuito": "Imola", "GP": "Emilia‑Romagna", "lat": 44.3427, "lon": 10.9928, "País": "Italia"},
        {"Circuito": "Monaco", "GP": "Mónaco", "lat": 43.7347, "lon": 7.4246, "País": "Mónaco"},
        {"Circuito": "Gilles‑Villeneuve", "GP": "Canadá", "lat": 45.5042, "lon": -73.5292, "País": "Canadá"},
        {"Circuito": "Barcelona‑Catalunya", "GP": "España", "lat": 41.3879, "lon": 2.0840, "País": "España"},
        {"Circuito": "Red Bull Ring", "GP": "Austria", "lat": 47.2153, "lon": 14.7648, "País": "Austria"},
        {"Circuito": "Silverstone", "GP": "Gran Bretaña", "lat": 52.0700, "lon": -1.0140, "País": "Reino Unido"},
        {"Circuito": "Hungaroring", "GP": "Hungría", "lat": 47.5782, "lon": 19.2502, "País": "Hungría"},
        {"Circuito": "Spa‑Francorchamps", "GP": "Bélgica", "lat": 50.4372, "lon": 5.9714, "País": "Bélgica"},
        {"Circuito": "Zandvoort", "GP": "Países Bajos", "lat": 52.3880, "lon": 4.5400, "País": "Países Bajos"},
        {"Circuito": "Monza", "GP": "Italia", "lat": 45.6190, "lon": 9.2810, "País": "Italia"},
        {"Circuito": "Baku City", "GP": "Azerbaiyán", "lat": 40.3725, "lon": 49.8539, "País": "Azerbaiyán"},
        {"Circuito": "Marina Bay", "GP": "Singapur", "lat": 1.2914, "lon": 103.8545, "País": "Singapur"},
        {"Circuito": "COTA", "GP": "Estados Unidos", "lat": 30.1328, "lon": -97.6410, "País": "EE.UU."},
        {"Circuito": "Hermanos Rodríguez", "GP": "México", "lat": 19.4040, "lon": -99.0948, "País": "México"},
        {"Circuito": "Interlagos", "GP": "Brasil", "lat": -23.7036, "lon": -46.6997, "País": "Brasil"},
        {"Circuito": "Las Vegas Strip", "GP": "Las Vegas", "lat": 36.0900, "lon": -115.1830, "País": "EE.UU."},
        {"Circuito": "Lusail Intl", "GP": "Qatar", "lat": 25.2582, "lon": 51.6144, "País": "Qatar"},
        {"Circuito": "Yas Marina", "GP": "Abu Dhabi", "lat": 24.4677, "lon": 54.6031, "País": "EAU"}
    ]

    df_map = pd.DataFrame(circuitos)

    tooltip = {
        "html": "<b>{GP}</b><br/>{Circuito}<br/>{País}",
        "style": {"backgroundColor": "steelblue", "color": "white", "fontSize": "12px", "padding": "5px"}
    }

    st.pydeck_chart(pdk.Deck(
        map_style="dark",
        initial_view_state=pdk.ViewState(
            latitude=20, longitude=0, zoom=1.5, pitch=30
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                df_map,
                get_position=["lon", "lat"],
                get_color=[255, 100, 100],
                get_radius=200000,
                pickable=True
            )
        ],
        tooltip=tooltip
    ))

    st.markdown("🔎 *Pasa el cursor sobre un punto para ver el circuito y país.*")
