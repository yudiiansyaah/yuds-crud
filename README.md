# CRUD Python MySQL

This repository contains a CRUD application built using Python and MySQL. Below is an overview of the project structure, setup instructions, and usage guidelines.

## Demo Videos

Here are some demo videos showcasing the application:

1. **Registration Process**: [regist.mp4](video/regist.mp4)
2. **Input Process**: [proses-input.mp4](video/proses-input.mp4)
3. **Forgot Password**: [Lupa-Password.mp4](video/Lupa-Password.mp4)

## Database Setup

### Step 1: Create Database
```sql
CREATE DATABASE CRUD;
```

### Step 2: Create Tables

#### Table `karyawan`
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

#### Table `users`
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
```

### Step 3: Insert Sample Data

#### Insert into `karyawan`
```sql
INSERT INTO karyawan (NIP, Nama_Depan, Nama_Belakang, Tanggal_Lahir, Alamat_Tinggal, Nomor_Handphone, Jabatan, Divisi) VALUES
('1234567890', 'John', 'Doe', '1985-06-15', '123 Elm Street', '081234567890', 'Manager', 'HR'),
('9876543210', 'Jane', 'Smith', '1990-09-22', '456 Oak Avenue', '081298765432', 'Developer', 'IT');
```

#### Insert into `users`
```sql
INSERT INTO users (username, password, email) VALUES
('admin', 'admin123', 'admin@example.com'),
('user1', 'password123', 'user1@example.com');
```

## Installation Instructions

### Install Git

#### For Debian/Ubuntu:
```bash
sudo apt update
sudo apt install git
```

#### For Fedora:
```bash
sudo dnf install git
```

#### For Arch Linux:
```bash
sudo pacman -S git
```

#### For macOS:
```bash
brew install git
```

#### For Windows:
Download Git from [git-scm.com](https://github.com/yudiiansyaah/yuds-crud.git) and follow the installation instructions.

### Clone the Repository
```bash
git clone https://github.com/yudiiansyaah/yuds-crud.git
cd crud-python-mysql
```

### Create a Virtual Environment

#### For Linux/macOS:
```bash
python3 -m venv venv
```

#### For Windows:
```bash
python -m venv venv
```

### Activate Virtual Environment

#### For Linux/macOS:
```bash
source venv/bin/activate
```

#### For Windows:
```bash
venv\Scripts\activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

## Run the Application

#### For Linux/macOS:
```bash
streamlit run Home.py
```

#### For Windows:
```bash
streamlit run Home.py
```
## Project Structure

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

