#!/usr/bin/python
import math
import sys
import requests
import os
import sqlite3
from pprint import pprint

# get command line argument
numberOfRecords = int(sys.argv[1])

# set security token
token = os.getenv('GITHUB_TOKEN', '481e89ae7e660063c923b2392b6298864ffd3318')

# Calculate number of pages (API Max 100 records per page) and per_page
pages = math.ceil(numberOfRecords / 100);

# lastPerPage is the reminder divided by 100.
lastPerPage = numberOfRecords % 100
perPage = 100
if numberOfRecords < 100:
    perPage = lastPerPage
# github api default any per_page size larger then 100 to 100
if numberOfRecords % 100 == 0:
   lastPerPage = numberOfRecords

# Open SQLite3 database connection and create table
conn = sqlite3.connect('gitusers.db')
c = conn.cursor()

# Doping users table if already exists
c.execute("DROP TABLE IF EXISTS users")
print("Table dropped... ")

#Commit changes in the database
conn.commit()

# Creatse users table if not already exists
c.execute("CREATE TABLE IF NOT EXISTS users ( git_id varchar(3), git_username varchar(50), git_avatar_url varchar(200), git_type varchar(10), git_profile_url varchar(200)  )")


# API query and Insert into SQLLite Databaase
for page in range(pages):
    if page!=0:
        recordSince = lastGitID
    else:
        recordSince = 0

    if page+1 == pages:
        query_url = f"https://api.github.com/users?since={recordSince}&per_page={lastPerPage}"
    else:
        query_url = f"https://api.github.com/users?since={recordSince}&per_page={perPage}"

    # print ("query_url:", query_url )

    params = {
        "state": "open",
    }
    headers = {'Authorization': f'token {token}'}

    r = requests.get(query_url, headers=headers, params=params)
    # pprint(r.json())
    users = r.json()
    length=len(r.json())
    # print ("Number of Records: ", length)

    for user in users:
        c.execute("insert into users values (?, ?, ?, ?, ?)",
        [ user['id'], user['login'], user['avatar_url'], user['type'], user['html_url'] ])
    lastGitID = user['id']
    conn.commit()
    print ("Number of Records insert to database: ", length)
    print ("last git_id: ", lastGitID)

conn.close()
