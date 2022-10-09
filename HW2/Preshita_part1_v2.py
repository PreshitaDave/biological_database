
# import the PyMySQL module
import pymysql
import sys

# get arguments from system argument list
dtbs = sys.argv[1]
usrnm  = sys.argv[2]
pswd = sys.argv[3]


# to print program usage when called with no parameters
# note that sys.arv[0] is the program name
# if len(sys.argv) != 4: #number of parameters +1 for program name
#    print ("Usage is: %s database username password" % sys.argv[0])
#    sys.exit(0)

# connecting Python to MySQL
connection = pymysql.connect(host="bioed.bu.edu",
                             db=dtbs,          
                             user=usrnm,
                             passwd=pswd,
                             port=4253, 
                             local_infile=1)

# getting cursor out of connection
cursor = connection.cursor()

#part a. sql 

try:
    cursor.execute("""drop table if exists Pathways;""")
except pymysql.Error as e:
    print(e)

query="""create table Pathways(
path_id integer not null, 
pathname varchar(100) not null, 
primary key(path_id)    
)engine=innodb;"""
try:
    cursor.execute(query)
except pymysql.Error as e:
    print(e)


#part b. sql 


query = """LOAD DATA LOCAL INFILE 'pathways.tab' INTO TABLE Pathways 
(path_id, pathname)"""
try:
    cursor.execute(query)
except pymysql.Error as e:
    print(e)