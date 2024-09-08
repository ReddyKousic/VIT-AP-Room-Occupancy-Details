import csv
import json

# Function to convert CSV to JSON
def csv_to_json(file_path):
    result = {}
    
    # Read the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        # Iterate through each row of the CSV
        for row in csv_reader:
            block = row['BLOCK']
            slot = row['SLOT']
            room_number = row['ROOM NUMBER']
            course_code = row['COURSE CODE']
            course_title = row['COURSE TITLE']
            employee_name = row['EMPLOYEE NAME']
            
            # Data to add for each class
            class_info = {
                "course_code": course_code,
                "course_title": course_title,
                "employee_name": employee_name,
                "room_number": room_number
            }
            
            # If the block is not in the result, add it
            if block not in result:
                result[block] = {}
            
            # If the slot is not in the block, add it
            if slot not in result[block]:
                result[block][slot] = []
            
            # Add the class information to the slot
            result[block][slot].append(class_info)
    
    return result

# Convert CSV to JSON and save the result to a file
def save_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# File paths
csv_file_path = 'cxl.csv'
json_output_file = 'output2.json'

# Process the CSV and save it as JSON
json_data = csv_to_json(csv_file_path)
save_json(json_data, json_output_file)

print("CSV successfully converted to JSON.")
