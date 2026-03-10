import pandas as pd
import matplotlib.pyplot as plt
from database import DatabaseManager
from model import AirQualityModel
import os

def main():
    # Kendi PostgreSQL bilgilerini buraya yaz:
    # PostgreSQL yerine bunu yapıştır, şifre sormaz:
    DB_URL = "sqlite:///hava_kalitesi.db"
    db = DatabaseManager(DB_URL)
    ai = AirQualityModel()

    data = {
        'temp': [15, 18, 20, 22, 25, 28, 30, 32, 35, 12, 10, 8],
        'humidity': [30, 35, 40, 45, 50, 55, 60, 65, 70, 25, 20, 15],
        'pm10': [20, 25, 30, 45, 60, 75, 90, 105, 120, 15, 12, 10]
    }
    df = pd.DataFrame(data)

    try:
        db.save_data(df, 'sensor_data')
        df_from_db = db.load_data("SELECT * FROM sensor_data")
        
        X = df_from_db[['temp', 'humidity']]
        y = df_from_db['pm10']
        mse = ai.train(X, y)
        print(f"✅ Başarılı! Hata Payı (MSE): {mse:.2f}")

        plt.scatter(df_from_db['temp'], df_from_db['pm10'], label='Veri')
        plt.plot(df_from_db['temp'], ai.predict(X), color='red', label='Tahmin')
        plt.savefig('outputs/sonuc.png')
        print("📊 Grafik 'outputs/sonuc.png' konumuna kaydedildi.")

    except Exception as e:
        print(f"❌ Hata: {e}")

if __name__ == "__main__":
    main()