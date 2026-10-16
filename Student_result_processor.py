



import csv

# STEP 1: Create the CSV file with student scores
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Score 1", "Score 2", "Score 3"])
    writer.writerow(["emmanuel", 70, 80, 90])
    writer.writerow(["ella", 89, 90, 90])
    writer.writerow(["david", 87, 67, 57])


# STEP 2: Open the CSV file and read the student records
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)  # Skip the header row

    # STEP 3: Open the report file
    with open("student_report.txt", "w") as report:
        report.write("STUDENT RESULT REPORT\n")
        report.write("---------------------\n")

        # STEP 4: Process each student
        for row in reader:
            name = row[0]
            score1 = int(row[1])
            score2 = int(row[2])
            score3 = int(row[3])

            # Calculate the average
            average = (score1 + score2 + score3) / 3

            # STEP 5: Assign a grade
            if average >= 70:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 50:
                grade = "C"
            elif average >= 45:
                grade = "D"
            elif average >= 40:
                grade = "E"
            else:
                grade = "F"

            # STEP 6: Save the student's result
            report.write(
                f"Name: {name} | Average: {average:.2f} | Grade: {grade}\n"
            )

            # Display the result in the terminal
            print(name, f"{average:.2f}", grade)

print("Report saved successfully!")
