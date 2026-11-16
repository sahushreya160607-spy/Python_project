# Project Summary – Student Course Registration System (PS 89)

## 1. Problem Statement
Build a registration program using classes `Student` and `Course` that can register, drop and view courses.
It must reject full courses, duplicate registrations, unknown courses and more than 3 courses per student,
and save registrations to a file.

## 2. Approach
- `Course` stores code, name, capacity and enrolled students; it reports seats left.
- `Student` stores ID, name and registered course codes.
- `RegistrationSystem` keeps courses and students in dictionaries and implements Create (register), Read (view student / course list), Delete (drop) operations.
- After every change the data is written to `registrations.txt`, and it is reloaded on start-up.
- Validation order for registration: unknown course → duplicate → 3-course limit → course full.

## 3. Test Cases (run in order from an empty `registrations.txt`)

| # | Input | Expected Output | Result |
|---|-------|-----------------|--------|
| 1 | Register S101, Riya, CS101 | Registered: Riya (S101) in CS101 - Programming. Seats left: 1 | Pass |
| 2 | Register S102, Arjun, CS101 | Registered: Arjun (S102) in CS101 - Programming. Seats left: 0 | Pass |
| 3a | Register S103, Meera, CS101 | Course CS101 is full. | Pass |
| 3b | Register S101, Riya, CS101 | Student S101 is already registered in CS101. | Pass |
| 3c | Register S104, Neel, EE999 | Course EE999 does not exist. | Pass |
| 4a | Drop S101, CS101 | Riya (S101) dropped CS101. Seats left: 1 | Pass |
| 4b | View student S101 | Riya (S101) has no registered courses. | Pass |

## 4. Screenshots

> Run the program, take a screenshot of each test case and save it in the `screenshots/` folder.

**Test Case 1 – Normal Input**
![Test Case 1](screenshots/test1.png)

**Test Case 2 – Boundary Input**
![Test Case 2](screenshots/test2.png)

**Test Case 3 – Invalid Input**
![Test Case 3](screenshots/test3.png)

**Test Case 4 – Different Valid Scenario**
![Test Case 4](screenshots/test4.png)

## 5. Conclusion
The program meets all requirements of PS 89 and passes all four test cases. Possible improvements: a GUI, a database instead of a text file, and an admin option to add new courses.
