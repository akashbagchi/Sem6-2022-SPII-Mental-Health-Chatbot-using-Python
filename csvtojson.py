import os
import json
import csv
data_dict = {}
data_dict['intents'] = []

with open('./Datasets/Mental_Health_FAQ.csv', encoding = 'utf-8') as csv_file_handler:
    csv_reader = csv.DictReader(csv_file_handler)
    for row in csv_reader:
        row['tag'] = row['Question_ID']
        del(row['Question_ID'])
        row['patterns'] = row['Questions']
        del(row['Questions'])
        row['responses'] = row['Answers']
        del(row['Answers'])
        data_dict['intents'].append(row)

with open('./JSON/faq.json', 'w', encoding = 'utf-8') as json_file_handler:
    json_file_handler.write(json.dumps(data_dict, indent = 4))