import re

def generate_sql_file(file_path):
    sql_file = open(file_path, "r").readlines()
    for line in sql_file:
        if line[0:6] == "INSERT":
            # print(line[12:20])
            tables = re.search("\(.*?\)", line).group()
            tables = line.split(tables)
            for table in range(len(tables)):
                tables[table] = tables[table].replace(" ', '\n'", "")
                tables[table] = tables[table].replace("INSERT INTO ", "")
                if table == 1:
                    tables.remove(tables[table])
                    print(tables)

if __name__ == "__main__": 
    file_path = "/home/ehab/uitestautomation/src/test/resources/db-scripts/accounting/vendorinvoice/setup-activate-add-journal-entry(S1).sql"
    generate_sql_file(file_path)