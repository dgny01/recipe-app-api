# 🍳 Recipe App API

[![Build Status](https://github.com/dgny01/recipe-app-api/actions/workflows/checks.yml/badge.svg)](https://github.com/dgny01/recipe-app-api/actions)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-3.2-green.svg)](https://djangoproject.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)](https://docker.com)

Bu proje, **Test-Driven Development (TDD)** yaklaşımı benimsenerek geliştirilmiş, **Docker** ve **Nginx** altyapısı üzerine kurgulanmış, prodüksiyon (canlı ortam) standartlarında bir RESTful API servisidir. Gerçek hayat senaryolarına uygun, ölçeklenebilir bir Backend mimarisi hedeflenmiştir.

---

## 🚀 Proje Özellikleri

* **Güvenli Kimlik Doğrulama:** Token tabanlı (Token Authentication) güvenli giriş sistemi, kullanıcı oluşturma ve profil yönetimi.
* **Tarif Yönetimi:** Resim yükleme desteği ile tarif (Recipe) oluşturma, listeleme, güncelleme ve silme işlemleri.
* **Gelişmiş Filtreleme:** Etiket (Tag) ve Malzeme (Ingredient) bazlı akıllı filtreleme özellikleri.
* **Dockerize Altyapı:** Tüm servisler (App, DB, Proxy) Docker ve Docker Compose ile konteynerize edilmiştir.
* **Reverse Proxy:** Statik dosyaların yönetimi ve güvenlik için **Nginx** yapılandırması entegre edilmiştir.
* **CI/CD Hattı:** GitHub Actions kullanılarak kod kalitesi (Linting/Flake8) ve Unit Testler otomatik hale getirilmiştir.
* **İnteraktif Dokümantasyon:** API uç noktaları **Swagger (OpenAPI)** ile otomatik dokümante edilmiştir.

---

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python 3.9, Django 3.2, Django REST Framework
* **Veritabanı:** PostgreSQL
* **DevOps & Altyapı:** Docker, Docker Compose, Nginx
* **Dokümantasyon:** Drf-spectacular (Swagger UI)
* **Kalite Güvence:** Flake8 (Linting), Django Test Framework

---

## 🔧 Kurulum ve Çalıştırma

### Ön Hazırlık
Bilgisayarınızda **Docker** ve **Docker Compose** kurulu olduğundan emin olun.

### 1. Projeyi Klonlayın
```bash
git clone [https://github.com/dgny01/recipe-app-api.git](https://github.com/dgny01recipe-app-api.git)
cd recipe-app-api

2. Ortam Değişkenlerini (Environment) Ayarlayın
Ana dizinde bir .env dosyası oluşturun. Örnek dosyadaki şablonu kullanabilirsiniz:
cp .env.sample .env

3. Derleyin ve Ayağa Kaldırın
Konteynerleri arka planda (detached mode) başlatmak için:
docker compose up -d --build

4. Veritabanı Migrasyonlarını Uygulayın
Tabloların veritabanında oluşması için:
docker compose run --rm app sh -c "python manage.py migrate"

📖 API Dokümantasyonu (Swagger)
Proje ayağa kalktığında, tarayıcınızdan aşağıdaki adrese giderek API'yi test edebilir ve tüm endpoint'leri görebilirsiniz:

👉 URL: http://127.0.0.1/api/docs/

🧪 Test ve Kod Kalitesi
Bu projede "Clean Code" prensiplerine dikkat edilmiştir.

Testleri Çalıştırmak İçin:
docker compose run --rm app sh -c "python manage.py test"

Kod Standartlarını Kontrol Etmek (Linting) İçin:
docker compose run --rm app sh -c "flake8"

📂 Proje Yapısı
.
├── .github/workflows   # CI/CD (GitHub Actions) ayarları
├── app                 # Django kaynak kodları
│   ├── app             # Temel ayarlar (Settings, URLs, WSGI)
│   ├── core            # Paylaşılan modeller ve yönetici paneli
│   ├── recipe          # Tarif iş mantığı (Views, Serializers)
│   └── user            # Kullanıcı işlemleri
├── proxy               # Nginx Docker yapılandırması
├── scripts             # Başlangıç (Entrypoint) scriptleri
├── docker-compose.yml  # Geliştirme ortamı ayarları
├── docker-compose-deploy.yml # Prodüksiyon ortamı ayarları
└── Dockerfile          # Python imaj tanımları

🐳 Docker Mimarisi
Sistem 3 ana servisten oluşur:

1.App: Django uygulamasının çalıştığı Gunicorn servisi.

2.Db: Verilerin tutulduğu PostgreSQL veritabanı.

3.Proxy: Gelen istekleri karşılayan ve statik dosyaları sunan Nginx sunucusu.
