# CRUD Python MySQL

Repositori ini berisi aplikasi CRUD yang dibangun menggunakan Python dan MySQL. Berikut adalah gambaran umum struktur proyek, petunjuk instalasi, dan panduan penggunaan.

## Video Demo

Berikut adalah beberapa video demo yang menunjukkan aplikasi ini:

1. **Proses Registrasi**:
<video width="600" controls>
  <source src="Video/regist.mp4" type="video/mp4">
  Browser Anda tidak mendukung elemen video.
</video>

2. **Proses Input**:
<video width="600" controls>
  <source src="Video/proses-input.mp4" type="video/mp4">
  Browser Anda tidak mendukung elemen video.
</video>

3. **Lupa Password**:
<video width="600" controls>
  <source src="Video/Lupa-Password.mp4" type="video/mp4">
  Browser Anda tidak mendukung elemen video.
</video>

## Pengaturan Basis Data

### Langkah 1: Buat Basis Data
```sql
CREATE DATABASE CRUD;
```

### Langkah 2: Buat Tabel

#### Tabel `karyawan`
```sql
CREATE TABLE karyawan (
    NIP VARCHAR(20) PRIMARY KEY,
    Nama_Depan VARCHAR(50),
    Nama_Belakang VARCHAR(50),
    Tanggal_Lahir DATE,
    Alamat_Tinggal TEXT,
    Nomor_Handphone VARCHAR(20),
    Jabatan VARCHAR(50),
    Divisi VARCHAR(50)
);
```

#### Tabel `users`
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

## Petunjuk Instalasi

### Instal Git

#### Untuk Debian/Ubuntu:
```bash
sudo apt update
sudo apt install git
```

#### Untuk Fedora:
```bash
sudo dnf install git
```

#### Untuk Arch Linux:
```bash
sudo pacman -S git
```

#### Untuk macOS:
```bash
brew install git
```

#### Untuk Windows:
Unduh Git dari [git-scm.com](https://github.com/yudiiansyaah/yuds-crud.git) dan ikuti petunjuk instalasi.

### Klon Repositori
```bash
git clone https://github.com/yudiiansyaah/yuds-crud.git
cd crud-python-mysql
```

### Buat Virtual Environment

#### Untuk Linux/macOS:
```bash
python3 -m venv venv
```

#### Untuk Windows:
```bash
python -m venv venv
```

### Aktifkan Virtual Environment

#### Untuk Linux/macOS:
```bash
source venv/bin/activate
```

#### Untuk Windows:
```bash
venv\Scripts\activate
```

### Instal Requirements
```bash
pip install -r requirements.txt
```

## Jalankan Aplikasi

#### Untuk Linux/macOS:
```bash
streamlit run Home.py
```

#### Untuk Windows:
```bash
streamlit run Home.py
```

## Struktur Proyek

```
CRUD Python MySQL/
├── db_connection.py
├── Home.py
├── requirements.txt
├── pages/
│   ├── Create.py
│   ├── Delete.py
│   ├── Read.py
│   └── Update.py
└── video/
    ├── regist.mp4
    ├── proses-input.mp4
    └── Lupa-Password.mp4
```


## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE](LICENSE) untuk detailnya.

