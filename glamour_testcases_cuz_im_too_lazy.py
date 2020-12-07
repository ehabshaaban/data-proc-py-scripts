import pandas as pd
import numpy as np
import itertools
from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)


df = pd.read_excel("/home/ehab/Downloads/NNII.xlsx", header=None)
df.columns = ['TestName', 'Data']
for i in df.index:
    if type(df["Data"][i]) is float:
        pass
    else:
        df["Data"][i] = df["Data"][i].title()

# generate n/a combination
def na_combination(l):
    yield from itertools.product(*([l] * 3))

def make_na_list(l):
    na_list = []
    for x in na_combination(l):
        na_list.append(''.join(x))
    return na_list

# save app header
rows_meta_idx = []
def save_app_header():
    global rows_meta_idx

    data_string = "Required Data Fields"
    rows_meta_idx = list(df['Data'][df['Data'] == data_string].index)
    row_meta_data = []

    app_list_obj = []
    for idx in rows_meta_idx:
        app_list_obj.append(df.loc[idx])
    return app_list_obj

# drop app header
df_wo_app_header  = None
def drop_app_header():
    global df_wo_app_header 

    df_wo_app_header = df.drop(index=rows_meta_idx)

def glamour_testcases_cuz_im_too_lazy():
    
    # handel delete test cases
    nan_data_ser = (df_wo_app_header.Data.isnull())
    nan_testcase_ser = df_wo_app_header.loc[nan_data_ser, 'TestName']

    for nan_testcase_idx in nan_testcase_ser.index:
        updated_nan_testcase = "Delete " + nan_testcase_ser[nan_testcase_idx].title() + " Feature"
        nan_testcase_ser[nan_testcase_idx] = updated_nan_testcase
        df_wo_app_header.at[nan_testcase_idx, "TestName"] = nan_testcase_ser[nan_testcase_idx]

    # handel other test cases
    data_ser = (df_wo_app_header.Data.notnull())
    testcase_ser = df_wo_app_header.loc[data_ser, 'TestName']
    
    for testcase_idx in testcase_ser.index:
        if type(testcase_ser[testcase_idx]) is not float:
            updated_testcase = "Setup " + testcase_ser[testcase_idx].title() + " Feature"
            testcase_ser[testcase_idx] = updated_testcase
            df_wo_app_header.at[testcase_idx, "TestName"] = testcase_ser[testcase_idx]

    # glowing it all back together
    for row in df_wo_app_header.index:
        df.at[row, "TestName"] = df_wo_app_header["TestName"][row]
    
    # fill nan empty cells in 'Data' with value n/a
    df["Data"].fillna("n/a", inplace = True)
    
# save DF into excel
def save_df(df_arg):
    df_arg.to_excel ('/home/ehab/glamour_testcases_cuz_im_too_lazy/sheet_'+str(timestamp)+'.xlsx', index = False, header=True)
    
if __name__ == "__main__":
    #save_app_header()
    drop_app_header()
    glamour_testcases_cuz_im_too_lazy()
    save_df(df)