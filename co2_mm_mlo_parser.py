import csv 
import pandas as pd

# the class that will hold one row of data 
# has a __str__ method that will print out all the class variables 
class Data_row:
    entry_num = 0
    year = 0
    month = 0
    decimal = 0
    average = 0
    ndays = 0
    
    def to_list(self):
        returned_list = []
        returned_list.append(str(self.entry_num))
        returned_list.append(self.year)
        returned_list.append(self.month)
        returned_list.append(self.decimal)
        returned_list.append(self.average)
        returned_list.append(self.ndays)
        return returned_list

    def __str__(self):
        return(str(self.entry_num) + 
			"\nyear\t" + str(self.year)+
			"\nmonth\t" + str(self.month)+
			"\ndecimal\t" + str(self.decimal)+
			"\naverage\t" + str(self.average)+
			"\nndays\t" + str(self.ndays))        
                
    
# data things in rows:
# year, month, amount into month, average, 

data = []
f = open("co2_mm_mlo.txt", "r")

x = 0 # a counter
for row in f.read().split('\n'): # go through all rows
	if (row != ""):
		row = row.split(" ")
		if x > 747:

				for item in row:
					if item == "":
						row.remove(item)


				row.remove(row[5])
				row.remove(row[5])
				row.remove(row[5])
				row.remove(row[5])
				row.remove(row[6])
				row.remove(row[6])
				row.remove(row[6])
				row.remove(row[7])
				row.remove(row[7])
				row.remove(row[7])
				
				row_data = Data_row() # make a new row class

				row_data.entry_num = x - 747 # count the entry number
				row_data.year = row[0] # put data into row_data
				row_data.month = row[1]
				row_data.decimal = row[2]
				row_data.average = row[3]
				row_data.ndays = row[5]
				data.append(row_data) # add that row to all the data
		
		x += 1

'''
# print data (remove this when finished)
for row in data:
    print(row)
    print()
    break
'''

categories = ['entry_num', 'year', 'month', 'decimal', 'average', 'ndays']
outdata = []
for row in data:
    outdata.append(row.to_list())

#print(outdata[0])
f = pd.DataFrame(outdata, columns = categories)
f.to_csv('data/co2_mm_db.csv',index=False)

