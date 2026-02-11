import sqlite3
import pandas as pd

def get_connection(db_path="data/olist.sqlite"):
    return sqlite3.connect(db_path)

def load_orders_clean(conn):
    return pd.read_sql("""
        SELECT *
        FROM orders
        WHERE order_status = 'delivered'
    """, conn)

def load_order_items_clean(conn):
    return pd.read_sql("""
        SELECT *
        FROM order_items
        WHERE price > 0
    """, conn)
