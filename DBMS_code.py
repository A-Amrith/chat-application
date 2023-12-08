# Author: Amrith A
# Python/SQL code for Library management system. The code creates a database
# and 2 tables for metadata and messages , provides functions for adding and deletion of book entries.

# Importing module
from typing import Tuple

import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4CSproj!",
    database="chat_app_database",
)
cursor = mydb.cursor();
cursor.execute("CREATE TABLE IF NOT EXISTS METADATA(USERNAME VARCHAR(255), HASHEDPASSWORD VARCHAR(255), DISPLAYNAME VARCHAR(255),UNIQUEUSERID VARCHAR(255))");

cursor2 = mydb.cursor();
cursor2.execute("CREATE TABLE IF NOT EXISTS MESSAGES(UNIQUEUSERID VARCHAR(255), CHATROOMID VARCHAR(255),UMESSAGE VARCHAR(1500))");
# Function to add a record to the metadata table
def add_record_to_table_METADATA (username,hashedpassword,displayname,uniqueuserid):
    print("Enter the strings username,hashedpassword,displayname,uniqueuserid (in that order)")
    sql = "INSERT INTO METADATA(USERNAME, HASHEDPASSWORD, DISPLAYNAME, UNIQUEUSERID) VALUES (%s, %s, %s,%s)"
    val = (username, hashedpassword, displayname,uniqueuserid)
    cursor.execute(sql, val)
    mydb.commit()

# Function to delete a record from the metadata table
def delete_record_from_table_METADATA (duniqueuserid):
    print("Enter uniquieuserid")
    dsql = "DELETE FROM METADATA WHERE UNIQUEUSERID = %s"
    dval = (duniqueuserid)
    cursor.execute(dsql, dval)
    mydb.commit()
# Function to add a record to the messages table
def add_record_to_table_MESSAGES (chatroomid,message,uniqueuserid):
    print("Enter the strings chatroomid,message,uniqueuserid (in that order)")
    sql = "INSERT INTO MESSAGES(CHATROOMID, MESSAGE,UNIQUEUSERID) VALUES (%s, %s, %s)"
    val = (chatroomid,message,uniqueuserid)
    cursor2.execute(sql, val)
    mydb.commit()
# Function to delete a record from the messages table
def delete_record_from_table_METADATA (dchatroomid,dmessage,duniqueuserid):
    print("Enter uniquieuserid,chatroomid,message for deletion (in that order)")
    dsql = "DELETE FROM MESSAGES WHERE UNIQUEUSERID = %s AND CHATROOMID = %s AND UMESSAGE = %s "
    dval = (duniqueuserid,dchatroomid,dmessage)
    cursor2.execute(dsql, dval)
    mydb.commit()
