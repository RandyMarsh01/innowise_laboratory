students = []

while True:

    print("--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add a grades for a student")
    print("3. Generate a full report")
    print("4. Find the top students")
    print("5. Exit")

    try:
        number = int(input("Enter a your choice: "))

        if number < 1 or number > 5:
            print("Your number is out of range")
            continue

    except ValueError:
        print("Please enter a number from 1 to 5")
        continue

    if number == 1:
        name = input("Enter a student name: ")
        students.append({"name": name, "grades": []})
        continue

    elif number == 2:

        if not students:
            print("No students available. Please add students first.")
            continue

        input_name = input("Enter a student's name: ")
        student_found = False

        for student in students:

            if student["name"] == input_name:
                student_found = True

                while True:

                    grade_input = (input("Enter a student grade ( or 'done' to finish): "))

                    if grade_input.lower() == "done":
                        break

                    try:
                        grade = int(grade_input)
                        if grade < 0 or grade > 100:
                            print("Please enter a grade from 0 to 100")
                            continue

                        student["grades"].append(grade)
                        continue

                    except ValueError:
                        print("Invalid input. Please enter a number")
                break

        if not student_found:
            print("Student not found")

    elif number == 3:

        print("--- Student report ---")

        if not students:
            print("No students found")

        min_average = None
        max_average = 0
        overall_average = 0
        total_average = 0
        count_average = 0

        for student in students:
            name = student.get("name")
            grade = student.get("grades", [])

            try:
                if grade:
                    average = sum(grade) / len(grade)
                    print(f"{name}'s average grade is: {average:.2f}")

                    if min_average is None or average < min_average:
                        min_average = average

                    if average > max_average:
                        max_average = average

                    total_average += average
                    count_average += 1

                else:
                    print(f"{name}'s average grade is N/A")

            except ZeroDivisionError:
                print("N/A")
            except TypeError:
                print(f"Invalid grades data for {name}")

        if min_average is not None and max_average is not None:
            overall_average = total_average / count_average if count_average > 0 else 0
            print("--------------------------")
            print(f"Min average: {min_average:.2f}")
            print(f"Max average: {max_average:.2f}")
            print(f"Overall average: {overall_average:.2f}")
            print("--------------------------")
        else:
            print("No students found!")

    elif number == 4:
        try:

            best_student = max(students, key=lambda student: sum(student['grades']) / len(student['grades']))

            if not best_student['grades']:
                print("Error: The best student has no grades!")
            else:
                average_grade = sum(best_student['grades']) / len(best_student['grades'])
                print(f"The student with the highest average is {best_student['name']}, with a grade of {average_grade:.2f}")

        except ZeroDivisionError:
            print("Error: One or more students have empty grade lists!")

        except KeyError:
            print("Error: 'grades' key is missing in one or more student!")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    elif number == 5:
        print("Exit program")
        break