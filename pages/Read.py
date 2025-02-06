import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Anda harus login untuk mengakses halaman ini.")
    st.stop() 
else:
    
    import pandas as pd
    from db_connection import create_connection 

    st.title("Menu Read Data")

    def load_data():
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

    data = load_data()
    if data is not None and not data.empty:
        st.write("Data dari tabel karyawan:")
        st.table(data)
    elif data is not None:
        st.error("Tidak ada data untuk ditampilkan.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_page = "home"
        st.rerun()
