"""
Metric definitions used across the project.

All metrics are defined as pure functions.
They assume input data has already been cleaned and scoped.
"""


def calc_gmv(order_items):
    """
    GMV (Gross Merchandise Value)

    Definition:
    Sum of item prices at the order-item level.
    Freight cost is excluded.

    Parameters
    ----------
    order_items : pandas.DataFrame
        Cleaned order_items data.

    Returns
    -------
    float
        Total GMV.
    """
    return order_items["price"].sum()


def calc_order_count(orders):
    """
    Order Count

    Definition:
    Number of unique orders.

    Parameters
    ----------
    orders : pandas.DataFrame
        Cleaned orders data.

    Returns
    -------
    int
        Total number of orders.
    """
    return orders["order_id"].nunique()


def calc_aov(orders, order_items):
    """
    AOV (Average Order Value)

    Definition:
    AOV = GMV / Order Count

    Parameters
    ----------
    orders : pandas.DataFrame
        Cleaned orders data.
    order_items : pandas.DataFrame
        Cleaned order_items data.

    Returns
    -------
    float
        Average order value.
    """
    order_cnt = calc_order_count(orders)
    if order_cnt == 0:
        return 0

    gmv = calc_gmv(order_items)
    return gmv / order_cnt
