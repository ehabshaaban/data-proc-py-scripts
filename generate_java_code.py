import pandas as pd

def generate_data_variables_and_enums(file_path, sheet_number):
    global header_list
    df = pd.read_excel(file_path,sheet_number)
    pd.options.display.max_rows = len(df.columns)
    header_values = df.columns.to_series().reset_index(drop=True)
    header_list = list(header_values)
    enum_list =[]
    data_list = []

    for i in range(len(header_list)):
        enum_variable = header_list[i]
        enum_variable = "public static final String " + header_list[i].upper() + " = " + '"' + header_list[i] + '"' + ";"
        enum_list.append(enum_variable)
        data_variable = header_list[i]
        data_variable = "private String " + header_list[i] + ";"
        data_list.append(data_variable)

    f=open('enum_variables.txt','w')
    for ele in enum_list:
        f.write(ele+'\n')
    f.close()

    f2=open('java_variables.txt','w')
    for ele in data_list:
        f2.write(ele+'\n')
    f2.close()

def generate_dynamic_java_lines():
    dynamic_list = []
    for element in range(len(header_list)):
        basic_line = "				"+MODULE_INSTANCE+"[i].setTestCaseID((data.get(i)).get(header.indexOf("+MODULE_ENUM+"."+header_list[element].upper()+")))"
        dynamic_list.append(basic_line)
    return dynamic_list

def generate_read_function(MODULE_DATA,MODULE_INSTANCE,MODULE_ENUM):
    file_lst = open('template_function.txt', "r").readlines()
    for i in range(len(file_lst)):
        if 'MODULE_DATA' or 'MODULE_INSTANCE' or 'MODULE_ENUM' in file_lst[i]:
            file_lst[i] = file_lst[i].replace('MODULE_DATA', MODULE_DATA)
            file_lst[i] = file_lst[i].replace('MODULE_INSTANCE', MODULE_INSTANCE)
            file_lst[i] = file_lst[i].replace('MODULE_ENUM', MODULE_ENUM)

        if i == 14:
            java_lines_lst = generate_dynamic_java_lines()
            for elem in reversed(java_lines_lst):
                file_lst.insert(14, elem)

    f3=open('read_function.txt','w')
    for ele in file_lst:
        f3.write(ele+'\n')
    f3.close()    
                

if __name__ == "__main__":

    """The following variables are for generating data variables in Data class & enum variables in Enum class
       Generated text files are enum_variables.txt & java_variables.txt"""
    
    """//\\//\\//\\//\\//\\//\\//\\//\\//\\"""
    # Data sheet path
    file_path = "/home/ehab/Desktop/NBKE/nbkautomation/NBKAutomationIE/resources/TestData/Trade/LG_Issue_Operative/Trade_LG_Amend_Operative.xls"
    # Sheet number
    sheet_number = 'Sheet1'
    """//\\//\\//\\//\\//\\//\\//\\//\\//\\"""
    generate_data_variables_and_enums(file_path,sheet_number)





    
    """The following variables are for generating read function
       Generated text file is read_function.txt"""
    
    """//\\//\\//\\//\\//\\//\\//\\//\\//\\"""
    # Data class name
    MODULE_DATA = "TradeLGAmendOperativeData"
    # Instance variable from MODULE_DATA object
    MODULE_INSTANCE = "lgAmendOperative"
    # Enum class name
    MODULE_ENUM = "TradeLGAmendOperativeEnum"
    """//\\//\\//\\//\\//\\//\\//\\//\\//\\"""
    generate_read_function(MODULE_DATA,MODULE_INSTANCE,MODULE_ENUM)