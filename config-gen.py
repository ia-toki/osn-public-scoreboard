import csv
import json

with open('contestants.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    contestants = {}
    for row in csv_reader:
        if row[0] == 'jid':
            continue

        contestants[row[0]] = {
            'username': row[1],
            'name': row[2],
            'school': row[3],
            'province': row[4],
        }

    print('var config = ' + json.dumps({
        'serverUrl': 'http://localhost:9144/serve',
        'refreshIntervalInMs': 5000,
        'contestants': contestants
    }, indent=4, separators=(',', ': ')))
