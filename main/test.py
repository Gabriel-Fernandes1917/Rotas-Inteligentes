import json 
  
# Sample JSON data 
json_data =
{ 
    "sample_data": 
        {"id": 1, "name": "John"}, 
        {"id": 2, "name": "Jane"}, 
        {"id": 3, "name": "Bob"} 
} 
  
# Convert JSON data to a Python object 
data = json.loads(json_data) 
  
# Iterate through the array 
print(data)

    