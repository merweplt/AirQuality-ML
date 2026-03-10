import streamlit as st
import pandas as pd
from src.model import AirQualityModel
from src.database import DatabaseManager

# 1. Sayfa Ayarları
st.set_page_config(page_title="Hava Kalitesi AI", layout="wide")

# CSS - Harita yüksekliğini ve genel boşlukları kontrol edelim
st.markdown("""
    <style>
    .stApp { background-color: #f1f5f9; }
    h1 { color: #1e3a8a !important; font-size: 2rem !important; margin-bottom: 0px; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 12px; border-left: 5px solid #1e3a8a; }
    /* Harita kutusunu sınırlayalım */
    [data-testid="stMap"] { height: 250px !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Veri ve Model Hazırlığı
db = DatabaseManager("sqlite:///hava_kalitesi.db")
ai = AirQualityModel()
df = db.load_data("SELECT * FROM sensor_data")
df.columns = ["Sıcaklık (°C)", "Nem (%)", "PM10 Değeri"]
ai.train(df[["Sıcaklık (°C)", "Nem (%)"]], df["PM10 Değeri"])

# 3. Başlık
st.title("🌍 Hava Kalitesi Analiz Paneli")
st.write("---")

# 4. Üst Bölüm: Konum ve Küçük Harita
col_loc, col_map = st.columns([1.2, 1], gap="medium")

with col_loc:
    st.subheader("📍 Konum Ayarları")
    location = st.selectbox("Bölge:", ["İstanbul - Zeytinburnu (Kampüs)", "İstanbul - Üsküdar", "İstanbul - Beşiktaş"])
    st.info(f"İstasyon: {location}")

with col_map:
    # Haritayı daha küçük bir alan içinde gösteriyoruz
    map_data = pd.DataFrame({'lat': [41.0125], 'lon': [28.9112]}) 
    st.map(map_data, zoom=10, use_container_width=True)

st.write("---")

# 5. Ana Panel
col_input, col_graph = st.columns([1, 2], gap="large")

with col_input:
    st.subheader("🔍 Tahminleme")
    t_input = st.slider("Sıcaklık (°C)", 0, 45, 25)
    h_input = st.slider("Nem (%)", 10, 95, 50)
    
    pred = ai.predict([[t_input, h_input]])[0]
    st.metric(label="Tahmini PM10", value=f"{pred:.2f} µg/m³")
    
    if pred > 80: st.error("⚠️ Kirlilik: Yüksek")
    else: st.success("✅ Kalite: İyi")

with col_graph:
    tab1, tab2 = st.tabs(["📊 Başarı Grafiği", "📑 Veri Kayıtları"])
    with tab1:
        st.image("outputs/sonuc.png", use_container_width=True)
    with tab2:
        st.dataframe(df.tail(8), use_container_width=True)

st.caption("© 2026 Air Quality AI | Yazılım Mühendisliği Portfolyo")