"""List:Build copy/paste/cut/select all to work probably--
        Make query text boxes dimmed--
        Draw error msgs/pop ups--
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
            output1.delete('1.0', END)
            output1.insert(END, str(jbase_value))
        except:
            valid_data_msg = "Enter Valid Log Data!"
            print(valid_data_msg)
            output1.delete('1.0', END)
            output1.insert(END, str(valid_data_msg))


def slct(event=None):
    entry.tag_add('sel', '1.0', 'end')
    return "break"

#Creating the widgets
l1 = Label(win, text="Enter First Line In Log:")
entry = Text(win, width=50, height=3, wrap=WORD)
button = Button(win, text="Generate", width=20)
l2 = Label(win, text="Jbase Record Count Query:")
output1 = Text(win, width=50, height=3, wrap=WORD)

#Positioning the widgets
l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
l2.grid(row=4, column=1, padx=5, sticky=W)
output1.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))


#Button activation
button.configure(command=get_queries)

win.bind('<Control-a>',slct)
win.bind('<Control-A>',slct)

#So the program is on repeat
win.mainloop()