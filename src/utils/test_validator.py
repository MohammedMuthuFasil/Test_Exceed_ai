from validator import is_email, is_phone, is_positive, is_non_empty_string


def test_email_valid():
    assert is_email("user@example.com") == True

def test_email_with_dots():
    assert is_email("first.last@domain.org") == True

def test_email_no_at():
    assert is_email("userexample.com") == False

def test_email_no_domain():
    assert is_email("user@") == False

def test_email_no_tld():
    assert is_email("user@domain") == False

def test_email_just_at_dot():
    assert is_email("@.") == False

def test_phone_ten_digits():
    assert is_phone("1234567890") == True

def test_phone_with_dashes():
    assert is_phone("123-456-7890") == True

def test_phone_with_parens():
    assert is_phone("(123) 456-7890") == True

def test_phone_too_short():
    assert is_phone("12345") == False

def test_phone_too_long():
    assert is_phone("12345678901") == False

def test_positive_int():
    assert is_positive(5) == True

def test_positive_float():
    assert is_positive(0.1) == True

def test_positive_zero():
    assert is_positive(0) == False

def test_positive_negative():
    assert is_positive(-3) == False

def test_positive_string():
    assert is_positive("5") == False

def test_non_empty_string_valid():
    assert is_non_empty_string("hello") == True

def test_non_empty_string_spaces():
    assert is_non_empty_string("   ") == False

def test_non_empty_string_empty():
    assert is_non_empty_string("") == False

def test_non_empty_string_not_string():
    assert is_non_empty_string(123) == False
