
def is_valid_number(value):
    
    if value is None:
        return False

    value = str(value).strip()

    if value == "":
        return False

    if value.startswith("-"):
        return False

    parts = value.split(".")

    if len(parts) > 2:
        return False

    for part in parts:
        if part == "" or not part.isdigit():
            return False

    return True


def validate_pin(pin):
    
    return isinstance(pin, str) and pin.isdigit() and len(pin) == 4


def validate_account_number(account_no):
   
    account_no = str(account_no).strip()

    if not account_no.isdigit():
        return False

    return 1000 <= int(account_no) <= 9999


def validate_name(name):
    
    return isinstance(name, str) and name.strip() != "" and all(
        ch.isalpha() or ch.isspace() for ch in name
    )

