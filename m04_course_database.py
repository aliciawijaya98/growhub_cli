#Initial events data
courses = [
    {
        "category": "Tech",
        "course_name": "Python for Beginners",
        "level": "Beginner",
        "price": 299000,
        "duration_mins": 450
    },
    {
        "category": "Tech",
        "course_name": "SQL for Data Analysis",
        "level": "Beginner",
        "price": 299000,
        "duration_mins": 120
    },
    {
        "category": "Business",
        "course_name": "Business Analytics Fundamentals",
        "level": "Beginner",
        "price": 499000,
        "duration_mins": 900
    },
    {
        "category": "Business",
        "course_name": "HR Analytics for Beginners",
        "level": "Beginner",
        "price": 399000,
        "duration_mins": 30
    },
    {
        "category": "Language",
        "course_name": "English for Professional Email",
        "level": "Beginner",
        "price": 199000,
        "duration_mins": 780
    },
    {
        "category": "Language",
        "course_name": "Business English Conversation",
        "level": "Intermediate",
        "price": 299000,
        "duration_mins": 440
    }
]

#Return the lastest course list
def get_menu():
    return courses

#Add a new item to the course list
def add_menu_item(course):
    courses.append(course)

#Delete a item from the course list
def remove_menu_item(course):
    if course in courses:
        courses.remove(course)