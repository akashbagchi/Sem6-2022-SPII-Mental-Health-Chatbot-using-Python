import os
import json
import csv
data_dict = {}

with open(r'D:\Uni\6th Sem\Special Topics\ChatBot\Datasets\Mental_Health_FAQ.csv', encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    for row in csv_reader:
        key = row['Question_ID']
        data_dict[key] = row

with open(r'D:\Uni\6th Sem\Special Topics\ChatBot\faq.json', 'w', encoding = 'utf-8') as json_file_handler:
    json_file_handler.write(json.dumps(data_dict, indent = 4))