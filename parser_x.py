import csv
import json


def csv_to_json(file_path):
    result = {}
    

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        

        for row in csv_reader:
            block = row['BLOCK']
            slot = row['SLOT']
            room_number = row['ROOM NUMBER']



            

            if block not in result:
                result[block] = {}
            

            if slot not in result[block]:
                result[block][slot] = []
            

            if room_number not in result[block][slot]:
                result[block][slot].append(room_number)
    
    return result


def save_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


csv_file_path = 'cxl.csv'
json_output_file = 'output.json'


json_data = csv_to_json(csv_file_path)
save_json(json_data, json_output_file)

print("CSV successfully converted to JSON.")
