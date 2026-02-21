<<<<<<< HEAD
from m05_course_manager import view_courses, search_courses, select_and_sort_courses
from m04_course_database import get_menu
from m01_utils import price_format
from m03_auth import members, validate_email

# Dictionary to store selected courses per member
member_cart = {}

def member_menu(current_user):

    # Fetch latest course list
    courses = get_menu()

    while True:
        print()
        print("========== MEMBER MENU =========")
        print()
        print("1. View All Courses")
        print("2. Search Courses")
        print("3. View Cart")
        print("4. Profile")
        print("5. Logout")
        
        # Ask user for input and validate
        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue
        
        # Handle user choice
        if choice == 1:
            member_view_courses(current_user, courses)
        elif choice == 2:
            member_search_courses(current_user, courses)
        elif choice == 3:
            view_cart(current_user)
        elif choice == 4:
            result = profile(current_user)
            if result == "deleted":
                print("Returning to main menu...")
                return "logout"
        elif choice == 5:
            print("Logout successful.")
            return "logout"
        else:
            print("Invalid choice.")

def member_view_courses(current_user, courses):
    # Display all courses
    view_courses(courses)

    # Let user add courses to cart after viewing
    add_to_cart(current_user, courses)

def member_search_courses(current_user, courses):
    while True:
        query = input("Search by type or course name (or type 'q' to quit): ").strip().lower()
        if query == "q":
            break

        # Search courses that match query
        search_result = search_courses(courses, query)

        if not search_result:
            print(f"No courses found matching '{query}'.")
            continue

        # Ask user if they want to continue search, sort, or add to cart
        while True:
            print(f"\nFound {len(search_result)} course(s):")
            view_courses(search_result)

            choice = input(
                "\nEnter 's' to sort, 'a' to add course to cart, 'f' to search again, or 'q' to go back: "
            ).strip().lower()

            if choice == "a":
                add_to_cart(current_user, search_result)
            elif choice == "s":
                search_result = select_and_sort_courses(search_result)
                print("Search results sorted.")
                continue
            elif choice == "f":
                break
            elif choice == "q":
                return
            else:
                print("Invalid choice. Please type 'a', 's', 'f', or 'q'.")

def add_to_cart(current_user, courses):
    if current_user not in member_cart:
        member_cart[current_user] = []
        
        print("\nYour current cart:")
        view_courses(member_cart[current_user]) if member_cart[current_user] else print("[Cart is empty]")

    while True:
        choice = input(
            "\nEnter course number to add to cart, or 'q' to go back: "
        ).lower().strip()

        if choice == "q":
            return
        if not choice.isdigit() or not (1 <= int(choice) <= len(courses)):
            print("Invalid number.")
            continue
        
        course = courses[int(choice) - 1]

        if any(c["course_name"] == course["course_name"] for c in member_cart[current_user]):
            print("This course is already in your cart.")
            continue

        member_cart[current_user].append(course)
        print(f"Added '{course['course_name']}'.")


# View Cart
def view_cart(current_user):
    cart = member_cart.get(current_user, [])
    if not cart:
        print("[Cart is empty]")
        return
    
    while True:
        # Display cart
        print("\nYour cart:")
        view_courses(cart)

        #Display price
        total = sum(c["price"] for c in cart)
        print(f"\nTotal price: {price_format(total)}")

    
        choice = input(
            "\nEnter course number to remove, 'c' to checkout, or 'q' to go back: "
        ).strip().lower()

        if choice == "q":
            return
        elif choice == "c":
            confirm = input("Confirm checkout? (y/n): ").lower()
            if confirm == "y":
                member_cart[current_user] = []
                print("Checkout successful!")
                return
            continue
        elif not choice.isdigit() or not (1 <= int(choice) <= len(cart)):
            print("Invalid number.")
            continue
        else:
            removed = cart.pop(int(choice) - 1)
            print(f"Removed '{removed['course_name']}' from cart.")

