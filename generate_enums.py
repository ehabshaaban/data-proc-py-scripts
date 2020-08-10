import pandas as pd

file_path = "/home/ehab/Desktop/NBKE/nbkautomation/NBKAutomationIE/resources/TestData/Trade/Import_DC_Amend/Import_DC_Amend.xls"
df = pd.read_excel(file_path,'Sheet1')
pd.options.display.max_rows = len(df.columns)
header_values = df.columns.to_series().reset_index(drop=True)
header = list(header_values)
#del header[-1]
for i in range(len(header)):
    header[i] = "public static final String " + header[i].upper() + " = " + '"' + header[i] + '"' + ";"

f=open('enum_variables.txt','w')
for ele in header:
    f.write(ele+'\n')
f.close()