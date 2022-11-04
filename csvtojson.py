import json
import csv
import hashlib

with open('hngi9csv.csv', 'r') as my_csv:
    read_csv = csv.reader(my_csv, delimiter=',')
    next(read_csv)

    data = [c for c in read_csv]
    print(data)





















'''
def convert_csv_to_json(csv_filepath, json_filepath):
   
    data = {'format': 'CHIP-0007'}
    with open(csv_filepath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['Filename']
            data[key] = rows

    with open(json_filepath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    sha256_hash = hashlib.sha256()
    with open(json_filepath, "rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())



csv_file = r'teamclutch.csv'
json_path = r'json_dest.json'
convert_csv_to_json(csv_file, json_path)
'''