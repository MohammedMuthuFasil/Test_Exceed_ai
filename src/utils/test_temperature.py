from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin


def test_boiling_point_c_to_f():
    assert celsius_to_fahrenheit(100) == 212

def test_freezing_point_c_to_f():
    assert celsius_to_fahrenheit(0) == 32

def test_body_temp_c_to_f():
    assert celsius_to_fahrenheit(37) == 98.6

def test_negative_c_to_f():
    assert celsius_to_fahrenheit(-40) == -40

def test_boiling_point_f_to_c():
    assert fahrenheit_to_celsius(212) == 100

def test_freezing_point_f_to_c():
    assert fahrenheit_to_celsius(32) == 0

def test_negative_f_to_c():
    assert fahrenheit_to_celsius(-40) == -40

def test_absolute_zero_c_to_k():
    assert celsius_to_kelvin(-273.15) == 0

def test_freezing_point_c_to_k():
    assert celsius_to_kelvin(0) == 273.15

def test_boiling_point_c_to_k():
    assert celsius_to_kelvin(100) == 373.15

def test_room_temp_c_to_k():
    assert celsius_to_kelvin(25) == 298.15
