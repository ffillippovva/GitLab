def can_sell_medicine(requires_prescription, has_prescription):
    if requires_prescription and not has_prescription:
        return False
    return True


def check_stock(stock_quantity, sale_quantity):
    if sale_quantity > stock_quantity:
        return False
    return True