# ---------- PROFILE ----------
def profile(user_id):
    user = members.get(user_id)

    if not user:
        print("User not found.")
        return

    while True:
        print()
        print("============ PROFILE ===========")
        print()
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Gender:", user["gender"])
        print("Age:", user["age"])

        # Profile menu options
        print("\nEnter 'e' to edit profile, 'd' to delete account, or 'q' to back")
        choice = input("Choose option: ").lower().strip()

        if choice == "e":
            edit_profile(user_id)
        elif choice == "d":
            confirm = input("Are you sure you want to delete your account? (y/n): ").lower()
            if confirm == "y":
                del members[user_id]
                print("Account deleted.")
                return "deleted"
            else:
                print("Deletion canceled.")
        elif choice == "q":
            break
        else:
            print("Invalid input. Please choose 'e', 'd', or 'q'.")

    
# ---------- EDIT PROFILE ----------
def edit_profile(user_id):
    user = members.get(user_id)
    print()
    print("========= EDIT PROFILE =========")
    print("Press Enter to skip any field.")
    print()

    if not user:
        print("User not found.")
        return

    # Email
    print(f"\nCurrent Email: {user['email']}")
    while True:
        new_email = input("New Email: ").strip()
        if not new_email:
            break
        if validate_email(new_email):
            user["email"] = new_email
            print("Email updated successfully.")
            break

    # Age
    print(f"\nCurrent Age: {user['age']}")
    new_age = input("New Age: ").strip()

    if new_age:
        try:
            new_age_int = int(new_age)
            if 17 <= int(new_age) <= 80:
                user["age"] = new_age_int
            else:
                print("Age must be between 17 and 80. Age not updated.")
        except ValueError:
            print("Invalid age format. Age not updated.")

    print("\nProfile updated successfully.")

if __name__ == "__main__":
=======
from m05_course_manager import view_courses, search_courses, select_and_sort_courses
from m04_course_database import get_menu
from m01_utils import price_format
from m03_auth import members, validate_email

# Dictionary to store selected courses per member
member_cart = {}

def member_menu(current_user):

    # Fetch latest course list
    courses = get_menu()

    while True:
        print()
        print("========== MEMBER MENU =========")
        print()
        print("1. View All Courses")
        print("2. Search Courses")
        print("3. View Cart")
        print("4. Profile")
        print("5. Logout")
        
        # Ask user for input and validate
        try:
            choice = int(input("Choose an option (1-5): "))
        except ValueError:
            print("Please enter a number between 1 and 5.")
            continue
        
        # Handle user choice
        if choice == 1:
            member_view_courses(current_user, courses)
        elif choice == 2:
            member_search_courses(current_user, courses)
        elif choice == 3:
            view_cart(current_user)
        elif choice == 4:
            result = profile(current_user)
            if result == "deleted":
                print("Returning to main menu...")
                return "logout"
        elif choice == 5:
            print("Logout successful.")
            return "logout"
        else:
            print("Invalid choice.")

def member_view_courses(current_user, courses):
    # Display all courses
    view_courses(courses)

    # Let user add courses to cart after viewing
    add_to_cart(current_user, courses)

def member_search_courses(current_user, courses):
    while True:
        query = input("Search by type or course name (or type 'q' to quit): ").strip().lower()
        if query == "q":
            break

        # Search courses that match query
        search_result = search_courses(courses, query)

        if not search_result:
            print(f"No courses found matching '{query}'.")
            continue

        # Ask user if they want to continue search, sort, or add to cart
        while True:
            print(f"\nFound {len(search_result)} course(s):")
            view_courses(search_result)

            choice = input(
                "\nEnter 's' to sort, 'a' to add course to cart, 'f' to search again, or 'q' to go back: "
            ).strip().lower()

            if choice == "a":
                add_to_cart(current_user, search_result)
            elif choice == "s":
                search_result = select_and_sort_courses(search_result)
                print("Search results sorted.")
                continue
            elif choice == "f":
                break
            elif choice == "q":
                return
            else:
                print("Invalid choice. Please type 'a', 's', 'f', or 'q'.")

