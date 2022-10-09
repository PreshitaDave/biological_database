#!/usr/bin/env python
import pymysql
import sys

# START FUNCTION DEFINITIONS
def read_query(filename):
	# open the file
	with open(filename) as f:

	# initialize a variable (to store the query) as empty string
		data = ""
	
	# concatenate each line (remove \n) to the sequence
		for line in f:
			data += line.rstrip('\n') + ' '
	# close the file
	f.close()
	
	# return the sequence
	return data 
	
def execute_query(dtbs,usrnm,pswd,query):
	# connect to the database
	# connecting Python to MySQL
	connection = pymysql.connect(host="bioed.bu.edu",
                             db=dtbs,          #note the database name
                             user=usrnm,
                             passwd=pswd,
                             port=4253, 
                             local_infile=1, autocommit = 1)
		
	# get cursor
	cursor = connection.cursor()
	


	# Display columns
	


	
	# run query
	try:
		cursor.execute(query)

		
	except pymysql.Error as e:
		print(e)
	
	# fetch results 
	results = cursor.fetchall()

	# close the connection
	cursor.close()
	connection.close()
	
	# return the results
	return results

# FUNCTIONS FINISHED


# THIS IS THE MAIN BODY OF CODE THAT WILL CALL THE FUNCTIONS:

# get arguments from system argument list
dtbs = sys.argv[1]
usrnm  = sys.argv[2]
pswd = sys.argv[3]
filename = sys.argv[4]


# parse the query file using function read_query
query = read_query(filename)

# execute the query and get the results
executed = execute_query(dtbs,usrnm, pswd, query)

# print the results, one row at a time
for i in executed:
	print(i)