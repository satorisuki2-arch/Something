"""
FILE HANDLING EXAM - BEGINNER LEVEL
====================================
Total Points: 100
Time: 60 minutes

Instructions:
- Complete all questions in this file
- Test your code after each question
- Save your work regularly
- You can use Python documentation
"""

# ============================================================================
# QUESTION 1: Basic File Writing (10 points)
# ============================================================================
"""
Write a function called 'create_greeting_file()' that:
- Creates a new file called 'greeting.txt'
- Writes "Hello, World!" to the file
- Closes the file properly
"""

def create_greeting_file():
    # Write your code here
    pass


# Test Question 1
# Uncomment the line below to test
# create_greeting_file()


# ============================================================================
# QUESTION 2: Reading a File (10 points)
# ============================================================================
"""
Write a function called 'read_greeting()' that:
- Opens and reads the content of 'greeting.txt'
- Returns the content as a string
- Handles the case where the file might not exist
"""

def read_greeting():
    # Write your code here
    pass


# Test Question 2
# Uncomment the lines below to test
# content = read_greeting()
# print(content)


# ============================================================================
# QUESTION 3: Writing Multiple Lines (15 points)
# ============================================================================
"""
Write a function called 'create_todo_list(tasks)' that:
- Takes a list of tasks as parameter
- Creates a file called 'my_tasks.txt'
- Writes each task on a new line with numbering (1. Task1, 2. Task2, etc.)
- Returns the number of tasks written

Example:
    tasks = ["Buy groceries", "Study Python", "Exercise"]
    Result in file:
    1. Buy groceries
    2. Study Python
    3. Exercise
"""

def create_todo_list(tasks):
    # Write your code here
    pass


# Test Question 3
# Uncomment the lines below to test
# sample_tasks = ["Buy groceries", "Study Python", "Exercise"]
# count = create_todo_list(sample_tasks)
# print(f"Wrote {count} tasks to file")


# ============================================================================
# QUESTION 4: Append to File (15 points)
# ============================================================================
"""
Write a function called 'add_task(task)' that:
- Takes a task string as parameter
- Appends the task to 'my_tasks.txt' (doesn't overwrite existing content)
- Adds proper numbering (continues from the last number)
- Returns True if successful, False otherwise
"""

def add_task(task):
    # Write your code here
    pass


# Test Question 4
# Uncomment the lines below to test
# add_task("Call mom")
# add_task("Read a book")


# ============================================================================
# QUESTION 5: Read File Line by Line (10 points)
# ============================================================================
"""
Write a function called 'count_lines(filename)' that:
- Takes a filename as parameter
- Counts and returns the number of lines in the file
- Returns 0 if the file doesn't exist
"""

def count_lines(filename):
    # Write your code here
    pass


# Test Question 5
# Uncomment the line below to test
# print(f"Number of lines: {count_lines('my_tasks.txt')}")


# ============================================================================
# QUESTION 6: Using 'with' Statement (15 points)
# ============================================================================
"""
Write a function called 'safe_write_file(filename, content)' that:
- Uses the 'with' statement to ensure the file is properly closed
- Writes the content to the specified filename
- Returns True if successful
- Handles any exceptions and returns False if an error occurs
"""

def safe_write_file(filename, content):
    # Write your code here
    pass


# Test Question 6
# Uncomment the lines below to test
# result = safe_write_file('test.txt', 'This is a test')
# print(f"Write successful: {result}")


# ============================================================================
# QUESTION 7: File Existence Check (10 points)
# ============================================================================
"""
Write a function called 'file_exists(filename)' that:
- Checks if a file exists
- Returns True if it exists, False otherwise
- Hint: You can use os.path.exists() or try to open the file
"""

def file_exists(filename):
    # Write your code here
    pass


# Test Question 7
# Uncomment the lines below to test
# print(f"greeting.txt exists: {file_exists('greeting.txt')}")
# print(f"nonexistent.txt exists: {file_exists('nonexistent.txt')}")


# ============================================================================
# QUESTION 8: Search in File (15 points)
# ============================================================================
"""
Write a function called 'search_in_file(filename, search_term)' that:
- Searches for a specific term in a file
- Returns a list of line numbers where the term appears (1-indexed)
- Search should be case-insensitive
- Returns an empty list if the file doesn't exist or term not found

Example:
    If 'my_tasks.txt' contains:
    1. Buy groceries
    2. Study Python
    3. Exercise
    
    search_in_file('my_tasks.txt', 'python') should return [2]
"""

def search_in_file(filename, search_term):
    # Write your code here
    pass


# Test Question 8
# Uncomment the lines below to test
# results = search_in_file('my_tasks.txt', 'Python')
# print(f"Found 'Python' on lines: {results}")


# ============================================================================
# BONUS QUESTION: Student Grade Manager (Bonus 20 points)
# ============================================================================
"""
Create a complete Student Grade Manager with the following functions:

1. save_grades(filename, student_dict):
   - Takes a dictionary: {'StudentName': grade, ...}
   - Saves to a file in format: "StudentName,Grade" (CSV format)

2. load_grades(filename):
   - Reads the grades file
   - Returns a dictionary of students and their grades
   - Returns empty dict if file doesn't exist

3. add_student(filename, name, grade):
   - Adds a new student to the grades file
   - Appends without losing existing data

4. get_average_grade(filename):
   - Calculates and returns the average grade from the file
   - Returns 0 if file is empty or doesn't exist

Test your functions with sample data!
"""

def save_grades(filename, student_dict):
    # Write your code here
    pass


def load_grades(filename):
    # Write your code here
    pass


def add_student(filename, name, grade):
    # Write your code here
    pass


def get_average_grade(filename):
    # Write your code here
    pass


# Test Bonus Question
# Uncomment the lines below to test
# sample_grades = {
#     'Alice': 95,
#     'Bob': 87,
#     'Charlie': 92
# }
# save_grades('grades.txt', sample_grades)
# print(load_grades('grades.txt'))
# add_student('grades.txt', 'David', 88)
# print(f"Average grade: {get_average_grade('grades.txt')}")


# ============================================================================
# EXAM TIPS
# ============================================================================
"""
Common File Modes:
- 'r'  : Read (default)
- 'w'  : Write (overwrites file)
- 'a'  : Append (adds to end of file)
- 'r+' : Read and Write
- 'w+' : Write and Read (overwrites file)

Always remember to:
1. Close files after opening (or use 'with' statement)
2. Handle exceptions (try-except blocks)
3. Check if files exist before reading
4. Use appropriate file modes

Good luck! 🐍
"""
