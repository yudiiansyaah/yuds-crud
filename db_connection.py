from sqlalchemy import create_engine

def create_connection():
    """Membuat koneksi ke database MySQL menggunakan SQLAlchemy."""
    host = "localhost"
    user = "root"
    password = ""
    database = "CRUD"
    
    try:
        engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')
        with engine.connect() as connection:
            pass
        return engine
    except Exception as e:
        print(f"Error connecting to the database: {e}") 
        return None