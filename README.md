# scripts4data
# In this repo scripts for data analytics

###log2csv.py 
This script drag information from syslog.log file (login, log type, description) and count number of this events by login and by description.
syslog.log sample:
 May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
 Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)

###null_killer.py 
This script read csv file, convert all 'null' values to '0', and rewrite old file.
You can choose as many files as you want
