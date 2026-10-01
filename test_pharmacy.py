from pharmacy import can_sell_medicine, check_stock


def test_sale_without_prescription():
    assert can_sell_medicine(False, False) == True


def test_prescription_medicine_without_prescription():
    assert can_sell_medicine(True, False) == False


def test_insufficient_stock():
    assert check_stock(5, 10) == False