# 🧮 CalcPro – Kalkulator Canggih Berbasis Web

> Aplikasi web kalkulator canggih dengan tiga kategori utama: Aritmatika, Logika, dan Transformasi Bilangan. Dibangun dengan Python + Flask, tampilan modern glassmorphism, dark/light mode, dan penjelasan langkah demi langkah.

---

## ✨ Fitur Utama

### 1. Operasi Aritmatika
| Operasi | Simbol | Deskripsi |
|---|---|---|
| Penjumlahan | `+` | A + B |
| Pengurangan | `−` | A − B |
| Perkalian | `×` | A × B |
| Pembagian | `÷` | A ÷ B |
| Perpangkatan | `^` | A pangkat B |
| Akar Kuadrat | `√` | √A |
| Modulus | `mod` | Sisa bagi A ÷ B |
| Floor Division | `//` | Pembagian bulat bawah |

### 2. Operator Logika (Bitwise)
| Gerbang | Deskripsi |
|---|---|
| AND | Konjungsi – 1 hanya jika keduanya 1 |
| OR | Disjungsi – 1 jika salah satu 1 |
| NOT | Negasi – membalik bit |
| XOR | Eksklusif OR – 1 jika berbeda |
| NAND | NOT AND |
| NOR | NOT OR |

> Dilengkapi **representasi biner**, **tabel kebenaran visual**, dan langkah bit per bit.

### 3. Transformasi Bilangan
| Jenis | Keterangan |
|---|---|
| **Konversi Basis** | Desimal ↔ Biner ↔ Oktal ↔ Heksadesimal |
| **Konversi Suhu** | Celsius, Fahrenheit, Kelvin, Réaumur |
| **Konversi Mata Uang** | IDR ↔ USD, EUR, SGD, MYR, JPY, GBP, SAR, AUD (rate statis) |
| **Faktorial** | n! untuk n = 0 – 20 |
| **Fibonacci** | Deret Fibonacci hingga suku ke-50 |

### 4. UI/UX
- 🌙 **Dark / Light Mode** dengan toggle (disimpan di localStorage)
- 💎 **Glassmorphism Design** dengan gradient dan animasi halus
- 📱 **Responsif** – ramah mobile
- 📋 **Riwayat Perhitungan** – disimpan dalam session (max 20 entri)
- 📝 **Step-by-Step Explanation** – setiap hasil disertai rumus dan langkah detail
- 📋 **Copy to Clipboard** – salin hasil dengan satu klik

---

## 🗂️ Struktur Proyek

```
Kalkulator/
├── app.py                    # Flask entry point & routing
├── requirements.txt          # Dependensi Python
├── README.md
├── calculator/
│   ├── __init__.py
│   ├── arithmetic.py         # Modul aritmatika
│   ├── logic.py              # Modul logika bitwise
│   └── transformasi.py       # Modul transformasi bilangan
├── templates/
│   ├── base.html             # Layout dasar (navbar, footer)
│   ├── index.html            # Halaman beranda
│   ├── aritmatika.html       # Halaman aritmatika
│   ├── logika.html           # Halaman logika
│   └── transformasi.html     # Halaman transformasi
└── static/
    ├── css/
    │   └── style.css         # CSS lengkap (glassmorphism)
    └── js/
        └── main.js           # JavaScript (theme, animasi, copy)
```

---

## 🚀 Cara Menjalankan Secara Lokal

### Prasyarat
- Python 3.8 atau lebih baru
- pip

### Langkah Instalasi

```bash
# 1. Clone atau download repository
git clone https://github.com/username/kalkulator-canggih.git
cd kalkulator-canggih

# 2. (Opsional) Buat virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependensi
pip install -r requirements.txt

# 4. Jalankan aplikasi
python app.py
```

### Akses Aplikasi
Buka browser dan kunjungi: **http://127.0.0.1:5000**

---

## 🌐 Panduan Deploy ke Domain `.my.id`

### Opsi 1: PythonAnywhere (Gratis)
1. Daftar di [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload semua file proyek
3. Buat Web App baru → pilih Flask → set source code path
4. Edit `WSGI configuration file`:
   ```python
   import sys
   sys.path.insert(0, '/home/username/kalkulator')
   from app import app as application
   ```
5. Reload web app → akses di `username.pythonanywhere.com`
6. Untuk domain custom `.my.id`: daftarkan domain di Niagahoster/Hostinger, lalu arahkan DNS ke server PythonAnywhere

### Opsi 2: VPS (DigitalOcean / Contabo)
```bash
# Install dependensi server
sudo apt update && sudo apt install python3-pip nginx -y
pip3 install gunicorn flask

# Jalankan dengan Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# Setup Nginx sebagai reverse proxy
# Konfigurasi /etc/nginx/sites-available/kalkulator
server {
    listen 80;
    server_name kalkulator-nama.my.id;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

### Setup Domain `.my.id`
1. Beli domain `kalkulator-nama.my.id` di [Niagahoster](https://niagahoster.co.id) atau [Hostinger](https://hostinger.co.id)
2. Di DNS Management, tambahkan record:
   - Type: `A`
   - Name: `@`
   - Value: `IP_SERVER_ANDA`
3. Tunggu propagasi DNS (5–30 menit)
4. (Opsional) Setup SSL gratis dengan Certbot:
   ```bash
   sudo certbot --nginx -d kalkulator-nama.my.id
   ```

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|---|---|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Template Engine | Jinja2 |
| CSS Framework | Bootstrap 5 |
| Font | Inter + JetBrains Mono (Google Fonts) |
| Icons | Bootstrap Icons |
| Session | Flask server-side session |

---

## 📊 Rate Mata Uang (Statis)

| Mata Uang | Rate per IDR |
|---|---|
| USD | 0.000063 (≈ 1 USD = Rp 15.873) |
| EUR | 0.000058 (≈ 1 EUR = Rp 17.241) |
| SGD | 0.000085 (≈ 1 SGD = Rp 11.765) |
| MYR | 0.000297 (≈ 1 MYR = Rp 3.367) |
| JPY | 0.0093 (≈ 1 JPY = Rp 107) |
| GBP | 0.000050 (≈ 1 GBP = Rp 20.000) |
| SAR | 0.000236 (≈ 1 SAR = Rp 4.237) |
| AUD | 0.000097 (≈ 1 AUD = Rp 10.309) |

> ⚠️ Rate bersifat statis untuk keperluan demonstrasi. Untuk rate real-time, integrasikan dengan API seperti ExchangeRate-API.

---

## 👨‍💻 Author

Dibuat untuk tugas mata kuliah **Pemrograman Web** – Semester 2  
Dosen: **Pak Bayu**

---

## 📄 Lisensi

MIT License – bebas digunakan untuk keperluan akademik.
