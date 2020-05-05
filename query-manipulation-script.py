"""
--input box acts weird
  (maybe custom paste
  method needs to be
  implemented )
--hit alternative enter
  to generate inseration
  from input box
--build better graphics
--build text_manipulation


--to get number of records
ORACLE : Select Count(*) from T24.V_F_CONVERSION_PGMS;

JBASE : SELECT F.CONVERSION.PGMS

--to get number of columns 
ORACLE : SELECT count(*) FROM ALL_TAB_COLUMNS WHERE 
OWNER = 'T24' AND TABLE_NAME = 'V_F_CONVERSION_PGMS';

JBASE : SELECT F.STANDARD.SELECTION SYS.FIELD.NAME WITH FILE.NAME EQ 'CONVERSION.PGMS'


--to get specific column in specific record
ORACLE : Select PROGRAM_NAME from T24.V_F_CONVERSION_PGMS where RECID = 'G8'

JBASE: LIST F.CONVERSION.PGMS PROGRAM.NAME WITH @ID = 'G8'


"""

#Importing tKinter module
from tkinter import *
from tkinter import messagebox
import pyperclip

#Setting up GUI
win = Tk()
win.title("Query Generator")
win.resizable(0,0)

"""Needs More Unit Test Before Continue"""
def text_manipulation(jbase_value, oracle_value):
    global first_query
    global second_query
    print(oracle_value[0], oracle_value[:5])
    if oracle_value[:5] == 'FBNK_':
        print('FBNK')
        #Building 1st query_With FBNK
        key=oracle_value[:5]
        table_name = str(jbase_value).replace("_",".")
        prefix = str(key).replace("_",".")
        first_query_table = prefix+table_name
        first_query = "SELECT "+first_query_table
        #Building 2nd quey_With FBNK
        second_query = "SELECT F.STANDARD.SELECTION SYS.FIELD.NAME WITH FILE.NAME EQ '"+table_name+"'"
        
    elif oracle_value[:2] == 'F_':
        print('F')
        #Building 1st query_With F
        key=oracle_value[:2]
        table_name=str(jbase_value).replace("_",".")
        prefix=str(key).replace("_",".")
        first_query_table =  prefix+table_name
        first_query = "SELECT "+first_query_table
        #Building 2nd quey_With F
        second_query = "SELECT F.STANDARD.SELECTION SYS.FIELD.NAME WITH FILE.NAME EQ '"+table_name+"'"


def processing(text):
    global jbase_value
    global oracle_value
    jbase_pattern = "jbase file \[(.*?)\] with "
    oracle_pattern = "oracle file \[(.*?)]|\n"
    jbase_value = re.search(jbase_pattern, text).group(1)
    oracle_value = re.search(oracle_pattern, text).group(1)
    print("Enty.Get:",text)
    print("count:",len(text))
    print("Jbase:", jbase_value)
    print("Oracle:", oracle_value)
    entry.delete('1.0', END)
    text_manipulation(jbase_value=jbase_value, \
                      oracle_value=oracle_value)
    output1.config(text=first_query)
    output2.config(text=second_query)
    output3.config(text=oracle_value)
    output4.config(text=oracle_value)

def takingInput(*args):
    if len(entry.get("1.0", "end-1c")) == 0:
        empty_box = "Text Box Is Empty!"
        print(empty_box)
        entry.delete('1.0', END)
        messagebox.showwarning("Warning","Text Box Is Empty!")
        return 'break'
    else: 
        text = entry.get("1.0",END)
        try:
            processing(text=text)
            return 'break'
        except:
            valid_data_msg = "Enter Valid Log Data!"
            print(valid_data_msg)
            entry.delete('1.0', END)
            messagebox.showwarning("Warning","Enter Valid Log Data!")
            return 'break'

def selectall(event=None):
    entry.tag_add('sel', '1.0', 'end')
    return 'break'
"""
def custom_paste(event):
    try:
        entry.delete("sel.first", "sel.last")
    except:
        pass
    entry.insert("insert", entry.clipboard_get())
    return "break"
"""
#Creating the widgets
entry = Text(win, width=50, height=3, wrap=WORD)
entry.insert(END, "Enter First Line In Log")
button = Button(win, text="Generate", width=20)
output1 = Label(text="Jbase Record Count Query",cursor="plus", relief=RAISED, pady=5, wraplength=500)
output2 = Label(text="Jbase Column Count Query",cursor="plus", relief=RAISED, pady=5, wraplength=500)
output3 = Label(text="Oracle Record Count Query",cursor="plus", relief=RAISED, pady=5, wraplength=500)
output4 = Label(text="Oracle Count Count Query",cursor="plus", relief=RAISED, pady=5, wraplength=500)

#Positioning the widgets
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
output1.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))
output2.grid(row=7, column=1, columnspan=2, padx=5, pady=(0,10))
output3.grid(row=9, column=1, columnspan=2, padx=5, pady=(0,10))
output4.grid(row=11, column=1, columnspan=2, padx=5, pady=(0,10))

#Button activation
button.configure(command=takingInput)

#Bindings
win.bind('<Control-a>',selectall)
win.bind('<Control-A>',selectall)
entry.bind("<Return>", takingInput)
output1.bind("<Button-1>",lambda event:pyperclip.copy(first_query))
output2.bind("<Button-1>",lambda event:pyperclip.copy(second_query))
output3.bind("<Button-1>",lambda event:pyperclip.copy(oracle_value))
output4.bind("<Button-1>",lambda event:pyperclip.copy(oracle_value))
"""
win.bind_all('<Control-a>', selectall)
win.bind_all('<Control-A>', selectall)
win.bind("<<Paste>>", custom_paste)
"""
win.mainloop()