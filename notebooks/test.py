from src.data_scope import get_connection, load_orders_clean, load_order_items_clean
from src.metrics import calc_gmv, calc_order_count, calc_aov

conn = get_connection()
orders = load_orders_clean(conn)
items = load_order_items_clean(conn)

print(calc_gmv(items))
print(calc_order_count(orders))
print(calc_aov(orders, items))
