import pymysql
conn=pymysql.connect(host="localhost",user="root",db="mppython")
print("connection established")
mycursor=conn.cursor()
#que="create table user_info(name varchar(50),age int(3))"
que="insert into user_info(name,age)values('Ram',22)"
#que="update user_info set name='Shyam' where name='Ram'"
mycursor.execute(que)
conn.commit() # to save the result(data) of execution of any query
#print("table Created Successfully")
print("Data Stored successfully")
#print("Data Updated  successfully")
mycursor.close()
conn.close()