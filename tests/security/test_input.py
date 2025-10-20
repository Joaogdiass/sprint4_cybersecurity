import re
def is_valid_email(s: str) -> bool:
    return bool(re.fullmatch(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", s))
def sanitize_str(s: str) -> str:
    return s.strip()

def test_email_validation():
    assert is_valid_email("a@b.com")
    assert not is_valid_email("bad@@x")

def test_sanitize():
    assert sanitize_str("  oi ") == "oi"
