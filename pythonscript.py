#!/usr/bin/python3
# Install python pip if you dont have. 
# sudo apt install python3-pip
# once pip is installed, install python-mysql connector
# pip3 install pymysql
# Note: apt is the repository for linux(ubuntu) apps, pip/pip3 is the repository for python apps.
# pymysql is a python library to execute SQL commands.

#Create a database using mysql cli
#login to mysql --> mysql -u <username> -p
#give your password
#once logged in create a new database --> CREATE DATABASE ab1;
#after this step, you can use python to execute data read and write to table

import pymysql

conn =pymysql.connect(database="pars",user="parvathy",password="assignment3",host="localhost")
cur=conn.cursor()

#create database
#cur.execute("CREATE TABLE users(id int primary, name text, age int, gender text, address text);")

#to store user data

Username = "user1"
Userage = 25
Userstate = "Tamilnadu"

data={'Username':Username,'Userage':Userage,'Userstate':Userstate}
print(data)

# Saving data to DB
cur.execute("INSERT INTO userdata   (Username,Userage,Userstate) VALUES (%(Username)s,%(Userage)s,%(Userstate)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
cur.execute("SELECT * FROM userdata;")
#get one row
data1=cur.fetchone()
#get all rows
data2=cur.fetchall()

print(data1)
print(data2)
