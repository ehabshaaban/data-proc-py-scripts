import pandas as pd

def generate_data_variables_and_enums(file_path, sheet_number):
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

    def generate_read_function():
        # template_file = open("template_function.txt", "r")
        # for aline in tempslate_file:
        #     pass
            # values = aline.split()
            # print(values)
        # template_file.close()
        print("Hello from a function")

if __name__ == "__main__":
    """The following variables are for generating data variables in Data class & enum variables in Enum class"""
    """Generated text files are enum_variables.txt & java_variables.txt"""
    
    # Data sheet path
    file_path = "/home/ehab/Desktop/NBKE/nbkautomation/NBKAutomationIE/resources/TestData/Trade/Import_DC_Amend/Import_DC_Amend.xls"
    # Sheet number
    sheet_number = 'Sheet1'
    generate_data_variables_and_enums(file_path,sheet_number)



    """The following variables are for generating read function"""
    """Generated text file is read_function.txt"""
    
    # Data class name
    MODULE_DATA = "MODULE_DATAMODULE_DATA"
    # Instance variable from MODULE_DATA object
    MODULE_INSTANCE = "MODULE_INSTANCEMODULE_INSTANCE"
    # Enum class name
    MODULE_ENUM = "MODULE_ENUMMODULE_ENUM"
    generate_read_function()
