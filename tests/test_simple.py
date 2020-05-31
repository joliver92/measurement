from measurement import Measurement


def test_basic():
    assert Measurement(2, 3) + Measurement(4, 4) == Measurement(6, 5)
