import price_info

def test_total_cost_shopping():
    test_result = 46.75

    result = price_info.total_cost_shopping()
    assert (result == test_result)


def test_cost_of_fruits():
    test_fruit = "apple"
    test_qty = 10
    test_result = 12.0

    result = price_info.cost_of_fruits(test_fruit, test_qty)
    assert (result == test_result)