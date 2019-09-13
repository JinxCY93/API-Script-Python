import csv
import psycopg2

connection = psycopg2.connect("host=localhost user=postgres dbname=homes")
cur = connection.cursor()

record = {}

# with open("homes.csv", mode="r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         if record.get(row[' "List"'] or row[' "Living"'].replace(" ", "")) == None:
#             record[row[' "List"'] or row[' "Living"'].replace(" ", "")] = 0
#         record[row[' "List"']  or row[' "Living"'].replace(" ","")] +=1

# with open("homes2.csv", mode="w") as csv_file:
#     fieldnames = ["Sell","List","Living","Rooms","Beds","Baths","Age","Acres","Taxes"]
#     csv_writer = csv.DictWriter(csv_file, fieldnames)

#     csv_writer.writeheader()
#     for Sell,List,Living,Rooms,Beds,Baths,Age,Acres,Taxes in record.items():
#         csv_writer.writerow({"Sell": Sell,"List": List,"Living":Living,"Rooms": Rooms,"Beds": Beds,"Baths": Baths,"Age": Age,"Acres": Acres,"Taxes": Taxes})

with open("homes.csv", mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    recordCount = 0
    # next(csv_reader)
    # cur.copy_from(csv_file,'home',sep=',')
    for row in csv_reader:
        sqlInsert = \
            """INSERT INTO home ("Sell", "List", "Living", "Rooms", "Beds", "Baths", "Age", "Acres", "Taxes") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        try:
            cur.execute(sqlInsert,(row['Sell'], 
                                row[' "List"'], 
                                row[' "Living"'],
                                row[' "Rooms"'], 
                                row[' "Beds"'], 
                                row[' "Baths"'], 
                                row[' "Age"'], 
                                row[' "Acres"'], 
                                row[' "Taxes"']))
            connection.commit()
            recordCount +=1
        
        except psycopg2.DatabaseError as error:
            print(error)
            quit()
    connection.close()