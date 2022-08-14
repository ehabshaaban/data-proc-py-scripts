"""
make_me_testcases is generating tests based all on combination parameters for testing payment services
"""

import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

BANK_TYPEs = ["h2h"]
BANK_SERs = ["Acquirer"]
BANK_NAMEs = ["UNB"]
BANK_PROs = ["123"]
BANK_PRODUCTs = ["Visa Classic"
,"Visa Gold"
,"MasterCard Platinum"
,"MasterCard Standard"
,"Prepaid"
]
BANK_FLOWs = ["on us"
,"Off us"
]
TRANSACTION_CODES = ["53 - ATM Payment Credit" 
,"52 - ATM Payment Debit" 
,"51 - ATM Payment Pass" 
,"10 - Withdrawal" 
,"40 - Transfer" 
,"30 - Balance inquiry" 
,"20 - Deposit" 
,"50 - Payment"
,"110 - Purchase" 
,"177 - POS Payment Credit" 
,"176 - POS Payment Debit" 
,"137 - POS Transfer" 
,"118 - Purchase With Cashback "
]
ENTRY_MODE = ["Manual Entry"
,"Chip"
,"Mag"
]
EXPEC_RES_CODE = ["1 - Approved"
,"51 - Expired card"
,"59 - Insufficient funds"
,"67 - Invalid amount"
,"52 - Invalid card"
,"53 - Invalid PIN"
,"40 - Lost card"
,"62 - PIN tries limit was reached"
,"83 - PIN tries limit was exceeded"
,"41 - Stolen card"
,"Card expired"
,"Card Block"
,"Card Cancelled"
,"Terminal out of service"
]

excel = {'TC ID': [],
        'TC Name': [],
        'TC Description': [],
        'Precondition': [],
        'Test Data': [],
        'Test Steps': [],
        'Expected Results': [],
        }
#df = pd.DataFrame(excel, columns = ['TC ID', 'TC Name', 'Precondition', 'Test Data', 'Test Steps', 'Expected Results'])
excel = []
df = pd.DataFrame()

count = 0
automated_tc_list = []
def cooking_machine():
    global count
    global automated_tc_list
    global df
    print("Start[TCs]")
    for bnk_type in BANK_TYPEs:
        for bnk_ser in BANK_SERs:
            for bnk_name in BANK_NAMEs:
                for bnk_pro in BANK_PROs:
                    for bnk_product in BANK_PRODUCTs:
                        for bnk_flow in BANK_FLOWs:
                            for transaction in TRANSACTION_CODES:
                                for mode in ENTRY_MODE:
                                    for res_code in EXPEC_RES_CODE:
                                        count+=1
                                        tc = str(count) + "\t" + bnk_type + "\t" + bnk_ser + "\t" + bnk_name + "\t" + bnk_pro + "\t" +  bnk_product + "\t" + bnk_flow + "\t" + transaction + "\t" + mode + "\t" + res_code
                                        #print(tc)
                                        excel.append(
                                            {'TC ID' : str(count),
                                            'TC Name' : bnk_name+"_"+bnk_pro+"_"+bnk_type+"_"+bnk_ser+"_"+bnk_product+"_"+bnk_flow+"_"+transaction+"_"+mode+"_"+res_code,
                                            'TC Description' : "Validate "+ transaction[5:]+" transaction code for "+bnk_name+" bank using protocol "+bnk_pro+" from "+bnk_product+" card with flow "+bnk_flow,
                                            'Precondition' : "* Transaction from "+bnk_name+" bank\n"+"* Protocol "+bnk_pro+"\n"+"* Card type "+bnk_product+"\n"+"* Flow "+bnk_flow+"\n"+"* Transaction type: "+transaction[5:]+"\n"+"* Entry mode: "+mode,
                                            'Test Data' : "* Bank "+bnk_name+"\n"+"* Protocol "+bnk_pro+"\n"+"* Card "+bnk_product,
                                            'Test Steps' : "* Prepare "+bnk_ser+" service\n"+"* Insert card with type "+bnk_product+"\n"+"* Enter PIN Code\n"+"* Initiate the "+transaction[5:]+"\n   request by sending the corresponding iso format",
                                            'Expected Results' : "Response code should be "+res_code+" code"}
                                        )
    
    df = pd.DataFrame(excel)
    return df , count

if __name__ == "__main__":
    cooking_machine()
    print(len(df.index), count)
    print(df.head())    
    df.to_excel("/home/ehab/Desktop/script/tc_für_heute.xlsx")