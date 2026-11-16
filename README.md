# Python_project
# Student Course Registration System (PS 89)

A console-based Python 3 program to register, drop and view student course enrollments.
Built for **Rungta International Skills University – School of Computer Science and Engineering (B.Tech CSE)**.

## Repository Structure

```
Student-Course-Registration-System/
├── One.py          # Complete solution (single Python file)
├── Readme.md       # Describes the repository (this file)
├── Summary.md      # Project summary + screenshots
└── screenshots/    # Output screenshots used in Summary.md
```

`registrations.txt` is created automatically the first time the program runs.

## Features

- Register a student in a course
- Drop a course
- View a student's registered courses
- View the course list with capacity and seats left
- Rejects: full courses, duplicate registrations, unknown courses, and more than 3 courses per student
- Saves all registrations to `registrations.txt` (file handling)

## Concepts Used

OOP (`Student`, `Course`, `RegistrationSystem` classes), Dictionaries, CRUD, File Handling.

## Available Courses

| Code  | Name        | Capacity |
|-------|-------------|----------|
| CS101 | Programming | 2        |
| MA101 | Mathematics | 30       |
| PH101 | Physics     | 30       |

## How to Run

```bash
python One.py
```

Menu options: `1` Register, `2` Drop course, `3` View student, `4` View course list, `5` Exit
(typing the name, e.g. `Register`, also works).

To start from a clean state, delete `registrations.txt` before running.

## Data File Format

Each line in `registrations.txt`: `StudentID|Name|CourseCode1,CourseCode2`
Example: `S101|Riya|CS101,MA101`

## Requirements

Python 3.x (no external libraries).
