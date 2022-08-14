"""
executing queries on a laggy jbase shell was the most dreadful experience ever
fastest way was to use query_manipulation_script to generate those queries and paste them
"""

#Importing tKinter module
from tkinter import *
from tkinter import messagebox

#Setting up GUI
win = Tk()
win.title("Query Generator")
win.resizable(0,0)

def text_manipulation(jbase_value, oracle_value):
    global first_query
    global second_query
    global third_query
    global fourth_query

    if oracle_value[:5] == 'FBNK_':
        print(oracle_value[:5])
        #Building 1st query_With FBNK --> Jbase
        key=oracle_value[:5]
        table_name = str(jbase_value).replace("_",".")
        prefix = str(key).replace("_",".")
        first_query_table = prefix+table_name
        first_query = "SELECT "+first_query_table
               
    elif oracle_value[:2] == 'F_':
        print(oracle_value[:2])
        #Building 1st query_With F --> Jbase
        key=oracle_value[:2]
        table_name=str(jbase_value).replace("_",".")
        prefix=str(key).replace("_",".")
        first_query_table =  prefix+table_name
        first_query = "SELECT "+first_query_table

        #Building 2nd query_With $HIS --> Jbase
    if '$HIS' in str(jbase_value):
        table_name_witout_his = table_name.replace('$HIS',"")
        second_query = "SELECT F.STANDARD.SELECTION SYS.FIELD.NAME WITH FILE.NAME EQ '"+table_name_witout_his+"'"
    else:
        #Building 2nd query_Without $HIS --> Jbase
        second_query = "SELECT F.STANDARD.SELECTION SYS.FIELD.NAME WITH FILE.NAME EQ '"+table_name+"'"
        
    #Building 3rd query --> Oracle
    third_query = "SELECT COUNT(*) FROM T24.V_"+oracle_value+";"

    #Building 4th query --> Oracle
    fourth_query = "SELECT count(*) FROM ALL_TAB_COLUMNS WHERE OWNER = 'T24' AND TABLE_NAME = 'V_"+oracle_value+"';"

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
    output3.config(text=third_query)
    output4.config(text=fourth_query)

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

def custom_paste(event):
    try:
        entry.delete("sel.first", "sel.last")
    except:
        pass
    return "break"

def toggleAlwaysOnTop():
    if win.attributes("-topmost") == 0:
        win.attributes("-topmost", 1)
    else:
        win.attributes("-topmost", 0)

def copy_to_clipboard(value):
    win.clipboard_clear()
    win.clipboard_append(value)

def emptyselect_clipboard():
    win.clipboard_clear()
    win.clipboard_append("SELECT")

def About():
    messagebox.showinfo("About","Developed in Python 3.0 for QCENTRIS GmbH")

#Creating the widgets
entry = Text(win, width=30, height=3, wrap=WORD)
entry.insert(END, "Enter First Line In Log")
button = Button(win, text="Generate", width=8,font = ('Ubuntu Mono','15','bold'), fg='green')
info1 = Label(text="jbase RECORD count query", pady=5, wraplength=500,font=("Ubuntu Mono", 10))
output1 = Label(text="                           ",cursor="plus", relief=RAISED, pady=5, wraplength=500,bg='white')
info2 = Label(text="jbase COLUMN count query", pady=5, wraplength=500,font=("Ubuntu Mono", 10))
output2 = Label(text="                           ",cursor="plus", relief=RAISED, pady=5, wraplength=500,bg='white')
info3 = Label(text="oracle RECORD count query", pady=5, wraplength=500,font=("Ubuntu Mono", 10))
output3 = Label(text="                           ",cursor="plus", relief=RAISED, pady=5, wraplength=500,bg='white')
info4 = Label(text="oracle COLUMN count query", pady=5, wraplength=500,font=("Ubuntu Mono", 10))
output4 = Label(text="                           ",cursor="plus", relief=RAISED, pady=5, wraplength=500,bg='white')
emptySelect = Label(text="Empty Select",cursor="plus", relief=RAISED, pady=5, wraplength=500)

#Positioning the widgets
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
info1.grid(row=5, column=1,sticky="NE")
output1.grid(row=7, column=1, columnspan=2, padx=5, pady=(0,10))
info2.grid(row=9, column=1,sticky="NE")
output2.grid(row=11, column=1, columnspan=2, padx=5, pady=(0,10))
info3.grid(row=13, column=1,sticky="NE")
output3.grid(row=14, column=1, columnspan=2, padx=5, pady=(0,10))
info4.grid(row=16, column=1,sticky="NE")
output4.grid(row=18, column=1, columnspan=2, padx=5, pady=(0,10))
emptySelect.grid(row=20, column=1, columnspan=2, padx=5, pady=(0,10))

#Configs
button.config(command=takingInput)
output1.config(font=("Ubuntu Mono", 10))
output2.config(font=("Ubuntu Mono", 10))
output3.config(font=("Ubuntu Mono", 10))
output4.config(font=("Ubuntu Mono", 10))
emptySelect.config(font=("Ubuntu Mono", 10))

#Bindings
win.bind('<Control-a>',selectall)
win.bind('<Control-A>',selectall)
entry.bind("<Return>", takingInput)
win.bind('<Control-v>',custom_paste)
win.bind('<Control-V>',custom_paste)
first_query = ""
second_query = ""
third_query = ""
fourth_query = ""
output1.bind("<Button-1>",lambda event:copy_to_clipboard(first_query))
output2.bind("<Button-1>",lambda event:copy_to_clipboard(second_query))
output3.bind("<Button-1>",lambda event:copy_to_clipboard(third_query))
output4.bind("<Button-1>",lambda event:copy_to_clipboard(fourth_query))
emptySelect.bind("<Button-1>",lambda event:emptyselect_clipboard())

#Options Menu
menubar = Menu()
optionsMenu = Menu(menubar, tearoff=0)
optionsMenu.add_checkbutton(label="Always on top", command=toggleAlwaysOnTop)
optionsMenu.add_checkbutton(label="About", command=About)
menubar.add_cascade(label="Options", menu=optionsMenu)
win.config(menu=menubar)

#Tkinter Main Loop
win.mainloop()
