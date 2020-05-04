"""List:Build copy/paste/cut/select all to work probably--
        Make query text boxes dimmed--
        Hit enter to generate
"""
#Importing TKinter module
from tkinter import *

#Setting up the GUI window
win = Tk()
win.title("Query Generator")
win.resizable(0,0)

#Converting
def get_queries():
    if len(entry.get("1.0", "end-1c")) == 0:
        empty_box = "Text Box Is Empty!"
        print(empty_box)
        output1.delete('1.0', END)
        output2.delete('1.0', END)
        output3.delete('1.0', END)
        output4.delete('1.0', END)
        entry.delete('1.0', END)
        output1.insert(END, str(empty_box))
    else: 
        text = entry.get("1.0",END)
        try:
            jbase_pattern = "jbase file \[(.*?)\] with "
            jbase_value = re.search(jbase_pattern, text).group(1)
            oracle_pattern = "oracle file \[(.*?)]|\n"
            oracle_value = re.search(oracle_pattern, text).group(1)
            print("str:",text)
            print("count:",len(text))
            print("Jbase:", jbase_value)
            print("Oracle:", oracle_value)
            output4.delete('1.0', END)
            output3.delete('1.0', END)
            output2.delete('1.0', END)
            output1.delete('1.0', END)
            entry.delete('1.0', END)
            
            output1.insert(END, str(jbase_value))
            output2.insert(END, str(jbase_value))
            output3.insert(END, str(oracle_value))
            output4.insert(END, str(oracle_value))
        except:
            valid_data_msg = "Enter Valid Log Data!"
            print(valid_data_msg)
            output1.delete('1.0', END)
            output2.delete('1.0', END)
            output3.delete('1.0', END)
            output4.delete('1.0', END)
            entry.delete('1.0', END)
            output1.insert(END, str(valid_data_msg))


# def slct(event=None):
#     entry.tag_add('sel', '1.0', 'end')
#     return "break"

# def custom_paste(event):
#     try:
#         entry.delete("sel.first", "sel.last")
#     except:
#         pass
#     entry.insert("insert", entry.clipboard_get())
#     return "break"


#Creating the widgets
l1 = Label(win, text="Enter First Line In Log:")
entry = Text(win, width=50, height=3, wrap=WORD)
button = Button(win, text="Generate", width=20)
l2 = Label(win, text="Jbase Record Count Query:")
output1 = Text(win, width=50, height=3, wrap=WORD)
l3 = Label(win, text="Jbase Column Count Query:")
output2 = Text(win, width=50, height=3, wrap=WORD)
l4 = Label(win, text="Oracle Record Count Query:")
output3 = Text(win, width=50, height=3, wrap=WORD)
l5 = Label(win, text="Oracle Count Count Query:")
output4 = Text(win, width=50, height=3, wrap=WORD)

#Positioning the widgets
l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
l2.grid(row=4, column=1, padx=5, sticky=W)
output1.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))
l3.grid(row=6, column=1, padx=5, sticky=W)
output2.grid(row=7, column=1, columnspan=2, padx=5, pady=(0,10))
l4.grid(row=8, column=1, padx=5, sticky=W)
output3.grid(row=9, column=1, columnspan=2, padx=5, pady=(0,10))
l5.grid(row=10, column=1, padx=5, sticky=W)
output4.grid(row=11, column=1, columnspan=2, padx=5, pady=(0,10))



#Button activation
button.configure(command=get_queries)

#Build basic text functions
# win.bind('<Control-a>',slct)
# win.bind('<Control-A>',slct)
# win.bind_all('<Control-a>', slct)
# win.bind_all('<Control-A>', slct)
# win.bind("<<Paste>>", custom_paste)

#So the program is on repeat
win.mainloop()