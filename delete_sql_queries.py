import re

def generate_sql_file(file_path):
    table_lst = []
    sql_file = open(file_path, "r").readlines()
    for line in sql_file:
        if line[0:6] == "INSERT":
            tables = re.search("\(.*?\)", line).group()
            tables = line.split(tables)
            for table in range(len(tables)):
                tables[table] = tables[table].replace(" ', '\n'", "")
                tables[table] = tables[table].replace("INSERT INTO ", "")
                if table == 1:
                    tables.remove(tables[table])
                    table_name = tables[0]
                    query = "DELETE FROM " + tables[0] +"WHERE id=;"
                    table_lst.append(query)
    print(table_lst)
    f=open('delete_queries.txt','w')
    for t in table_lst:
        f.write(t+'\n')
    f.close()    

if __name__ == "__main__": 
    file_path = "/home/ehab/uitestautomation/src/test/resources/db-scripts/accounting/vendorinvoice/setup-activate-add-journal-entry(S1).sql"
    generate_sql_file(file_path)