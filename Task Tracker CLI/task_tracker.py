import json 

#define empty dictionary 
tracker_data = {}

#create the json 
json_task =json.dumps(tracker_data)

with open('tracker.json','w') as file:
    file.write(json_task)

