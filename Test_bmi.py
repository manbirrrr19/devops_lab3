import lab2_retry.bmi as bmi


def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 60)
    assert (result == 0)


def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.73, 40)
    assert (result == -1)


def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.73, 110)
    assert (result == 1)