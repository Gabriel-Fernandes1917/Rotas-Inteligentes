import json 
  
# Sample JSON data 
json_data = """ 
{ 
    "sample_data": [ 
        {"id": 1, "name": "John"}, 
        {"id": 2, "name": "Jane"}, 
        {"id": 3, "name": "Bob"} 
    ] 
} 
"""
  
# Convert JSON data to a Python object 
data = json.loads(json_data) 
  
# Iterate through the array 
for item in data["sample_data"]:  
      # Updated data["sample_data"] as the array is  
    # being present as the value for sample_data 
    print(item["id"], item["name"])