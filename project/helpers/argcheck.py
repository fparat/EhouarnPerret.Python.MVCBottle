def check_value_type(value, t: type):
    if not value and isinstance(t):
        return true


def try_int(s: str):
    try:
        return int(s)
    except ValueError:
        return None
