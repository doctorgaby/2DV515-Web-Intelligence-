# #import csv module
# import csv


# #open users file(usernames and user ids)
# with open('users.csv', 'r') as csv_file:
# 	readCSV = csv.reader(csv_file, delimiter= ';')

# 	next(readCSV)

# 	for line in readCSV:
# 		print(line)


# #open ratings file(user ids, movie, ratings)
# with open('ratings.csv', 'r') as csv_file:
# 	readCSV2 = csv.reader(csv_file, delimiter= ';')

# 	next(readCSV2)

# 	for line in readCSV2:
# 		#print(userId)
# 		mydict = {line[0]:line[1]}
# 		print(mydict)

#another method
import csv
from collections import defaultdict

joined_data = dict()
column_map = defaultdict(list)

with open('users.csv') as f1, open('ratings.csv') as f2:
    kh = next(f1).strip()
    vh = next(f2).strip()
    key_headers = kh.split(';')
    value_headers = vh.split(';')

    [column_map[k].append(v) for k in key_headers[1:] for v in value_headers[1:] if v.startswith(k)]
    joined_data['UserID'] = dict(column_map)

    key_list = list(csv.DictReader(f1, fieldnames=key_headers))
    value_list = list(csv.DictReader(f2, fieldnames=value_headers))

for kl, vl in zip(key_list, value_list):
    inner = {}
    for key, value_list in column_map.items():
        if kl[key]:
            inner[kl[key]] = [vl[el] for el in value_list]

    joined_data[kl['UserID']] = inner
    print(joined_data[kl['UserID']])