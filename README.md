<<<<<<< HEAD
# GrowHub — Online Course Platform

## About
**GrowHub** is a **Command Line Interface (CLI)** application that lets members browse, search, and enroll in courses, while administrators can add, edit, or delete courses. 

## Requirements
- Python 3.8 or higher

## Features

### Members
- **Browse Courses** – View all courses with details such as category, name, level, price, and duration.
- **Search & Sort** – Find courses by name or category (partial matches supported) and organize results by any course attribute.
- **Cart Management** – Add or remove courses, view your cart, and confirm checkout.
- **Profile Management** – Update personal information (email or age) or delete your account with confirmation.

### Administrators
- **Course Management** – Add, edit, delete, search, and sort courses for efficient administration.

### General Features
- Interactive menu-driven CLI.
- Input validation and error handling to ensure smooth user experience.
- Modular code structure with a separate course database module.

## Project Structure
```
growhub_cli/
├── m01_utils.py           # Utility functions
├── m02_main.py            # Entry point for the CLI
├── m03_auth/              # Authentication module
├── m04_course_database/   # Course data module
├── m05_course_manager/    # Course management functions
├── m06_admin_flow/        # Admin workflow logic
├── m07_member_flow/       # Member workflow logic
├── README.md              # Project documentation
└── LICENSE                # License file
```

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/aliciawijaya98/growhub_cli.git
```

2. Navigate the folder:
```bash
cd growhub-cli
```

3. Run the CLI
```bash
python m02_main.py
```

## Example of CLI Output
```
====== WELCOME TO GROWHUB ======
==== ONLINE COURSE PLATFORM ====
1. Login or Register
2. Exit Program

=========== ADMIN MENU =========
1. View Courses
2. Search Courses
3. Add Course
4. Edit Course
5. Delete Course
6. Logout

========== MEMBER MENU =========
1. View Courses
2. Search Courses
3. View Cart
4. Profile
5. Logout

```

## Contributing
1. Fork the repository.
2. Create feature branch:
```bash
git checkout -b feature/name
```

3. Commit changes:
```bash
git commit -m "Add feature"
```

4. Push to branch:
```bash
git push origin feature/name
```

5. Open pull request.

## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
=======
# GrowHub — Online Course Platform

## About
**GrowHub** is a **Command Line Interface (CLI)** application that lets members browse, search, and enroll in courses, while administrators can add, edit, or delete courses. 

## Requirements
- Python 3.8 or higher

## Features

### Members
- **Browse Courses** – View all courses with details such as category, name, level, price, and duration.
- **Search & Sort** – Find courses by name or category (partial matches supported) and organize results by any course attribute.
- **Cart Management** – Add or remove courses, view your cart, and confirm checkout.
- **Profile Management** – Update personal information (email or age) or delete your account with confirmation.

### Administrators
- **Course Management** – Add, edit, delete, search, and sort courses for efficient administration.

### General Features
- Interactive menu-driven CLI.
- Input validation and error handling to ensure smooth user experience.
- Modular code structure with a separate course database module.

## Project Structure
```
growhub_cli/
├── m01_utils.py           # Utility functions
├── m02_main.py            # Entry point for the CLI
├── m03_auth/              # Authentication module
├── m04_course_database/   # Course data module
├── m05_course_manager/    # Course management functions
├── m06_admin_flow/        # Admin workflow logic
├── m07_member_flow/       # Member workflow logic
├── README.md              # Project documentation
└── LICENSE                # License file
```

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/aliciawijaya98/growhub_cli.git
```

2. Navigate the folder:
```bash
cd growhub-cli
```

3. Run the CLI
```bash
python m02_main.py
```

## Example of CLI Output
```
====== WELCOME TO GROWHUB ======
==== ONLINE COURSE PLATFORM ====
1. Login or Register
2. Exit Program

=========== ADMIN MENU =========
1. View Courses
2. Search Courses
3. Add Course
4. Edit Course
5. Delete Course
6. Logout

========== MEMBER MENU =========
1. View Courses
2. Search Courses
3. View Cart
4. Profile
5. Logout

```

## Contributing
1. Fork the repository.
2. Create feature branch:
```bash
git checkout -b feature/name
```

3. Commit changes:
```bash
git commit -m "Add feature"
```

4. Push to branch:
```bash
git push origin feature/name
```

5. Open pull request.

## License
This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
>>>>>>> 15ce2ee6eeb2e00339abd91c7d7dbd02b458b07c
