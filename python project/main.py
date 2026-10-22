"""
===========================================================
Student Grade Calculator & Report Card
A beginner-friendly Python mini project
===========================================================

This program:
1. Takes student name and number of subjects (3-5)
2. Collects marks for each subject (0-100)
3. Calculates total, percentage, and grade
4. Displays a formatted report card
5. Allows generating multiple report cards

Author: Generated with Codebuff
Date: 2026
"""

# ============================================================
# FUNCTION 1: get_student_details()
# Purpose: Collects student name and subject details
# Returns: tuple (student_name, list of subject dictionaries)
# Each subject dict has: {'name': subject_name, 'marks': marks}
# ============================================================


def get_student_details():
    """
    Gathers student information and marks for each subject.
    
    The function:
    - Asks for student name
    - Validates number of subjects (must be 3-5)
    - For each subject, gets name and marks (0-100)
    - Uses try-except to handle invalid numeric input
    
    Returns:
        tuple: (student_name, subjects_list)
    """
    
    # Step 1: Get student name
    student_name = input("Enter student name: ").strip()
    
    # Keep asking until we get a non-empty name
    while not student_name:
        print("Name cannot be empty. Please try again.")
        student_name = input("Enter student name: ").strip()
    
    # Step 2: Get number of subjects (must be 3 to 5)
    while True:
        try:
            num_subjects = int(input("Enter number of subjects (3-5): "))
            
            # Check if the number is in valid range
            if 3 <= num_subjects <= 5:
                break  # Valid input, exit the loop
            else:
                print("Please enter a number between 3 and 5.")
                
        except ValueError:
            # This catches non-numeric input like "abc" or "3.5"
            print("Invalid input! Please enter a whole number.")
    
    # Step 3: Collect marks for each subject
    subjects = []  # List to store subject dictionaries
    
    for i in range(1, num_subjects + 1):
        print(f"\n--- Subject {i} ---")
        
        # Get subject name
        subject_name = input(f"Enter name of subject {i}: ").strip()
        while not subject_name:
            print("Subject name cannot be empty.")
            subject_name = input(f"Enter name of subject {i}: ").strip()
        
        # Get marks with validation
        while True:
            try:
                marks = float(input(f"Enter marks for {subject_name} (0-100): "))
                
                # Check if marks are in valid range
                if 0 <= marks <= 100:
                    break  # Valid marks, exit the loop
                else:
                    print("Marks must be between 0 and 100.")
                    
            except ValueError:
                # Catches non-numeric input
                print("Invalid input! Please enter a numeric value.")
        
        # Add this subject to our list
        subjects.append({
            'name': subject_name,
            'marks': marks
        })
    
    return student_name, subjects


# ============================================================
# FUNCTION 2: calculate_results()
# Purpose: Computes total marks, percentage, and pass status
# Parameters: subjects_list (list of subject dictionaries)
# Returns: tuple (total_obtained, max_total, percentage, passed_all)
# ============================================================


def calculate_results(subjects):
    """
    Calculates academic results from subject marks.
    
    Formulas used:
    - Total marks = sum of all subject marks
    - Maximum total = number of subjects × 100
    - Percentage = (total / max_total) × 100
    - Pass status = all subjects must have marks >= 35
    
    Parameters:
        subjects: List of dictionaries with 'name' and 'marks' keys
    
    Returns:
        tuple: (total_obtained, max_total, percentage, passed_all_subjects)
    """
    
    # Calculate total marks obtained
    total_obtained = 0
    for subject in subjects:
        total_obtained += subject['marks']
    
    # Maximum possible marks (each subject is out of 100)
    max_total = len(subjects) * 100
    
    # Calculate percentage using the formula
    # percentage = (total_obtained / max_total) × 100
    percentage = (total_obtained / max_total) * 100
    
    # Check if student passed all subjects (each subject >= 35)
    passed_all_subjects = True
    for subject in subjects:
        if subject['marks'] < 35:
            passed_all_subjects = False
            break  # No need to check further
    
    return total_obtained, max_total, percentage, passed_all_subjects


# ============================================================
# FUNCTION 3: assign_grade()
# Purpose: Determines letter grade based on percentage and pass status
# Parameters: percentage (float), passed_all_subjects (boolean)
# Returns: string grade (A, B, C, or Fail)
# ============================================================


def assign_grade(percentage, passed_all_subjects):
    """
    Assigns a letter grade based on percentage and subject pass status.
    
    Grading criteria:
    - Grade A: 75% and above
    - Grade B: 60% to 74.99%
    - Grade C: 40% to 59.99%
    - Fail: Below 40% OR failed any subject (below 35)
    
    Important: Even with high percentage, failing any subject = Fail
    
    Parameters:
        percentage: Overall percentage (float)
        passed_all_subjects: True if all subjects >= 35 marks
    
    Returns:
        string: 'A', 'B', 'C', or 'Fail'
    """
    
    # First check: Did student fail any subject?
    # This overrides all percentage-based grades
    if not passed_all_subjects:
        return "Fail"
    
    # Now assign grade based on percentage
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


