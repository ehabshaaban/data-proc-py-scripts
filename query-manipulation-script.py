from tkinter import *
import os
os.system('clear')

root =Tk()
root.title('Query Manipulation Program')
# root.iconbitmap('/home/ehab/Desktop/query manipulation script/image.ico')
root.geometry('400x600')

#fix any other input but files!
#and also more than two lines!!
def get_queries():

    log_line = log_text_box.get()

    if len(log_line) == 0:
        print("str:",log_line)
        print("count:",len(log_line))
        msg = Label(root, text="Enter first line in log file", font="Tahoma").pack()
    
    else:
        print("str:",log_line)
        print("count:",len(log_line))

        #finding jbase file value
        jbase_pattern = "jbase file \[(.*?)\] with "
        jbase_value = re.search(jbase_pattern, log_line).group(1)
        print("jbase:", jbase_value)
        jbase = Label(root, text=jbase_value).pack()
        # jbase_value=None
        

        #finding oracle file value
        oracle_pattern = "oracle file \[(.*?)]|\n"
        oracle_value = re.search(oracle_pattern, log_line).group(1)
        print("oracle:", oracle_value)
        oracle = Label(root, text=oracle_value).pack()
        # oracle_value = None

        log_text_box.delete(0,END)
    

log_text_box = Entry(root, width=30)
log_text_box.insert(0, "Enter first line in log file")
log_text_box.pack()

get_query = Button(root, text='Generate Queries',command=get_queries).pack()

root.mainloop()