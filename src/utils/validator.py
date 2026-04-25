import re

def is_email(s):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, s))

def is_phone(s):
    digits = ''.join(c for c in s if c.isdigit())
    return len(digits) == 10

def is_positive(n):
    return isinstance(n, (int, float)) and n > 0

def is_non_empty_string(s):
    return isinstance(s, str) and len(s.strip()) > 0