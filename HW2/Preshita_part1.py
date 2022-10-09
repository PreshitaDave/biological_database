
# import the PyMySQL module
import pymysql

# connecting Python to MySQL
connection = pymysql.connect(host="bioed.bu.edu",
                             db="preshita",          
                             user="preshita",
                             passwd="bf768preshita",
                             port=4253, 
                             local_infile=1, autocommit=True)

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