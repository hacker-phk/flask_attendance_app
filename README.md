
# HRMS (Human Resource Management System)

A web-based Human Resource Management System (HRMS) built using Flask, SQLAlchemy, and Tailwind CSS. This project provides functionality to manage employees, track attendance, and generate reports.

## Features
- Employee management (Add, View, Update Attendance)
- Attendance tracking
- Department-wise overview
- Graphical representation of attendance using charts
- Responsive UI built with Tailwind CSS

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [Database Setup](#database-setup)
- [Available Routes](#available-routes)
- [License](#license)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/hrms.git
cd hrms
```

### 2. Create and Activate Virtual Environment
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Make sure you have Python installed (preferably Python 3.10+).
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory with the following configuration:
```plaintext
FLASK_APP=main.py
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=sqlite:///mydatabase.db
```

### 5. Run Database Migrations
Initialize the SQLite database and create the required tables:
```bash
flask db init
flask db migrate
flask db upgrade
```

### 6. Run the Application
```bash
flask run
```

The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

```bash
hrms/
│
├── models/                     # Database models
│   ├── employees.py             # Employee model
│   └── __init__.py
│
├── routes/                     # Flask route handlers               # Fetch all employees     # Update employee attendance
│   ├── attendance_routes.py          # Department-wise attendance overview
│   └── __init__.py
│
├── templates/                  # Jinja2 templates for UI
│   ├── all_employees.html                # Home page template
│   ├── all_employees.html            # Department attendance overview
│   └── overview.html               # Base template
│
├── static/                     # Static files (CSS, JS)
│                  # Custom CSS for styling
│
├── main.py                      # Main Flask app
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .env                         # Environment variables
```

## Environment Setup

1. Install Python 3.10+ from [here](https://www.python.org/downloads/).
2. Install SQLite3 from [here](https://www.sqlite.org/download.html) or use your preferred database.
3. Install Tailwind CSS (optional if you're making modifications to the styles):
   ```bash
   npm install -D tailwindcss
   ```

## Database Setup

The application uses SQLite by default. To switch to a different database like PostgreSQL, update the `SQLALCHEMY_DATABASE_URI` in `.env` accordingly. Example for PostgreSQL:

```plaintext
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost:5432/mydatabase
```

Run migrations whenever you modify the models:
```bash
flask db migrate
flask db upgrade
```

## Available Routes

### 1. Home
- **URL**: `/`
- **Method**: `GET`
- **Description**: Displays a list of all employees.
- **Template**: `home.html`

### 2. Add Employee
- **URL**: `/add`
- **Method**: `POST`
- **Description**: Adds a new employee.
- **Payload**:
  - `name`: Employee's name (string)
  - `designation`: Employee's designation (string)
  - `department`: Department name (string)
  - `doj`: Date of joining (string, in `YYYY-MM-DD` format)
- **Response**: `201 Created` or `400 Bad Request`

### 3. Get All Employees
- **URL**: `/all`
- **Method**: `GET`
- **Description**: Retrieves all employees in the database.

### 4. Update Attendance
- **URL**: `/update-attendance/<int:employee_id>`
- **Method**: `PUT`
- **Description**: Updates attendance status (present/absent) for a specific employee.
- **Payload**:
  - `status`: `present` or `absent`
- **Response**: `200 OK`

### 5. Department-wise Attendance Overview
- **URL**: `/overview/<string:department>`
- **Method**: `GET`
- **Description**: Provides an overview of attendance for employees in a particular department.
- **Template**: `overview.html`

### 6. Attendance Report (Graph)
- **URL**: `/report`
- **Method**: `GET`
- **Description**: Generates a bar graph showing the attendance overview (present/absent count) for each department.
- **Template**: `overview_chart.html` (renders the graph using Chart.js)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
