#!/usr/bin/env python3

#Query the miRNA database through the browser using a cgi program

import pymysql
import cgi
import cgitb
#next is for packaging the output into json format
import json

#the next line is useful for debugging
#it causes errors during execution to be sent back to the browser
cgitb.enable()

#this program does NOT generate html
#instead, it queries the miRNA database and returns the results
#to be formatted by the calling AJAX function



#retrieve input data from the web server
form = cgi.FieldStorage() 

#next line is always required as first part of http output
print("Content-type: text/html\n")

if (form):
    #get submitted values
    mRNA1 = form.getvalue("miRNA_name","") #second string is default if nothing is returned
    RNA_seq = form.getvalue("RNA_seq","")

    ##### for chart #####
    #if there was a gene name as input
    if (mRNA1 != ""):
        #establish the connection on bioed
        try:
            connection = pymysql.connect(
                host='bioed.bu.edu', 
                user='preshita',
                password='bf768preshita', 
                db='miRNA',
                port = 4253) 
        except pymysql.Error as e: 
            print(e)
           
        # get cursor
        cursor = connection.cursor()

        # define the query
        query1 = """
        select score
        from miRNA join targets using (mid)
        where name regexp '%s'
        """%(mRNA1)

        #execute query
        try: 
            cursor.execute(query1)
        except pymysql.Error as e: 
            print(e)
    
        results = cursor.fetchall()
        plot_data = [['score']]
        for row in results:
            plot_data.append([row[0]])

        #format the output as json object
        print(json.dumps(plot_data))

    ##### for table #####
    if(RNA_seq != ""):
        #establish the connection on bioed
        try:
            connection = pymysql.connect(
                host='bioed.bu.edu', 
                user='preshita',
                password='bf768preshita', 
                db='miRNA',
                port = 4253) 
        except pymysql.Error as e: 
            print(e)
           
        # get cursor
        cursor = connection.cursor()

        # define the query
        query1 = """
        select name, seq
        from miRNA 
        where seq regexp '%s'
        """%(RNA_seq)

        #execute query
        try: 
            cursor.execute(query1)
        except pymysql.Error as e: 
            print(e)
    
        results = cursor.fetchall()


        #format the output as json object
        print(json.dumps(results))