def add_to_cart(current_user, courses):
    if current_user not in member_cart:
        member_cart[current_user] = []
        
        print("\nYour current cart:")
        view_courses(member_cart[current_user]) if member_cart[current_user] else print("[Cart is empty]")

    while True:
        choice = input(
            "\nEnter course number to add to cart, or 'q' to go back: "
        ).lower().strip()

        if choice == "q":
            return
        if not choice.isdigit() or not (1 <= int(choice) <= len(courses)):
            print("Invalid number.")
            continue
        
        course = courses[int(choice) - 1]

        if any(c["course_name"] == course["course_name"] for c in member_cart[current_user]):
            print("This course is already in your cart.")
            continue

        member_cart[current_user].append(course)
        print(f"Added '{course['course_name']}'.")


# View Cart
def view_cart(current_user):
    cart = member_cart.get(current_user, [])
    if not cart:
        print("[Cart is empty]")
        return
    
    while True:
        # Display cart
        print("\nYour cart:")
        view_courses(cart)

        #Display price
        total = sum(c["price"] for c in cart)
        print(f"\nTotal price: {price_format(total)}")

    
        choice = input(
            "\nEnter course number to remove, 'c' to checkout, or 'q' to go back: "
        ).strip().lower()

        if choice == "q":
            return
        elif choice == "c":
            confirm = input("Confirm checkout? (y/n): ").lower()
            if confirm == "y":
                member_cart[current_user] = []
                print("Checkout successful!")
                return
            continue
        elif not choice.isdigit() or not (1 <= int(choice) <= len(cart)):
            print("Invalid number.")
            continue
        else:
            removed = cart.pop(int(choice) - 1)
            print(f"Removed '{removed['course_name']}' from cart.")

# ---------- PROFILE ----------
def profile(user_id):
    user = members.get(user_id)

    if not user:
        print("User not found.")
        return

    while True:
        print()
        print("============ PROFILE ===========")
        print()
        print("Name:", user["name"])
        print("Email:", user["email"])
        print("Gender:", user["gender"])
        print("Age:", user["age"])

        # Profile menu options
        print("\nEnter 'e' to edit profile, 'd' to delete account, or 'q' to back")
        choice = input("Choose option: ").lower().strip()

        if choice == "e":
            edit_profile(user_id)
        elif choice == "d":
            confirm = input("Are you sure you want to delete your account? (y/n): ").lower()
            if confirm == "y":
                del members[user_id]
                print("Account deleted.")
                return "deleted"
            else:
                print("Deletion canceled.")
        elif choice == "q":
            break
        else:
            print("Invalid input. Please choose 'e', 'd', or 'q'.")

    
# ---------- EDIT PROFILE ----------
def edit_profile(user_id):
    user = members.get(user_id)
    print()
    print("========= EDIT PROFILE =========")
    print("Press Enter to skip any field.")
    print()

    if not user:
        print("User not found.")
        return

    # Email
    print(f"\nCurrent Email: {user['email']}")
    while True:
        new_email = input("New Email: ").strip()
        if not new_email:
            break
        if validate_email(new_email):
            user["email"] = new_email
            print("Email updated successfully.")
            break

    # Age
    print(f"\nCurrent Age: {user['age']}")
    new_age = input("New Age: ").strip()

    if new_age:
        try:
            new_age_int = int(new_age)
            if 17 <= int(new_age) <= 80:
                user["age"] = new_age_int
            else:
                print("Age must be between 17 and 80. Age not updated.")
        except ValueError:
            print("Invalid age format. Age not updated.")

    print("\nProfile updated successfully.")

if __name__ == "__main__":
>>>>>>> 15ce2ee6eeb2e00339abd91c7d7dbd02b458b07c
    member_menu("test_user")