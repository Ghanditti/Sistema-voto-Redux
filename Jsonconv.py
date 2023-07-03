import csv
import json

csv_file_path = 'C:\\Users\\Utente\\Documents\\Webserver voti\\abilities.CSV'
json_file_path = 'C:\\Users\\Utente\\Documents\\Webserver voti\\coso.json'

data = []

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        if len(row) < 2:  # Check if the row has at least 2 columns
            continue  # Skip this row if it doesn't have enough columns

        ability_name = row[0]
        ability_description = row[1]

        ability_data = {
            'name': ability_name,
            'description': ability_description
        }

        data.append(ability_data)

with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)