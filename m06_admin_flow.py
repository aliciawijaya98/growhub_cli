from m04_course_database import get_menu
from m05_course_manager import (
    view_courses,
    search_courses,
    edit_course,
    delete_course,
    add_course,
    select_and_sort_courses
)

# ---------- ADMIN MAIN MENU ----------
def admin_menu(current_user):

    # Fetch the current list of courses
    courses = get_menu()

    while True:
        print()
        print("=========== ADMIN MENU =========")
        print()
        print("1. View courses")
        print("2. Search courses")
        print("3. Add course")
        print("4. Back to Main Menu")

        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            admin_view_courses(courses)
        elif choice == 2:
            admin_search_courses(courses)
        elif choice == 3:
            add_course(courses, update_db=True)
        elif choice == 4:
            return "logout"
        else:
            print("Invalid choice.")

# ---------- VIEW COURSES WITH SORT/EDIT ----------
def admin_view_courses(courses):
    while True:

        # Display the current list of courses
        print("\nCourses:")
        view_courses(courses)

        # Ask admin what to do next: sort, edit/delete, or back
        action = input(
        "\nEnter 's' to sort, 'e' to edit, 'd' to delete, or 'q' to go back: "
        ).strip().lower()

        if action == "q":
            break
        elif action == "s":
            courses[:] = select_and_sort_courses(courses)
            print("Courses sorted.")
        elif action == "e":
            confirm = input("Are you sure you want to edit a course? (y/n): ").strip().lower()
            if confirm == "y":
                edit_course(courses)
            else:
                print("Edit cancelled.")
        elif action == "d":
            confirm = input("Are you sure you want to delete a course? (y/n): ").strip().lower()
            if confirm == "y":
                delete_course(courses)
            else:
                print("Delete cancelled.")
        else:
            print("Invalid input. Please type 's', 'e', 'd', or 'q'.")


# ---------- SEARCH COURSES WITH SORT/EDIT ----------
def admin_search_courses(courses):

    while True:
        # Ask admin for search query
        query = input("Search by type or course name (or type 'q' to quit): ").strip().lower()
        
        if query == "q":
            print ("Exiting search...")
            break 
        
        # Search result that match query from database
        search_result = search_courses(courses, query)

        if not search_result:
            print(f"No courses found matching '{query}'.")
            continue
        
        # Allow sorting/editing after search results are shown
        while True:
            print(f"\nFound {len(search_result)} course(s):")
            view_courses(search_result)
            action = input(
                "\nEnter 's' to sort, 'e' to edit, 'd' to delete, or 'q' to go back: "
            ).strip().lower()

            if action == "q":
                break
            elif action == "s":
                # Sort main courses list, then refresh search_result
                courses[:] = select_and_sort_courses(courses)
                search_result = search_courses(courses, query)
                print("Course sorted.")
            elif action == "e":
                confirm = input("Are you sure you want to edit a course? (y/n): ").strip().lower()
                if confirm == "y":
                    edit_course(search_result)
                    search_result = search_courses(courses, query)
                else:
                    print("Edit cancelled.")
            elif action == "d":
                confirm = input("Are you sure you want to delete a course? (y/n): ").strip().lower()
                if confirm == "y":
                    deleted_course = delete_course(search_result, update_db=False)
                    if deleted_course:
                        courses[:] = [c for c in courses if c not in deleted_course]
                    search_result = search_courses(courses, query)
                else:
                    print("Delete cancelled.")
            else:
                print("Invalid input. Please type 's', 'e', 'd', or 'q'.")


if __name__ == "__main__":
    admin_menu()