# ---------- EMAIL VALIDATION ----------
def validate_email(email):
    if email.count("@") != 1:
        print("Email must contain exactly one '@'. Example: user@mail.com")
        return False

    local, domain_full = email.split("@")

    if not local or not local[0].isalnum():
        print("Email username invalid.")
        return False

    if any(not (c.isalnum() or c in "._") for c in local):
        print("Email username can only contain letters, numbers, dot (.) and underscore (_).")
        return False

    if domain_full.count(".") != 1:
        print("Email domain must contain e" \
        "actly one dot. Example: mail.com")
        return False

    hosting, extension = domain_full.split(".")
    if not hosting.isalnum() or not extension.isalpha() or len(extension) > 5:
        print("Email domain invalid.")
        return False

    return True
# ---------- PRICE FORMAT ----------
def price_format(amount):
    return f"Rp{amount:,}".replace(",", ".")

# ---------- DURATION FORMAT ----------
def duration_format(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours}h {minutes}m"