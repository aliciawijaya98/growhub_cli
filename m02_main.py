from m03_auth import auth_menu
from m06_admin_flow import admin_menu
from m07_member_flow import member_menu

current_user = None
current_role = None

def main_menu():
    global current_user, current_role

    while True:
        if not current_user:
            print()
            print("====== WELCOME TO GROWHUB ======")
            print("==== ONLINE COURSE PLATFORM ====")
            print()
            print("1. Login or Register")
            print("2. Exit Program")
            try:
                choice = int(input("Select an option: ").strip())
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue   

            if choice == 1:
                user, role = auth_menu()

                if user and role:
                    current_user = user
                    current_role = role

                    if current_role == "admin":
                        admin_menu(current_user)
                    elif current_role == "member":
                        member_menu(current_user)
                    
                    current_user = None
                    current_role = None

            elif choice == 2:
                print("Exiting...")
                break
            else:
                print("Invalid option. Try again.")
                continue

if __name__ == "__main__":
    main_menu()
