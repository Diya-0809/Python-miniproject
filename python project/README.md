=====================================================================
SAMPLE RUN: Student Grade Calculator & Report Card
=====================================================================

--- Sample Input ---

Enter student name: Alice Johnson
Enter number of subjects (3-5): 3

--- Subject 1 ---
Enter name of subject 1: Mathematics
Enter marks for Mathematics (0-100): 85

--- Subject 2 ---
Enter name of subject 2: Science
Enter marks for Science (0-100): 72

--- Subject 3 ---
Enter name of subject 3: English
Enter marks for English (0-100): 45
Do you want to continue? (yes/no): no

--- Sample Output ---

==================================================
               STUDENT REPORT CARD            
==================================================

Student Name : Alice Johnson

--------------------------------------------------
Subject                    Marks       Status
--------------------------------------------------
Mathematics                  85.00         PASS
Science                      72.00         PASS
English                      45.00         PASS
--------------------------------------------------

Total Marks:                 202.00 / 300
Percentage:                  67.33%
Grade:                             B
Result:                         PASS

==================================================
Good job! You're doing well!
==================================================

=====================================================================
ANOTHER SAMPLE: Student who fails
=====================================================================

--- Sample Input ---

Enter student name: Rohan Mehta
Enter number of subjects (3-5): 4

--- Subject 1 ---
Enter name of subject 1: Physics
Enter marks for Physics (0-100): 90

--- Subject 2 ---
Enter name of subject 2: Chemistry
Enter marks for Chemistry (0-100): 88

--- Subject 3 ---
Enter name of subject 3: Mathematics
Enter marks for Mathematics (0-100): 92

--- Subject 4 ---
Enter name of subject 4: Computer Science
Enter marks for Computer Science (0-100): 30

--- Sample Output ---

==================================================
               STUDENT REPORT CARD            
==================================================

Student Name : Rohan Mehta

--------------------------------------------------
Subject                    Marks       Status
--------------------------------------------------
Physics                      90.00         PASS
Chemistry                    88.00         PASS
Mathematics                  92.00         PASS
Computer Science             30.00         FAIL
--------------------------------------------------

Total Marks:                 300.00 / 400
Percentage:                  75.00%
Grade:                            Fail
Result:                         FAIL

==================================================
Don't give up! Try again next time.
==================================================

Note: Even though Rohan has 75% (which would normally be Grade A),
he FAILS because he scored below 35 in Computer Science.

=====================================================================
LOGIC EXPLANATION AND FORMULAS
=====================================================================

1. PERCENTAGE FORMULA:
   ---------------------
   Percentage = (Total Marks Obtained / Maximum Total Marks) × 100
   
   Example: If total obtained = 202 and max total = 300
   Percentage = (202 / 300) × 100 = 67.33%
   
   Why multiply by 100? 
   - This converts the fraction to a percentage
   - 202/300 = 0.6733... → 0.6733 × 100 = 67.33%

2. MAXIMUM TOTAL MARKS:
   ---------------------
   Maximum Total = Number of Subjects × 100
   
   Each subject is out of 100 marks, so:
   - 3 subjects → 300 maximum
   - 4 subjects → 400 maximum
   - 5 subjects → 500 maximum

3. GRADING LOGIC (if-elif-else):
   ------------------------------
   The grade is decided in this order:
   
   Step 1: Check if any subject has marks < 35
           → If YES: Grade = "Fail" (immediate fail)
           → If NO: Continue to Step 2
   
   Step 2: Check percentage
           - 75% or above → Grade A
           - 60% to 74.99% → Grade B  
           - 40% to 59.99% → Grade C
           - Below 40% → Grade Fail
   
   Why check subject pass first?
   - A student could have 90% overall but fail one subject
   - Most education systems require passing ALL subjects
   - This is why Rohan (75%) still fails

4. PASS/FAIL FOR INDIVIDUAL SUBJECTS:
   -----------------------------------
   - Marks >= 35 → PASS
   - Marks < 35 → FAIL
   
   This threshold (35) is common in many education systems.

5. INPUT VALIDATION:
   ------------------
   - Number of subjects: Must be integer between 3 and 5
   - Marks: Must be number between 0 and 100
   - try-except ValueError: Catches non-numeric input
   - while loops: Keep asking until valid input received

