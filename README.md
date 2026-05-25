# 🧮 CalcTrick – Kalkulator Canggih Berbasis Web

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

---

## 📄 Lisensi

MIT License – bebas digunakan untuk keperluan akademik.
