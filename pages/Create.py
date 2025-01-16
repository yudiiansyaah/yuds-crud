import streamlit as st
from sqlalchemy import text
from datetime import datetime
from sqlalchemy.exc import IntegrityError # Import IntegrityError

# Pengecekan status login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Anda harus login untuk mengakses halaman ini.")
    st.stop()  
else:

    from db_connection import create_connection 

    st.title("Menu Create Data")

    def save_data(nip, nama_depan, nama_belakang, tanggal_lahir, alamat_tinggal, nomor_handphone, jabatan, divisi):
        """Menyimpan data karyawan baru ke dalam database."""
        engine = create_connection()
        if engine:
            try:
                with engine.connect() as connection:
                    query = text("""
                    INSERT INTO karyawan (NIP, Nama_Depan, Nama_Belakang, Tanggal_Lahir, Alamat_Tinggal, Nomor_Handphone, Jabatan, Divisi)
                    VALUES (:NIP, :Nama_Depan, :Nama_Belakang, :Tanggal_Lahir, :Alamat_Tinggal, :Nomor_Handphone, :Jabatan, :Divisi)
                    """)
                  
                    connection.execute(query, {
                        "NIP": nip,
                        "Nama_Depan": nama_depan,
                        "Nama_Belakang": nama_belakang,
                        "Tanggal_Lahir": tanggal_lahir,
                        "Alamat_Tinggal": alamat_tinggal,
                        "Nomor_Handphone": nomor_handphone,
                        "Jabatan": jabatan,
                        "Divisi": divisi,
                    })
                    connection.commit()
                    st.success("Data berhasil ditambahkan ke database!")
                    st.session_state.data_changed = True  
            except IntegrityError as e: 
                st.error("Data sudah ditambahkan! Anda tidak bisa menambahkan data yang sama!")
            except Exception as e:
                st.error(f"Terjadi kesalahan saat menyimpan data: {e}")

    st.write("Masukan data Karyawan: ")

    nip = st.text_input("NIP", placeholder="Nomor Induk Pegawai")
    nama_depan = st.text_input("Nama Depan", placeholder="Nama Depan")
    nama_belakang = st.text_input("Nama Belakang", placeholder="Nama Belakang")
    tanggal_lahir = st.date_input("Tanggal Lahir")
    alamat_tinggal = st.text_area("Alamat Tinggal", placeholder="Alamat Tinggal Karyawan")
    nomor_handphone = st.text_input("Nomor Handphone", placeholder="Nomor Handphone Karyawan")
    jabatan = st.text_input("Jabatan", placeholder="Jabatan Karyawan")
    divisi = st.text_input("Divisi", placeholder="Divisi Karyawan")

    if 'data_changed' not in st.session_state:
        st.session_state.data_changed = False

    if st.button("Simpan Data"):
        if nip and nama_depan and nama_belakang and tanggal_lahir and alamat_tinggal and jabatan and divisi and nomor_handphone:
             save_data(nip, nama_depan, nama_belakang, tanggal_lahir.strftime("%Y-%m-%d"), alamat_tinggal, nomor_handphone, jabatan, divisi)
        else:
            st.error("Mohon lengkapi semua data sebelum menyimpan")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_page = "home"
        st.rerun()
    if st.session_state.data_changed:
        st.session_state.data_changed = False
        st.rerun()