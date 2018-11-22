#import csv module
import csv
import itertools


#open users file(usernames and user ids)
with open('users.csv', 'r') as csv_users, open('ratings.csv', 'r') as csv_ratings:
	readCsvUsers = csv.reader(csv_users, delimiter= ';')
	readCsvRatings = csv.reader(csv_ratings, delimiter= ';')
	next(readCsvUsers)
	next(readCsvRatings)
	#mydict_ratings = dict(readCsvUsers)
	#print(mydict_ratings)
	mydict = {}
	mydict2 = {}
	mydict3 = {}
	mydict4 = {}


	for line_users in readCsvUsers:
		for line_ratings in readCsvRatings:
			if line_users[1] in line_ratings[0]:
				mydict = {line_ratings[1]:line_ratings[2]}
			mydict2.update(mydict)
#mydict2 holds all movies for the first iteration: correct line_users but only for the first set
		mydict3 = {line_users[0] : mydict2}
		#print(mydict3)
		mydict4.update(mydict3)
	print(mydict4)



		# 	mydict = ({line_users[0]:{line_ratings[1]:line_ratings[2]}})
		# for line_ratings in readCsvRatings:
		# 	if line_users[1] in line_ratings[0]:
		# 		if mydict == {}:
		# 			mydict = ({line_users[0]:{line_ratings[1]:line_ratings[2]}})
		# 		else:
		# 		  mydict = ({line_ratings[1]:line_ratings[2]}})
		# 		print(mydict)


	# for line_ratings in readCsvRatings:
	# 	for line_users in line
	# 	if line_users[1] == :
	# 		print("i work")
	# 		mydict = {line_ratings[1]:line_ratings[2]}
	# 		mydict2.update(mydict)
	# print(mydict2)

	# mydict3 = {'Lisa' : mydict2}
	# print(mydict3)

	# for line_users in readCsvUsers:
	# 	mydict3 = {line_users[0] : mydict2}
	# 	for line_ratings in readCsvRatings:
	# 	#print(userId)
	# 	mydict = {line_ratings[1]:line_ratings[2]}
	# 	mydict2.update(mydict)
	# print(mydict2)

	#print(mydict)

	# for line_users in readCsvUsers:
	# 	for line_ratings in readCsvRatings:
	# 		if line_users[1] in line_ratings[0]:
	# 			mydictline_ratings] = dict({line_users[0]:{line_ratings[1]:line_ratings[2]}})
	# 			print(mydict)
	# for line_ratings in readCsvRatings:
	# 	for line_users in readCsvUsers:
	# 		if line_users[1] == line_ratings[0]:
	# 			mydict.update({line_users[0]:{line_ratings[1]:line_ratings[2]}})
	# 			print(mydict)


#another method
# import csv
# from collections import defaultdict

# joined_data = dict()
# column_map = defaultdict(list)

# with open('users.csv') as f1, open('ratings.csv') as f2:
#     kh = next(f1).strip()
#     vh = next(f2).strip()
#     key_headers = kh.split(';')
#     value_headers = vh.split(';')

#     [column_map[k].append(v) for k in key_headers[1:] for v in value_headers[1:] if v.startswith(k)]
#     joined_data['UserID'] = dict(column_map)

#     key_list = list(csv.DictReader(f1, fieldnames=key_headers))
#     value_list = list(csv.DictReader(f2, fieldnames=value_headers))

# for kl, vl in zip(key_list, value_list):
#     inner = {}
#     for key, value_list in column_map.items():
#         if kl[key]:
#             inner[kl[key]] = [vl[el] for el in value_list]

#     joined_data[kl['UserID']] = inner
#     print(joined_data[kl['UserID']])