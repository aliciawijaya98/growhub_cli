from m04_course_database import get_menu, add_menu_item, remove_menu_item
from m01_utils import price_format, duration_format

# View the menu
def view_courses(courses):
    # Print table header
    column_width = "{:<5} | {:<20} | {:<55} | {:<15} | {:<10} | {:<10}"
    header = column_width.format("No.", "Category", "Course Name", "Level", "Price", "Duration")
    print(header)
    print("-" * len(header))

    # Print each menu course in formatted table
    for idx, course in enumerate(courses, start=1):
        print(column_width.format(
            idx, 
            course["category"], 
            course["course_name"], 
            course["level"], 
            price_format(course["price"]), 
            duration_format(course["duration_mins"])
            )
        )

# Search the course by category or course name
def search_courses(courses, query):
    result = []
    query = query.lower()

    for course in courses:
        if (
            query in course["category"].lower()
            or query in course["course_name"].lower()
        ):
            result.append(course)

    return result

# Dictionary for sort options
sort_options = {
    "1": ("category", "Category"),
    "2": ("course_name", "Course Name"),
    "3": ("level", "Level"),
    "4": ("price", "Price"),
    "5": ("duration_mins", "Duration")

}# Sort the course
def sort_courses(courses, key, ascending=True):
    try:
        return sorted(
            courses,
            key=lambda x: x[key],
            reverse=not ascending
        )
    except KeyError:
        print("Invalid sort key.")
        return courses

# Select and sort the course
def select_and_sort_courses(courses):
    if not courses:
        return courses

    while True:
        sort_choice = input("\nDo you want to sort these courses? (y/n): ").strip().lower()
        if sort_choice == "y":
            break  # lanjut ke sort
        elif sort_choice == "n":
            print("Skipping sort...")
            return courses  # skip sort
        else:
            print("Invalid input. Please type 'y' or 'n'")

    print("\nSort by:")
    for key, value in sort_options.items():
        print(f"{key}. {value[1]}")

    while True:
        selected_sort = input("Choose sort option (Enter to skip): ").strip()

        if selected_sort == "":
            print("Skipping sort...")
            return courses
        if selected_sort in sort_options:
            sort_key = sort_options[selected_sort][0]
            break

        print("Invalid option. Please choose 1–5 or press Enter to skip.")

    while True:
        order = input("Ascending or Descending? (a/d): ").strip().lower()
        if order in ("a", "d"):
            ascending = True if order == "a" else False
            break
        print("Invalid input. Please type 'a' for Ascending or 'd' for Descending.")

    return sort_courses(courses, sort_key, ascending)

