from m01_utils import validate_email

#DICTIONARY FOR ALL USERS
members = {}
admins = [
        {"username": "administrator_01", "password": "Admin@123"},
        {"username": "administrator_02", "password": "Admin@123"},
        {"username": "administrator_03", "password": "Admin@123"}
        ]

def register():
    print("====== REGISTER NEW MEMBER ======")
    print()

    # ---------- UserID ----------
    while True:
        user_id = input("UserID: ").strip()

        # Length check
        if not 6 <= len(user_id) <= 20:
            print("UserID must be 6–20 characters long.")
            continue

        # Character check
        if not all(c.isalnum() or c in "._" for c in user_id):
            print("UserID can only contain letters, numbers, dot (.) and underscore (_).")
            continue

        # Must have at least one letter and one number
        if not (any(c.isalpha() for c in user_id) and any(c.isdigit() for c in user_id)):
            print("UserID must contain at least one letter and one number.")
            continue

        # Already exists
        if user_id in members or any(a["username"] == user_id for a in admins):
            print("UserID already exists.")
            continue

        break

    # ---------- Password ----------
    while True:
        password = input("Password: ")

        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        if not any(c.isupper() for c in password):
            print("Password must include at least one uppercase letter.")
            continue
        if not any(c.islower() for c in password):
            print("Password must include at least one lowercase letter.")
            continue
        if not any(c.isdigit() for c in password):
            print("Password must include at least one number.")
            continue
        if not any(c in "/.,@#$%" for c in password):
            print("Password must include at least one special character: / . , @ # $ %")
            continue
        if any(not (c.isalnum() or c in "/.,@#$%") for c in password):
            print("Password contains invalid characters.")
            continue

        break

    # ---------- Email ----------
    while True:
        email = input("Email: ").strip()
        if validate_email(email):
            break
        print("Invalid email")

    # ---------- Name ----------
    while True:
        name = input("Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        if any(not (c.isalpha() or c == " ") for c in name):
            print("Name must contain only letters and spaces.")
            continue
        break

    # ---------- Gender ----------
    while True:
        gender = input("Gender (Male/Female): ").strip().lower()
        if gender not in ["male", "female"]:
            print("Invalid input. Please enter 'Male' or 'Female'.")
            continue
        gender = gender.capitalize()
        break

    # ---------- Age ----------
    while True:
        try:
            age = int(input("Age: "))
            if not (17 <= age <= 80):
                print("Age must be between 17 and 80.")
                continue
            break
        except ValueError:
            print("Please input a valid number.")

    # ---------- Confirm ----------
    while True:
        confirm = input("Save data? (y/n): ").strip().lower()
        if confirm in ["y", "n"]:
            break
        print("Please enter 'y' to save or 'n' to cancel.")

    if confirm == "y":
        members[user_id] = {
            "password": password,
            "name": name,
            "email": email,
            "gender": gender,
            "age": age
        }
        print("Registration successful.")
    else:
        print("Registration cancelled.")


# ---------- LOGIN ----------
def login():
    attempts = 0

    while attempts < 5:
        print(f"\nLogin attempt ({attempts+1}/5)")
        user_id = input("UserID: ").strip()
        password = input("Password: ").strip()

        # Check if admin is registered
        admin = next((a for a in admins if a["username"] == user_id), None)
        if admin:
            if admin["password"] == password:
                print("Admin login successful.")
                return user_id, "admin"
            else:
                print("Wrong password.")  
                attempts += 1
                continue
        
        # Check if member is registered
        member = members.get(user_id)
        if member:
            if member["password"] == password:
                print("Member login successful.")
                return user_id, "member"
            else:
                print("Wrong password.")  
                attempts += 1
                continue

        print("User not registered.")
        attempts += 1

    print("Too many attempts.")
    return None, None

# ---------- AUTH MENU ----------
def auth_menu():

    while True:
        print()
        print("=== AUTHENTICATION MENU ===".center(40))
        print()
        print("1. Register")
        print("2. Login")
        print("3. Back to Main Menu")

        try:
            choice = int(input("Choose an option (1-3): ").strip())
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            register()

        elif choice == 2:
            user_id, role = login()
            return user_id, role

        elif choice == 3:
            print("Back to Main Menu")
            return None, None

        else:
            print("Invalid option. Please choose 1-3.")

if __name__ == "__main__":
    auth_menu()