=====================================================================
5 VIVA QUESTIONS WITH ANSWERS
=====================================================================

-----------------------------------------------------------------
Question 1: What is the formula used to calculate percentage?
-----------------------------------------------------------------
Answer: 
The percentage formula is:
    Percentage = (Total Marks Obtained / Maximum Total Marks) × 100

In the code, this is written as:
    percentage = (total_obtained / max_total) * 100

Where:
- total_obtained = sum of all subject marks
- max_total = number of subjects × 100

Example: For 3 subjects with marks 85, 72, 45:
- Total = 202
- Max = 300
- Percentage = (202/300) × 100 = 67.33%

-----------------------------------------------------------------
Question 2: Why do we check if a student failed any subject before
assigning a grade based on percentage?
-----------------------------------------------------------------
Answer:
In most education systems, passing each subject individually is 
required to pass overall. Even if a student has a high percentage
(75% or more), failing any single subject means the student must 
reappear for that subject.

The logic flow is:
1. First check: Did student score < 35 in any subject?
   - If YES → Immediate Fail (regardless of percentage)
   - If NO → Proceed to percentage-based grading

This ensures the grading system follows real-world academic rules.

-----------------------------------------------------------------
Question 3: How does the if-elif-else structure work for grading?
-----------------------------------------------------------------
Answer:
The if-elif-else chain checks conditions in order:

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

How it works:
- Python checks each condition from top to bottom
- As soon as one condition is True, that branch executes
- The rest are skipped (no elif/else after a match)
- If nothing matches, the else block runs

Example with 67.33%:
- 67.33 >= 75? NO → skip
- 67.33 >= 60? YES → Grade B (stop here)

This is efficient because only one branch ever executes.

-----------------------------------------------------------------
Question 4: What is the purpose of try-except in this program?
-----------------------------------------------------------------
Answer:
The try-except block handles invalid user input gracefully:

    try:
        marks = float(input("Enter marks: "))
        if 0 <= marks <= 100:
            break
    except ValueError:
        print("Invalid input! Please enter a number.")

Without try-except:
- If user types "abc" instead of a number
- float() would raise ValueError
- Program would crash with an error

With try-except:
- ValueError is caught
- User gets a friendly message
- Loop continues, asking again
- Program doesn't crash

This is called "exception handling" and makes programs robust.

-----------------------------------------------------------------
Question 5: Why use functions instead of writing all code in main()?
-----------------------------------------------------------------
Answer:
Using separate functions provides several benefits:

1. MODULARITY: Each function does ONE thing well
   - get_student_details(): Only collects input
   - calculate_results(): Only does math
   - assign_grade(): Only decides grade
   - display_report_card(): Only prints output

2. REUSABILITY: Functions can be called multiple times
   - We can generate multiple report cards in a loop
   - Each call reuses the same functions

3. READABILITY: Code is easier to understand
   - Function names describe what they do
   - main() reads like a story:
     * Get details → Calculate → Assign grade → Display

4. TESTING: Easier to test individual parts
   - Can test calculate_results() separately
   - Can verify grade logic independently

5. MAINTENANCE: Changes are localized
   - If grading rules change, only edit assign_grade()
   - If report format changes, only edit display_report_card()

This follows the "Single Responsibility Principle" in programming.

=====================================================================
ADDITIONAL NOTES FOR VIVA
=====================================================================

Key Programming Concepts Used:
- Variables and data types (int, float, string, boolean, list, dict)
- Lists and dictionaries for data storage
- Loops (for loop for subjects, while loop for validation)
- Conditionals (if-elif-else for grading)
- Functions (4 separate functions + main)
- String formatting (alignment with {:<25}, {:>10})
- Exception handling (try-except ValueError)
- Module structure (if __name__ == "__main__")
- Type conversion (int(), float())
- Boolean flags (passed_all_subjects)

Common Mistakes to Avoid:
1. Forgetting to multiply by 100 in percentage calculation
2. Not checking individual subject pass before overall grade
3. Using > instead of >= (boundary conditions)
4. Not handling non-numeric input (crashes program)
5. Forgetting to initialize variables before using them

Edge Cases Handled:
- Empty student name
- Invalid number of subjects (not 3-5)
- Non-numeric marks input
- Marks outside 0-100 range
- Marks exactly at boundary (35, 40, 60, 75)
- Student with high percentage but failed subject