# ============================================================
# FUNCTION 4: display_report_card()
# Purpose: Prints a formatted, well-aligned report card
# Parameters: student_name, subjects, total, max_total, 
#             percentage, grade, passed
# Returns: nothing (just prints to console)
# ============================================================


def display_report_card(student_name, subjects, total_obtained, 
                        max_total, percentage, grade, passed_all):
    """
    Displays a clean, well-aligned report card.
    
    Uses string formatting to create aligned columns:
    - {:<20} means left-align in 20 character width
    - {:>10} means right-align in 10 character width
    - {:.2f} means 2 decimal places for floats
    
    Parameters:
        student_name: Name of the student
        subjects: List of subject dictionaries
        total_obtained: Total marks scored
        max_total: Maximum possible marks
        percentage: Overall percentage
        grade: Letter grade (A, B, C, or Fail)
        passed_all: Boolean for pass/fail status
    """
    
    # Print header with decorative border
    print("\n" + "=" * 50)
    print("           STUDENT REPORT CARD".center(50))
    print("=" * 50)
    
    # Student name section
    print(f"\nStudent Name : {student_name}")
    
    # Table header for subjects
    print("\n" + "-" * 50)
    print(f"{'Subject':<25} {'Marks':>10} {'Status':>12}")
    print("-" * 50)
    
    # Print each subject with marks and pass/fail status
    for subject in subjects:
        marks = subject['marks']
        subject_name = subject['name']
        
        # Determine status for this subject
        if marks >= 35:
            status = "PASS"
        else:
            status = "FAIL"
        
        # Print formatted row
        print(f"{subject_name:<25} {marks:>10.2f} {status:>12}")
    
    # Table footer
    print("-" * 50)
    
    # Summary section
    print(f"\n{'Total Marks:':<25} {total_obtained:>10.2f} / {max_total}")
    print(f"{'Percentage:':<25} {percentage:>10.2f}%")
    print(f"{'Grade:':<25} {grade:>10}")
    print(f"{'Result:':<25} {'PASS' if passed_all else 'FAIL':>10}")
    
    # Final decorative border
    print("\n" + "=" * 50)
    
    # Add a motivational message based on performance
    if grade == "A":
        print("Excellent work! Keep it up! ★")
    elif grade == "B":
        print("Good job! You're doing well!")
    elif grade == "C":
        print("You passed! Room for improvement.")
    else:
        print("Don't give up! Try again next time.")
    print("=" * 50 + "\n")


# ============================================================
# FUNCTION 5: main()
# Purpose: Main program loop - orchestrates all functions
# Returns: nothing
# ============================================================


def main():
    """
    Main function that runs the complete program.
    
    This function:
    - Displays welcome message
    - Runs in a loop to allow multiple report cards
    - Calls all other functions in sequence
    - Handles the continue/exit decision at the end
    """
    
    print("\n" + "=" * 50)
    print("   WELCOME TO STUDENT GRADE CALCULATOR".center(50))
    print("=" * 50)
    print("\nThis program calculates grades and generates report cards.")
    print("Let's get started!\n")
    
    # Main program loop - allows generating multiple report cards
    while True:
        # Step 1: Get student details and marks
        student_name, subjects = get_student_details()
        
        # Step 2: Calculate results
        total_obtained, max_total, percentage, passed_all = calculate_results(subjects)
        
        # Step 3: Assign grade
        grade = assign_grade(percentage, passed_all)
        
        # Step 4: Display the report card
        display_report_card(student_name, subjects, total_obtained,
                          max_total, percentage, grade, passed_all)
        
        # Step 5: Ask if user wants to continue
        while True:
            continue_choice = input("Generate another report card? (yes/no): ").strip().lower()
            
            # Accept various forms of yes/no
            if continue_choice in ['yes', 'y', 'yeah', 'ok']:
                print("\n" + "-" * 50)
                print("Starting new report card...\n")
                break  # Exit inner loop, continue outer loop
            elif continue_choice in ['no', 'n', 'nope', 'quit', 'exit']:
                print("\nThank you for using Student Grade Calculator!")
                print("Goodbye!\n")
                return  # Exit the main function, end program
            else:
                print("Please enter 'yes' or 'no'.")
    
    # This line is never reached due to return above,
    # but included for completeness
    return


# ============================================================
# ENTRY POINT
# Purpose: Ensures main() runs only when script is executed directly
#          (not when imported as a module)
# ============================================================

if __name__ == "__main__":
    # This block runs only when you execute this file directly:
    #   python grade_calculator.py
    #
    # If this file is imported into another script, main() won't run,
    # allowing you to reuse the functions.
    main()
