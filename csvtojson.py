import os
import json
import csv
data_dict = {}

with open('./Datasets/Mental_Health_FAQ.csv', encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    for row in csv_reader:
        key = row['Question_ID']
        data_dict[key] = row

with open('./JSON/faq.json', 'w', encoding = 'utf-8') as json_file_handler:
    json_file_handler.write(json.dumps(data_dict, indent = 4))