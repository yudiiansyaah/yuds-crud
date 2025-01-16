import streamlit as st
from datetime import datetime

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Anda harus login untuk mengakses halaman ini.")
    st.stop()  

    import pandas as pd
    from sqlalchemy import text
    from db_connection import create_connection  

    st.title("Menu Update Data")

    def load_data():
        """Membaca data dari tabel karyawan dan mengembalikan DataFrame."""
        try:
            engine = create_connection()
            if engine:
                data = pd.read_sql_query("""
                    SELECT NIP, Nama_Depan, Nama_Belakang, Tanggal_Lahir, Alamat_Tinggal, Nomor_Handphone, Jabatan, Divisi
                    FROM karyawan
                """, engine)
                return data
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca data: {e}")
            return None

    def update_data(nip, nama_depan, nama_belakang, tanggal_lahir, alamat_tinggal, nomor_handphone, jabatan, divisi):
        """Mengupdate data karyawan dalam database."""
        try:
            engine = create_connection()
            if engine:
                with engine.connect() as connection:
                    update_query = text("""
                        UPDATE karyawan
                        SET Nama_Depan = :Nama_Depan,
                            Nama_Belakang = :Nama_Belakang,
                            Tanggal_Lahir = :Tanggal_Lahir,
                            Alamat_Tinggal = :Alamat_Tinggal,
                            Nomor_Handphone = :Nomor_Handphone,
                            Jabatan = :Jabatan,
                            Divisi = :Divisi
                        WHERE NIP = :NIP
                    """)

                    connection.execute(update_query, {
                        'Nama_Depan': nama_depan,
                        'Nama_Belakang': nama_belakang,
                        'Tanggal_Lahir': tanggal_lahir,
                        'Alamat_Tinggal': alamat_tinggal,
                        'Nomor_Handphone': nomor_handphone,
                        'Jabatan': jabatan,
                        'Divisi': divisi,
                        'NIP': nip
                    })
                    connection.commit()
                    st.success(f"Data dengan NIP {nip} berhasil diperbarui!")
                    st.session_state.data_changed = True  
        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengupdate data: {e}")

    data = load_data()

    if 'data_changed' not in st.session_state:
        st.session_state.data_changed = False

    if data is not None and not data.empty:
        st.write("Data dari tabel karyawan:")
        st.table(data)

        update_nip = st.selectbox("Pilih NIP Karyawan untuk Diperbarui", data['NIP'])

        selected_data = data[data['NIP'] == update_nip].iloc[0]

        updated_nama_depan = st.text_input("Nama Depan", selected_data['Nama_Depan'])
        updated_nama_belakang = st.text_input("Nama Belakang", selected_data['Nama_Belakang'])
        updated_tanggal_lahir = st.date_input("Tanggal Lahir", value=datetime.strptime(str(selected_data['Tanggal_Lahir']), "%Y-%m-%d").date())
        updated_alamat_tinggal = st.text_area("Alamat Tinggal", selected_data['Alamat_Tinggal'])
        updated_nomor_handphone = st.text_input("Nomor Handphone", selected_data['Nomor_Handphone'])
        updated_jabatan = st.text_input("Jabatan", selected_data['Jabatan'])
        updated_divisi = st.text_input("Divisi", selected_data['Divisi'])

        if st.button("Update Data"):
            update_data(update_nip, updated_nama_depan, updated_nama_belakang, updated_tanggal_lahir.strftime("%Y-%m-%d"), updated_alamat_tinggal, updated_nomor_handphone, updated_jabatan, updated_divisi)
    if st.button("Logout"):
      st.session_state.logged_in = False
      st.session_state.current_page = "home"
      st.rerun()

    if st.session_state.data_changed:
        st.session_state.data_changed = False
        st.rerun()