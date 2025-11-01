"""
FILE HANDLING EXAM - ANSWER KEY
================================
This file contains solutions to all exam questions
"""

import os

# ============================================================================
# QUESTION 1: Basic File Writing (10 points)
# ============================================================================
def create_greeting_file():
    file = open('greeting.txt', 'w')
    file.write("Hello, World!")
    file.close()


# ============================================================================
# QUESTION 2: Reading a File (10 points)
# ============================================================================
def read_greeting():
    try:
        file = open('greeting.txt', 'r')
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return "File not found"


# ============================================================================
# QUESTION 3: Writing Multiple Lines (15 points)
# ============================================================================
def create_todo_list(tasks):
    file = open('my_tasks.txt', 'w')
    for index, task in enumerate(tasks, start=1):
        file.write(f"{index}. {task}\n")
    file.close()
    return len(tasks)


# ============================================================================
# QUESTION 4: Append to File (15 points)
# ============================================================================
def add_task(task):
    try:
        # Count existing lines to get the next number
        line_count = 0
        try:
            with open('my_tasks.txt', 'r') as file:
                line_count = len(file.readlines())
        except FileNotFoundError:
            pass
        
        # Append the new task
        with open('my_tasks.txt', 'a') as file:
            file.write(f"{line_count + 1}. {task}\n")
        return True
    except:
        return False


# ============================================================================
# QUESTION 5: Read File Line by Line (10 points)
# ============================================================================
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0


# ============================================================================
# QUESTION 6: Using 'with' Statement (15 points)
# ============================================================================
def safe_write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


# ============================================================================
# QUESTION 7: File Existence Check (10 points)
# ============================================================================
def file_exists(filename):
    # Method 1: Using os.path
    return os.path.exists(filename)
    
    # Method 2: Using try-except
    # try:
    #     with open(filename, 'r') as file:
    #         pass
    #     return True
    # except Exception:
    #     return False


# ============================================================================
# QUESTION 8: Search in File (15 points)
# ============================================================================
def search_in_file(filename, search_term):
    results = []
    try:
        with open(filename, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if search_term.lower() in line.lower():
                    results.append(line_number)
    except FileNotFoundError:
        pass
    return results


# ============================================================================
# BONUS QUESTION: Student Grade Manager (20 points)
# ============================================================================
def save_grades(filename, student_dict):
    try:
        with open(filename, 'w') as file:
            for name, grade in student_dict.items():
                file.write(f"{name},{grade}\n")
        return True
    except:
        return False


def load_grades(filename):
    grades = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, grade = line.split(',')
                    grades[name] = int(grade)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error loading grades: {e}")
    return grades


def add_student(filename, name, grade):
    try:
        with open(filename, 'a') as file:
            file.write(f"{name},{grade}\n")
        return True
    except:
        return False


def get_average_grade(filename):
    try:
        grades = load_grades(filename)
        if not grades:
            return 0
        return sum(grades.values()) / len(grades)
    except:
        return 0


# ============================================================================
# TESTING ALL FUNCTIONS
# ============================================================================
if __name__ == "__main__":
    print("Testing File Handling Exam Solutions\n")
    print("=" * 50)
    
    # Test Q1
    print("\n1. Testing create_greeting_file()...")
    create_greeting_file()
    print("   ✓ File created")
    
    # Test Q2
    print("\n2. Testing read_greeting()...")
    content = read_greeting()
    print(f"   Content: {content}")
    
    # Test Q3
    print("\n3. Testing create_todo_list()...")
    sample_tasks = ["Buy groceries", "Study Python", "Exercise"]
    count = create_todo_list(sample_tasks)
    print(f"   ✓ Wrote {count} tasks to file")
    
    # Test Q4
    print("\n4. Testing add_task()...")
    add_task("Call mom")
    add_task("Read a book")
    print("   ✓ Tasks added")
    
    # Test Q5
    print("\n5. Testing count_lines()...")
    lines = count_lines('my_tasks.txt')
    print(f"   Number of lines: {lines}")
    
    # Test Q6
    print("\n6. Testing safe_write_file()...")
    result = safe_write_file('test.txt', 'This is a test')
    print(f"   Write successful: {result}")
    
    # Test Q7
    print("\n7. Testing file_exists()...")
    print(f"   greeting.txt exists: {file_exists('greeting.txt')}")
    print(f"   nonexistent.txt exists: {file_exists('nonexistent.txt')}")
    
    # Test Q8
    print("\n8. Testing search_in_file()...")
    results = search_in_file('my_tasks.txt', 'Python')
    print(f"   Found 'Python' on lines: {results}")
    
    # Test Bonus
    print("\n9. Testing Student Grade Manager (BONUS)...")
    sample_grades = {
        'Alice': 95,
        'Bob': 87,
        'Charlie': 92
    }
    save_grades('grades.txt', sample_grades)
    print(f"   Saved grades: {sample_grades}")
    
    loaded = load_grades('grades.txt')
    print(f"   Loaded grades: {loaded}")
    
    add_student('grades.txt', 'David', 88)
    print("   ✓ Added David")
    
    average = get_average_grade('grades.txt')
    print(f"   Average grade: {average:.2f}")
    
    print("\n" + "=" * 50)
    print("All tests completed! 🎉")
