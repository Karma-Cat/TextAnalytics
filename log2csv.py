#!/usr/bin/env python3

import re
import operator
import csv

def dict_build():
  error = {}
  user_stat = {}
  spis = []

  with open('syslog.log', 'r') as f:
    for line in f:
      spis += re.findall(r': ([A-Z]*) ([A-Za-z \']*).* \(([a-zA-Z0-9.]*)\)', str(line))

  for i in spis:
    if i[0] == "ERROR":
      if i[1] not in error:
        error[i[1]] = 1
      else:
        error[i[1]] += 1


  for i in spis:
    if i[0] == "ERROR":
      if i[2] not in user_stat:
        user_stat[i[2]] = {"ERROR": 1,"INFO": 0}
      else:
        user_stat[i[2]][i[0]] += 1
    elif i[0] == "INFO":
      if i[2] not in user_stat:
        user_stat[i[2]] = {"ERROR": 0,"INFO": 1}
      else:
        user_stat[i[2]][i[0]] += 1

  error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
  user_stat = sorted(user_stat.items())

  return(error, user_stat) 

def to_csv(user_stat, error):

  with open("user_statistics.csv", "w") as user_csv:
    writer = csv.writer(user_csv)
    writer.writerow(["Username", "INFO", "ERROR"])
    for item in user_stat:
      user, log_type = item
      line = [user, log_type["INFO"], log_type["ERROR"]]
      writer.writerow(line)
  with open("error_message.csv", "w") as error_csv:
    writer = csv.writer(error_csv)
    writer.writerow(["Error", "Count"])
    writer.writerows(error)

error, user_stat = dict_build()
to_csv(user_stat, error)