# Edit course
def edit_course(courses):

    # Return if menu is empty
    if not courses:
        print("No courses available.")
        return
    
    # Show all courses
    view_courses(courses)

    # Ask for index of course to edit/delete
    index = input("Enter the index of the course to edit/delete (or 'q' to quit): ").strip()

    if index.lower() == "q":
        return
    if not index.isdigit() or not (1 <= int(index) <= len(courses)):
        print("Invalid index.")
        return

    selected_course = courses[int(index) - 1]
    print(f"Selected: {selected_course['course_name']}")

    # Prompt new category; Enter keeps old value
    new_category = input(f"New category (Enter to keep '{selected_course['category']}'): ").strip()

    # Prompt new name; Enter keeps old value
    while True:
        new_name = input(
            f"New course name (Enter to keep '{selected_course['course_name']}'): "
        ).strip()

        # Keep old name
        if not new_name:
            break

        # Check duplicate (excluding current course)
        duplicate = any(
            c["course_name"].lower() == new_name.lower()
            and c is not selected_course
            for c in courses
        )

        if duplicate:
            print("A course with this name already exists. Please choose a different name.")
            continue

        break

    # Prompt new level; Enter keeps old value
    valid_levels = ["beginner", "intermediate", "advanced"]

    while True:
        new_level = input(f"New level (Enter to keep '{selected_course['level']}'): ").strip()
        
        # Keep old level if Enter pressed
        if not new_level:
            new_level = selected_course["level"]
            break
        
        if new_level.lower() in valid_levels:
            new_level = new_level.lower().capitalize()
            break
        else:
            print("Invalid level. Please type only 'beginner', 'intermediate', or 'advanced'.")

    # Update the level
    selected_course["level"] = new_level

    # Loop until a valid price is entered
    while True:
        new_price = input(f"New price (Enter to keep '{selected_course['price']}'): ").strip()
        
        # Keep old price if Enter pressed
        if not new_price:
            break
        
        # Only positive number for price
        if not new_price.isdigit() or int(new_price) < 0:
            print("Price must be a non-negative number.")
            continue
        
        # Update new price
        selected_course["price"] = int(new_price)
        break
    
    # Loop until a valid duration is entered
    while True:
        new_duration = input(f"New duration in minutes (Enter to keep '{selected_course['duration_mins']}'): ").strip()
        
        # Keep old duration if Enter pressed
        if not new_duration:
            break
        
        # Only positive number for duration
        if not new_duration.isdigit() or int(new_duration) < 0:
            print("Duration must be a non-negative number.")
            continue
        
        # Update new duration
        selected_course["duration_mins"] = int(new_duration)
        break

    # Update the new input for category and name
    if new_category:
        selected_course["category"] = new_category.title()
    if new_name:
        selected_course["course_name"] = new_name.title()

    print("Course updated successfully!")

def delete_course(courses, update_db=True):
    if not courses:
        print("No courses available.")
        return []

    view_courses(courses)
    index = input("Enter the index of the course to delete (or 'q' to quit): ").strip()
    if index.lower() == "q":
        return []
    if not index.isdigit() or not (1 <= int(index) <= len(courses)):
        print("Invalid index.")
        return []

    selected_course = courses[int(index) - 1]
    
    # Confirm deletion
    confirm = input(
        f"Are you sure you want to delete '{selected_course['course_name']}'? (y/n): "
    ).strip().lower()

    if confirm == "y":
        # Remove from local list
        courses.remove(selected_course)
        # Remove from database
        if update_db:
            remove_menu_item(selected_course)
        print("Course deleted successfully!")
        return [selected_course]
    
    return[]

#Add course
def add_course(courses, update_db=True):

    # Prompt for category
    category = input("Enter category: ").strip().title()

    # Prompt for course name and check duplicates
    while True:
        course_name = input("Enter course name: ").strip().title()

        # Check duplicates
        if any(course["course_name"] == course_name for course in courses):
            print(f"Course already exists. Try another name.")
        else:
            break
    
    #Prompt for course level
    valid_levels = ["beginner", "intermediate", "advanced"]
    
    while True:
        level = input("Enter course level (beginner/intermediate/advanced): ").strip()
        if level.lower() in valid_levels:
            level = level.lower().capitalize()
            break
        else:
            print("Invalid level. Please type only 'beginner', 'intermediate', or 'advanced'.")


    # Prompt for price, ensure integer and non-negative
    while True:
        price = input("Enter price: ").strip()
        if not price.isdigit() or int(price) < 0:
            print("Price must be a non-negative number.")
            continue
        price = int(price)
        break

    # Prompt for duration, ensure integer and non-negative
    while True:
        duration = input("Enter duration (in minutes): ").strip()
        if not duration.isdigit() or int(duration) < 0:
            print("Duration must be a non-negative number.")
            continue
        duration = int(duration)
        break

    # Add new course to menu
    new_course = {
        "category": category,
        "course_name": course_name,
        "level": level,
        "price": price,
        "duration_mins": duration
    }

    # Add to database
    if update_db: 
        add_menu_item(new_course)
    print("Item added successfully!")


if __name__ == "__main__":
    courses = get_menu()