# 🌍 Air Quality Analysis & Prediction Platform

Bu proje; çevresel veri setleri üzerinde **regresyon analizi** ve **tahminleme** yapmak amacıyla geliştirilmiş, uçtan uca (end-to-end) bir makine öğrenmesi prototipidir. Yazılım mimarisi, modülerlik ve yüksek kohezyon (cohesion) prensipleri doğrultusunda **OOP (Nesne Yönelimli Programlama)** yapısında kurgulanmıştır.

## 🛠️ Teknik Mimari ve Analiz

### 🧠 Makine Öğrenmesi (ML) Modeli
* **Algoritma:** Modelde, non-lineer veri ilişkilerini modelleme yeteneği yüksek olan **Random Forest Regressor** algoritması tercih edilmiştir.
* **Ensemble Learning:** Karar ağaçları tabanlı bu toplu öğrenme yöntemi ile düşük varyans ve yüksek genelleyebilme kapasitesi hedeflenmiştir.
* **Metrikler:** Model performansı **Mean Squared Error (MSE)** üzerinden evalüe edilerek, tahmin hatası minimize edilmiştir.



### 🏗️ Yazılım Katmanları
* **Data Access Layer (DAL):** `DatabaseManager` sınıfı üzerinden **SQLAlchemy** entegrasyonu ile SQLite veritabanı yönetimi sağlanmıştır.
* **Business Logic Layer:** AI modelinin eğitim (training) ve çıkarım (inference) süreçleri `AirQualityModel` sınıfı içinde kapsüllenmiştir (encapsulation).
* **Presentation Layer:** Kullanıcı etkileşimi, reaktif bir yapı sunan **Streamlit framework**'ü üzerinden asenkron olarak yönetilmektedir.



### 📊 Veri Görselleştirme ve Dashboard
* **Regresyon Analizi:** Bağımsız değişkenler (sıcaklık, nem) ile hedef değişken (PM10) arasındaki korelasyon, **Matplotlib** üzerinden regresyon doğrusu ile görselleştirilmiştir.
* **İnteraktif Dashboard:** Kullanıcının dinamik veri girişi yapmasına olanak tanıyan, CSS ile özelleştirilmiş bir arayüz tasarlanmıştır.

## 📂 Dosya Organizasyonu
* `app.py`: Ana uygulama giriş noktası ve UI katmanı.
* `src/database.py`: Veritabanı işlemleri ve SQL sorgu yönetimi.
* `src/model.py`: ML algoritma implementasyonu ve model eğitimi.
* `outputs/`: Model çıktılarının ve grafiklerin saklandığı statik dizin.

## ⚙️ Gereksinimler ve Çalıştırma
Projenin bağımlılıklarını yüklemek ve yerel sunucuda ayağa kaldırmak için:

```bash
pip install -r requirements.txt
streamlit run app.py
Geliştirici: Merve | Bilgisayar Mühendisi Adayı


### 📤 GitHub'a Fırlatma (Update)
Dosyayı kaydettikten sonra terminale şu komutları sırayla yaz:

```powershell
git add README.md
git commit -m "docs: implement advanced technical documentation"
git push
