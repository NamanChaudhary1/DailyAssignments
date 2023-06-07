import csv

def calculate_total_marks(input_file, output_file):
    marks_by_roll = {}

    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)

        # Skip the header row
        next(csv_reader)

        for row in csv_reader:
            roll_number, marks = row
            marks = int(marks)

            if roll_number not in marks_by_roll:
                marks_by_roll[roll_number] = marks
            else:
                marks_by_roll[roll_number] += marks

    with open(output_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Roll Number', 'Total Marks'])  # Write the header row

        for roll_number, total_marks in marks_by_roll.items():
            csv_writer.writerow([roll_number, total_marks])

input_file = 'Mini Project - Marks Adding.csv'  # Replace with the path to your input file
output_file = 'output.csv'  # Replace with the desired path for the output file

calculate_total_marks(input_file, output_file)
