import pandas as pd
import numpy as np
import itertools


df = pd.read_excel("/home/ehab/Downloads/NNII.xlsx", header=None)

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
    rows_meta_idx = list(df[1][df[1] == data_string].index)
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

def glamour_testcases():
    df_data = df_wo_app_header[1].values
    for i in df_data:
        if str(i) == "nan":
            print(i)

    # TODO: ^ Update the N/A validation list with other cases

if __name__ == "__main__":
    save_app_header()
    drop_app_header()
    glamour_testcases()
    #print(make_na_list("n/a"))