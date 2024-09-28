import csv, pyodbc
import os

# set up some constants
MDB = 'C:/Users/Philipp/Desktop_PC/DM 1.24.08.0/LinkingDB/LinkingDB.mdb'
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
#PWD = 'pw'
export_file = "C:/temp/AC_CSV_Export_DM_v1.24.08.0.csv"

#print(pyodbc.drivers())

def make_csv():
    # connect to db
    #con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD)) # with password
    print("Connect to Database...")
    con = pyodbc.connect('DRIVER={};DBQ={};'.format(DRV,MDB))
    cur = con.cursor()
    print("...DONE")

    print("Execute SQL statement...")
    # run a query and get the results 
    #SQL = 'SELECT * FROM brands;' # your query goes here
    SQL = 'SELECT brandname, modell, volym, aarNr, systypNr, x, xx, obd1_prot, [obd1_prot_VCI+], obd2_prot, blink_prot, obd1_tolk, Key_R, NON_EU from mmod, brands WHERE mmod.maerkenr = brands.brandID AND brands.IsHeavyDuty = 0 ORDER BY brandname, modell, aarNr, systypNr, volym, x, xx, obd1_prot, [obd1_prot_VCI+], obd2_prot, blink_prot, obd1_tolk, key_r'
    rows = cur.execute(SQL).fetchall()
    print(type(rows))
    cur.close()
    con.close()
    print("...DONE")

    if os.path.exists(export_file):
        print("Remove existing export file...")
        os.remove(export_file)
        print("...DONE")
    else:
        print("The file does not exist")

    print("Write Header in CSV...")
    #f = open(export_file, "w", newline='\n', encoding='utf-8')
    f = open(export_file, "w", newline='\n')
    f.write("Hersteller|Modell|Vol|Jahr|Systyp|System (X)|Zusatzinformation (XX)|OBD|OBD_Plus|OBD2|Blink|SGW|SGW_INFO|NON_EU\n")
    f.close()
    print("...DONE")

    # normalize rows
    print("Normalize rows...")
    for row in rows:
        # normalize years
        tmp = int(row[3]) + 1970
        row[3] = str(tmp)

        # replace liter
        row[2] = row[2].replace(".", ",")

        '''if "Blind spot monitor" in row[5]:
            print(row[5])
        '''

    print("...DONE")


    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    print("Write CSV content...")
    #with open(export_file, 'a', newline='', encoding='utf-8') as fou:
    with open(export_file, 'a', newline='') as fou:
        csv_writer = csv.writer(fou,delimiter="|",quotechar="\\",lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
        csv_writer.writerows(rows)

    print("...DONE")

if __name__ == "__main__":
    make_csv()