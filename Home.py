import streamlit as st
from sqlalchemy import text
from db_connection import create_connection

st.set_page_config(
    page_title="Yud'S CRUD",
    page_icon="📊",
    layout="wide"
)

# Inisialisasi session state
if 'login_message' not in st.session_state:
    st.session_state.login_message = None
if 'register_message' not in st.session_state:
    st.session_state.register_message = None
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_page' not in st.session_state:
    st.session_state.current_page = "home"  # Halaman default adalah home
if 'forgot_message' not in st.session_state:
    st.session_state.forgot_message = None
if 'logout_triggered' not in st.session_state:
    st.session_state.logout_triggered = False


def register_user(username, password, email):
    engine = create_connection()
    if engine:
        try:
            with engine.connect() as connection:
                query = text("""
                    INSERT INTO users (username, password, email)
                    VALUES (:username, :password, :email)
                """)
                connection.execute(query, {"username": username, "password": password, "email": email})
                connection.commit()
                return True
        except Exception as e:
            st.error(f"Error saat registrasi: {e}")
    return False

def login_user(username_or_email, password):
    engine = create_connection()
    if engine:
        try:
            with engine.connect() as connection:
                query = text("""
                    SELECT * FROM users
                    WHERE (username = :username_or_email OR email = :username_or_email) AND password = :password
                """)
                result = connection.execute(query, {"username_or_email": username_or_email, "password": password}).fetchone()
                if result:
                    return True
        except Exception as e:
            st.error(f"Error saat login: {e}")
    return False

def logout_user():
    st.session_state.logged_in = False
    st.session_state.current_page = "home"
    st.session_state.logout_triggered = True
    st.rerun()

def reset_password(username_or_email, new_password):
    engine = create_connection()
    if engine:
        try:
            with engine.connect() as connection:
                query = text("""
                    UPDATE users
                    SET password = :new_password
                    WHERE (username = :username_or_email OR email = :username_or_email)
                """)
                connection.execute(query, {"username_or_email": username_or_email, "new_password": new_password})
                connection.commit()
                return True
        except Exception as e:
            st.error(f"Error saat mereset password: {e}")
    return False


def set_page(page_name):
    st.session_state.current_page = page_name
    st.rerun()

if st.session_state.logout_triggered:
  st.session_state.logged_in = False
  st.session_state.logout_triggered = False
  st.session_state.current_page = "home"

if not st.session_state.logged_in:
    st.title("Aplikasi CRUD")
    st.header("Selamat Datang di Aplikasi CRUD")
    st.write("Silakan login atau daftar untuk melanjutkan.")
    st.caption("Aplikasi ini dibuat oleh Yud'S")
    # Form Login
    with st.expander("Masuk"):
        with st.form("login_form"):
            login_username_or_email = st.text_input("Username atau Email")
            login_password = st.text_input("Password", type="password")
            login_submitted = st.form_submit_button("Masuk")

            if login_submitted:
                if login_user(login_username_or_email, login_password):
                    st.session_state.logged_in = True
                    st.session_state.login_message = "Login Berhasil!"
                    st.session_state.current_page = "dashboard"  # Redirect ke dashboard setelah login
                    st.rerun()
                else:
                    st.session_state.login_message = "Login Gagal. Cek Username/Email dan Password."

        if st.session_state.login_message:
            if "Berhasil" in st.session_state.login_message:
                st.success(st.session_state.login_message)
            else:
                st.error(st.session_state.login_message)
        st.session_state.login_message = None

    # Form Register
    with st.expander("Daftar"):
        with st.form("register_form"):
            register_username = st.text_input("Username")
            register_password = st.text_input("Password", type="password")
            register_confirm_password = st.text_input("Konfirmasi Password", type="password")
            register_email = st.text_input("Email")
            register_submitted = st.form_submit_button("Daftar")

            if register_submitted:
               if register_password != register_confirm_password:
                  st.session_state.register_message = "Password tidak sama!"
               else:
                    if register_user(register_username, register_password, register_email):
                      st.session_state.register_message = "Register Berhasil!"
                    else:
                        st.session_state.register_message = "Register Gagal. Mohon lengkapi semua data"

        if st.session_state.register_message:
            if "Berhasil" in st.session_state.register_message:
                st.success(st.session_state.register_message)
            else:
                st.error(st.session_state.register_message)
        st.session_state.register_message = None

    # Fitur Lupa Password
    with st.expander("Lupa Password"):
        with st.form("forgot_password_form"):
            forgot_username_or_email = st.text_input("Username atau Email")
            new_password = st.text_input("Password Baru", type="password")
            confirm_new_password = st.text_input("Konfirmasi Password Baru", type="password")
            forgot_submitted = st.form_submit_button("Reset Password")
                
            if forgot_submitted:
                 if new_password != confirm_new_password:
                     st.session_state.forgot_message = "Password tidak sama!"
                 elif reset_password(forgot_username_or_email, new_password):
                     st.session_state.forgot_message = "Password berhasil direset!"
                 else:
                     st.session_state.forgot_message = "Gagal mereset password. Pastikan Username/Email benar"
        if st.session_state.forgot_message:
            if "berhasil direset" in st.session_state.forgot_message:
                st.success(st.session_state.forgot_message)
            else:
                st.error(st.session_state.forgot_message)
            st.session_state.forgot_message = None
else:
    try:
        st.success("Anda berhasil Login!")
    except:
        pass
    st.title("Selamat Datang!")  
    if st.session_state.current_page == "create":
        import pages.Create as create
    elif st.session_state.current_page == "read":
        import pages.Read as read
    elif st.session_state.current_page == "update":
        import pages.Update as update
    elif st.session_state.current_page == "delete":
        import pages.Delete as delete
    else:
        st.header("Beranda")
        st.write("Selamat Datang! Silahkan melanjutkan kebutuhan Anda")
        st.caption("Aplikasi ini dibuat oleh Yud'S")
        if st.button("Logout"):
            logout_user()