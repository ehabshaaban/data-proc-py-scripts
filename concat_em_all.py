"""
concat_em_all is reading a directory `folder_path`
directory has automatically generated excel reports
it will concat all data and write it in new file
"""

from datetime import datetime
import pandas as pd
import os

folder_path = ""
report_name = "output-report-"+str(datetime.now())+".xlsx"
files = os.listdir(folder_path)

def get_path_to_file(folder_path, files):
    
    path_to_file_list = []
    for f in files:
        path_to_file = folder_path + f
        path_to_file_list.append(path_to_file)
    return path_to_file_list

def get_it_boy(path_to_file_list):
    
    df = pd.DataFrame()
    for ptf in path_to_file_list:
        df = df.append(pd.read_excel(ptf), ignore_index=True)
    return df.to_excel(report_name) 

if __name__ == "__main__":
    get_it_boy(get_path_to_file(folder_path, files))