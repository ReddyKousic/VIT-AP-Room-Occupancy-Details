import csv
import json

time_slot_mapping = {
    "theory": {
        "08:00-08:50": ["TF1", "TAA1", "TG1", "TE1", "TCC1"],
        "09:00-09:50": ["TA1", "TD1", "TB1", "C1", "E1"],
        "09:51-10:50": ["E1", "G1", "STA2", "A1", "STA1"],
        "10:00-10:50": ["E1", "F1", "D1", "A1", "G1"],
        "10:51-11:50": ["STC2", "TFF1", "D1", "A2", "TEE1"],
        "11:00-11:50": ["STC2", "D1", "F1", "D1", "B1"],
        "12:00-12:50": ["B1", "TDD1", "B2", "E2", "TE2"],
        "14:00-14:50": ["TA2", "TD2", "B2", "A2", "C2"],
        "15:00-15:50": ["E2", "STA1", "G2", "F2", "B2"],
        "16:00-16:50": ["STC1", "G2", "C2", "D2", "TEE2"],
        "17:00-17:50": ["D2", "TFF2", "C1", "D2", "F2"],
    },
    "lab": {
        "08:00-08:50": ["L1", "L7", "L13", "L19", "L25"],
        "08:51-09:40": ["L2", "L8", "L14", "L20", "L26"],
        "09:41-10:50": ["L3", "L9", "L15", "L21", "L27"],
        "10:51-11:40": ["L4", "L10", "L16", "L22", "L28"],
        "11:41-12:50": ["L5", "L11", "L17", "L23", "L29"],
        "14:00-14:50": ["L31", "L37", "L43", "L49", "L55"],
        "14:51-15:40": ["L32", "L38", "L44", "L50", "L56"],
        "15:41-16:50": ["L33", "L39", "L45", "L51", "L57"],
        "16:51-17:40": ["L34", "L40", "L46", "L52", "L58"],
        "18:00-18:50": ["L35", "L41", "L47", "L53", "L59"],
        "18:51-19:40": ["L36", "L42", "L48", "L54", "L60"],
    }
}

def find_time_for_slot(slot_code):
    slot_type = "lab" if 'L' in slot_code else "theory"
    
    for time_range, slots in time_slot_mapping[slot_type].items():
        if slot_code in slots:
            return time_range
    return "Unknown"

def csv_to_json(file_path):
    result = {}
    
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            block = row['BLOCK']
            slots = row['SLOT'].split('+')  
            room_number = row['ROOM NUMBER']
            course_code = row['COURSE CODE']
            course_title = row['COURSE TITLE']
            employee_name = row['EMPLOYEE NAME']
            
            slot_times = {slot: find_time_for_slot(slot) for slot in slots}
            
            class_info = {
                "course_code": course_code,
                "course_title": course_title,
                "employee_name": employee_name,
                "room_number": room_number,
                "slot_times": slot_times
            }
            
            if block not in result:
                result[block] = {}
            
            for slot in slots:
                if slot not in result[block]:
                    result[block][slot] = []
                
                result[block][slot].append(class_info)
    
    return result

def save_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

csv_file_path = 'cxl.csv'
json_output_file = 'output3.json'

json_data = csv_to_json(csv_file_path)
save_json(json_data, json_output_file)

print("CSV successfully converted to JSON.")
