#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
# import the PyMySQL module
import pymysql

#the next two lines are useful for debugging
#they cause errors during execution to be sent back to the browser
import cgitb
cgitb.enable()
#the next line gives us a convenient way to insert values into strings
from string import Template 

#retrieve form data from the web server
form_str="""
<html>
    <body>
        <h1>miRNAs targeting 2 genes</h1>
        <form name="form" action="https://bioed.bu.edu/cgi-bin/students_22/preshita/preshita_doubleSearch.py" method="get">
        <p>
            This page will allow the user to query the miRNA database with the names of two genes, and return a list of all miRNAs that target both genes.<br>
            
            Input the names of the two genes below in the text boxes:<br>
            
            Some examples of genes that can used to query are: A1CF and AFF4, A1CF and A2LD1...<br>
        </p>
        <!-- Name as text -->
        Gene 1: 
        <input type="text" name="gene1" > Ex: AAMP, A1CF ...
        <br>
        Gene 2: 
        <input type="text" name="gene2" > Ex: A2LD1, AFF4 ...
        <br>            
        <!-- Submit Button-->
        <button input type="Submit" > Submit </button>
        </form>
    </body>
</html>   
    """
print("Content-type: text/html\n")
print("%s" %form_str)


# connecting Python to MySQL
connection = pymysql.connect(host="bioed.bu.edu",
                            db="miRNA",          #note the database name
                            user="preshita",
                            passwd="bf768preshita",
                            port=4253)

# getting cursor out of connection
cursor = connection.cursor()

form = cgi.FieldStorage(keep_blank_values=True)

if(form):
    #get individual values from the form data
    #use getvalue when there is only one instance of the key in the query string
    gene1 = form.getvalue("gene1") 
    gene2 = form.getvalue("gene2") 
 
    if len(gene1) != 0 and len(gene2) != 0:
        # getting summary
        query01 = """SELECT count(*)
        from gene
        where name regexp '%s';
        """%(gene1)
        try:
            cursor.execute(query01)
        except pymysql.Error as e:
            print(e)
        
        result01=cursor.fetchall()
        query02 = """SELECT count(*) as ''
        from gene
        where name regexp '%s';
        """%(gene2)       
        try:
            cursor.execute(query02)
        except pymysql.Error as e:
            print(e)
        result02=cursor.fetchall()

        if result01[0][0] == 1 and result02[0][0] == 1:

            query1 = """SELECT count(m2.name) as ""
            FROM gene g2 JOIN targets t2 USING(gid) Join miRNA m2 USING(mid)
            Join (SELECT mid, gid as g1_gid, g1.name as g1_name, m1.name as m1_name, score as t1_score
            FROM gene g1 JOIN targets t1 USING(gid) Join miRNA m1 USING(mid)) gene1 USING(mid)
            WHERE g1_name = '%s' AND g2.name = '%s';
            """%(gene1,gene2)


    # Execute the mySQL query
            try:
                cursor.execute(query1)
            except pymysql.Error as e:
                print(e)

#fetching the results
            result1=cursor.fetchall()

#printing the results
            summary = Template("""
            <html>
            <body>
            <p> Gene ${gene1} and gene ${gene2} are both targeted by ${result1} miRNAs.</p>
            </body>
            </html>
            """)
            print(summary.safe_substitute(gene1=gene1, gene2=gene2,result1=result1[0][0]))

    # getting table rows

            query = """SELECT m2.name as miRNA, t1_score as gene1_TargetScore, t2.score as gene2_TargetScore
            FROM gene g2 JOIN targets t2 USING(gid) Join miRNA m2 USING(mid)
            Join (SELECT mid, gid as g1_gid, g1.name as g1_name, m1.name as m1_name, score as t1_score
            FROM gene g1 JOIN targets t1 USING(gid) Join miRNA m1 USING(mid)) gene1 USING(mid)
            WHERE g1_name = '%s' AND g2.name = '%s';
            """%(gene1,gene2)


        # Execute the mySQL query
            try:
                cursor.execute(query)

            except pymysql.Error as e:
                print(e)
#fetching results from query

            results = cursor.fetchall()

        #create table
        #start with non-variable part 


            table_template = """
                <html>
                    <head>
                        <title>My program's response</title>
                    </head>
                    <body>

            <style type="text/css">
            .tg  {border-collapse:collapse;border-spacing:0;}
            .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
            overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
            font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg .tg-0lax{text-align:left;vertical-align:top}
            </style>

            <table class="tg">
                <thead>
                    <tr>
                        <th>miRNA</th>
                        <th>Target Score %s</th>
                        <th>Target Score %s</th>
                    </tr>
                </thead>
                <tbody>
            """%(gene1,gene2)

            #now add rows to the table, using string substitution
            for row in results:
                table_template += """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                    </tr>
                """ % (row[0],row[1],row[2])

        #close table
            table_template += """  
                </tbody>
            </table>
            </body>
            </html>
            """
        # print("Content-type: text/html\n")
            print(table_template)

        else:
        #no form data
            form_wrong="""
            <html>
                <head>
                    <title>My program's response</title>
                </head>
                <body>
                    <p>
                    You didn't send the correct genes!
                    </p>
                </body>
            </html> 
            """
    # print("Content-type: text/html\n")
            print("%s" %form_wrong)

    else:
    #no form data
        form_wrong="""
        <html>
            <head>
                <title>My program's response</title>
            </head>
            <body>
                <p>
                One or both of the genes are missing!
                </p>
            </body>
        </html> 
        """
# print("Content-type: text/html\n")
        print("%s" %form_wrong)



    cursor.close()
    connection.close()








