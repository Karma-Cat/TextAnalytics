import os
import logging
import re

def time_it(func):
"""Time messument Wrapper"""

    import time
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("Execution time: {} sec.".format(end-start)) 
    return inner            

def check_path(func):
"""Input checks(path format) Wrapper for file_store function"""

    def inner(func):
        
    return func if re.findall(r'(\\)$', args) else logging.error("Format error. Backslash is needed in the end of path")
        
@time_it    
@check_path
def file_store(path):
"""Check files in folder and start json or html reader function"""

    for file in os.listdir(path):
    exten = re.findall(r'\.([a-zA-Z]*)$', file)
    file_path = path + file
        if exten == "json":
            data = json_reder(file_path)
        elif exten == "html":
            data = html_reader(file_path)
        else:
            logging.error("Extension error. This file is not json or html {}".format(file))
            pass 

def json_reder(path):
"""Read json file("data" hash key) and give value"""

    import json
    
    with open(path) as json_file:
        data = json.load(json_file)
    pass

def html_reader():
"""Read html file and give value"""
    pass

if __name__ == "__main__":
