import json 

# Function to append new data to JSON file
def write_json(new_data, filename='tracker.json'):
    with open(filename, mode ='r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        # Append new data to the 'emp_details' list
        file_data["tracker_details"].append(new_data)
        # Move the cursor to the beginning of the file
        file.seek(0)
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)


def check_id(filename='tracker.json'):
    f = open("tracker.json")

    data =json.load(f)

    for key, val in data.items():
        print(key, val)
    f.close()

check_id()





































#     # try: 
#     #     with open(filename ,'r') as file_json:
#     #         file_data=json.load(file_json)
#     # except FileNotFoundError:
#     #     file_data=[]
#     # print(file_data)
#     # entry = {
#     #     'ID':task,
#     # }
