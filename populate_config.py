import os
import json

project_name = 'project'
file_names = []

for path, subdirs, files in os.walk(project_name):
    for name in files:
        current_file_path = os.path.join(path, name)
        if current_file_path[-2:] == "py":
            formatted_name = current_file_path.replace("\\", ".")[:-3]
            if not formatted_name.endswith('load_config'):
                file_names.append(formatted_name)

name = "calculator"

# This will be the dictionary that determines our entire sphinx app:
settings = {
    "project_name": name,
    "pip_package": name,
    "theme": "furo",
    "first_name": "Jacob",
    "last_name": "Chang",
    "year": "2022",
    "desc": "Calculator is a Python library for people who like to do mathematics.",
    "active": 1,
    "files": file_names
}

# writes our settings to the config.json file:
jsonString = json.dumps([settings])
jsonFile = open("config.json", "w")
jsonFile.write(jsonString)
jsonFile.close()