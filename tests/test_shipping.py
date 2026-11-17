from pricing import shipping_cost


def test_free_shipping_at_200():
    assert shipping_cost(200) == 0


def test_shipping_cost_15_at_100():
    assert shipping_cost(100) == 15


def test_shipping_cost_30_below_100():
    assert shipping_cost(99) == 30
