from db import get_db
from psycopg2.extras import RealDictCursor


class ProductRepository:
    @staticmethod
    def get_all_products():
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT id, sku, name, price, quantity, description, uuid, created_at FROM products;")
            return cursor.fetchall()

    @staticmethod
    def get_product_by_sku(sku):
        connection = get_db()
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("""
                SELECT id, sku, name, price, quantity, description, uuid, created_at
                FROM products
                WHERE sku = %s;""", (sku,))
            return cursor.fetchone()

    @staticmethod
    def create_product(product):
        conn = get_db()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                INSERT INTO products (sku, name, price, quantity, description, uuid, created_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING *;
            """, (
                product.sku,
                product.name,
                product.price,
                product.quantity,
                product.description,
                product.uuid,
                product.created_at
            ))
            conn.commit()
            return cur.fetchone()

    @staticmethod
    def delete_product(sku):
        conn = get_db()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                "DELETE FROM products WHERE sku = %s RETURNING *;", (sku,))
            deleted = cur.fetchone()
            conn.commit()
            return deleted
