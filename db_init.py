from app import create_app
from db import get_db, close_db

def create_tables():
    app = create_app()
    with app.app_context():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                sku VARCHAR(64) UNIQUE NOT NULL,
                name VARCHAR(255) NOT NULL,
                price NUMERIC(10, 2) NOT NULL,
                quantity INTEGER NOT NULL,
                description TEXT,
                uuid UUID NOT NULL,
                created_at TIMESTAMP NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        close_db()

if __name__ == "__main__":
    create_tables()
    print("Tables created.")