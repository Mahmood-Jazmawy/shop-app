import pytest
from pricing import apply_coupon


def test_welcome10_coupon():
    assert apply_coupon(100, "WELCOME10") == 90


def test_vip20_coupon():
    assert apply_coupon(100, "VIP20") == 80


def test_coupon_lowercase():
    assert apply_coupon(100, "vip20") == 80


def test_unknown_coupon():
    with pytest.raises(ValueError):
        apply_coupon(100, "INVALID")
