import os
import logging
import re
import pandas

def time_it(func):
#"""Time messument Wrapper"""

    import time

    def inner():
	    start = time.time()
	    func()
	    end = time.time()
	    print("Execution time: {} sec.".format(end-start))
    return inner 
	
#def check_path(func):
#"""Input checks(path format) Wrapper for file_store function"""
#
#    def inner(*args, **kwargs):
#        
#        return func if not re.findall(r'(\\)$', args) else logging.error("Format error. Backslash is needed in the end of path")
        
		
def paths_maker():
#"""Check files in folder and start json or html reader function"""

    path = input()

    data = os.listdir(path)
	
    json_path = []
    html_path = []
    
    for i in data:
	    if len(i.split(".", 2))>2 and i.split(".", 2)[2] == "json":
	        json_path.append(path + "\\" + i)
	    elif i.split(".", 2)[1] == "html":
	        html_path.append(path + "\\" + i)
      else:
          logging.error("Extension error. This file is not json or html {}".format(i))
	
    return json_path, html_path
	
def json_rw(json_path):
#"""Read json file("data" hash key) and give value"""
	
    import json
    json_path = json_path
    json_data = []
    
    for path in json_path:
	    with open(path) as json_file:
	        json_data.append((json.load(json_file), json_path))
    
    json_data.append(('Data', 'Path')) 
    
    path = re.sub(r"[a-z]*$", "", json_path[-2])
    path = path + "xlsx"
    
    open(path, "w")
    
    df = pd.DataFrame(json_data[:-1], index = None, columns = json_data[-1])
    df.to_excel(path, sheet_name = 'json')
    
    return logging.info("Excel successfully created {}.excel".format('json`s'))
	
def html_rw(html_path):
	#"""Read html file and give value"""
    
    html_paths = html_path
    
    for html_path in html_paths:
	
	    html_data = []
    
	    df = pd.read_html(html_path , encoding = "utf-8")
	
	    for number in range(len(df[4]['Texts'])):
	        text = df[4]['Texts'][number]
	        time = df[4]['Duration (sec)'][number]  
	        RTF = df[4]['RTF'][number]
	        WER = df[4]['WER%'][number]
	        html_data.append((text, time, RTF, WER))
    
	    html_data.append(('Text', 'Time', 'RTF', 'WER'))
	
	    path = re.sub(r"[a-z]*$", "", html_path)
	    path = path + "xlsx"
	
    
	    open(path, "w")
    
	    df_w = pd.DataFrame(html_data[:-1], index = None, columns = html_data[-1])
	    df_w.to_excel(path, sheet_name = 'html')
	
	    name = re.findall(r'\\([0-9A-Za-z_.-]*)\.[a-z]*$', path)
	    logging.info("Excel successfully created {}.excel".format(name[0]))
	
    return logging.info("Excels successfully created ")
	
	
@time_it
def main():
    json_path, html_path = paths_maker()
    html_rw(html_path)
    json_rw(json_path)
	
if __name__ == "__main__":
    main()