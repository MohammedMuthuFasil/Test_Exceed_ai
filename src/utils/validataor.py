def is_email(s):
    return '@' in s and '.' in s

def is_phone(s):
    digits = ''.join(c for c in s if c.isdigit())
    return len(digits) == 10

def is_positive(n):
    return isinstance(n, (int, float)) and n > 0