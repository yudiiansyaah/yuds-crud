import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Anda harus login untuk mengakses halaman ini.")
    st.stop() 
else:
    import pandas as pd
    from sqlalchemy import text
    from db_connection import create_connection
    st.title("Menu Delete Data")

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

    def delete_data(delete_nip):
       """Menghapus data karyawan dari database berdasarkan NIP."""
       try:
          engine = create_connection()
          if engine:
             with engine.connect() as connection:
               delete_query = text("DELETE FROM karyawan WHERE NIP = :NIP")
               connection.execute(delete_query, {"NIP": delete_nip})
               connection.commit()
               st.success(f"Data dengan NIP {delete_nip} berhasil dihapus!")
               st.session_state.data_changed = True 

       except Exception as e:
          st.error(f"Terjadi kesalahan saat menghapus data: {e}")

    data = load_data()

    if 'data_changed' not in st.session_state:
        st.session_state.data_changed = False

    if data is not None and not data.empty:
        st.write("Data dari tabel karyawan:")
        st.table(data)

        delete_nip = st.selectbox("Pilih NIP Karyawan untuk Dihapus", data['NIP'])

        if st.button("Hapus Data"):
            delete_data(delete_nip)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.current_page = "home"
        st.rerun()
    if st.session_state.data_changed:
        st.session_state.data_changed = False
        st.rerun()