import json 
import os 

filename='//home//pigli965//Documents//task-tracker//Task_Tracker_CLI//tracker.json'
# Function to append new data to JSON file
def write_json(new_data, filename='tracker.json'):
    if os.path.isfile(filename):
        with open(filename, mode ='r+') as file:
            # Load existing data into a dictionary
            file_data = json.load(file)
            
            # Append new data to the 'emp_details' list
            file_data["tracker_details"].append(new_data)
            
            # Move the cursor to the beginning of the file
            file.seek(0)
            
            # Write the updated data back to the file
            json.dump(file_data, file, indent=4)
    else:
        print('Not exist cum plm')
task={
    "id1":"lidl",
}
write_json(task)








































#     # try: 
#     #     with open(filename ,'r') as file_json:
#     #         file_data=json.load(file_json)
#     # except FileNotFoundError:
#     #     file_data=[]
#     # print(file_data)
#     # entry = {
#     #     'ID':task,
#     # }

#     # file_data.append(entry)
#     # with open(filename, 'w') as file_json:
#         # json.dump(file_data, file_json, indent=4)

#     with open(filename, 'r+') as file:
#         #load existing data into a dictionary
#         file_data = json.load(file)
#         # Append new task 'tracker_details' list
#         file_data["tracker_details"].append(task)
#         # Move the cursor to the beginning of the file
#         file.seek(0)
#         # Write the updated data back to file
#         json.dump(file_data, task, indent=4)

# import json

# Function to append new data to JSON file
# def write_json(new_data, filename='tracker.json'):
#     with open(filename, 'r+') as file:
#         # Load existing data into a dictionary
#         file_data = json.load(file)
        
#         # Append new data to the 'emp_details' list
#         file_data["tracker_details"].append(new_data)
        
#         # Move the cursor to the beginning of the file
#         file.seek(0)
        
#         # Write the updated data back to the file
#         json.dump(file_data, file, indent=4)

# # New data to append
# new_employee = {
#     "emp_name": "Nikhil",
#     "email": "nikhil@geeksforgeeks.org",
#     "job_profile": "Full Time"
# }

# # Call the function to append data
# write_json(new_employee)
