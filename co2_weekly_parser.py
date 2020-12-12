import csv 

# the class that will hold one row of data 
# has a __str__ method that will print out all the class variables 
class Data_row:
	entry_num = 0
	year = 0
	month = 0
	day = 0
	decimal = 0
	average = 0
	ndays = 0
	def __str__(self):
		return(str(self.entry_num) + 
			"\nyear\t" + str(self.year)+
			"\nmonth\t" + str(self.month)+
			"\nday\t" + str(self.day)+
			"\ndecimal\t" + str(self.decimal)+
			"\naverage\t" + str(self.average)+
			"\nndays\t" + str(self.ndays))

data = []
with open("co2_weekly_mlo.csv", newline='') as file: # open the csv file
	read = csv.reader(file, delimiter=' ', quotechar='|') # read the file
	x = 0 # a counter
	for row in read: # go through all rows
		if x > 2221:
			row_data = Data_row() # make a new row class
			row = ', '.join(row).split(",") # split the line into a list
			row_data.entry_num = x - 2220 # count the entry number
			row_data.year = row[0] # put data into row_data
			row_data.month = row[1]
			row_data.day = row[2]
			row_data.decimal = row[3]
			row_data.average = row[4]
			row_data.ndays = row[5]
			data.append(row_data) # add that row to all the data
		x += 1

# print data (remove this when finished)
for row in data:
	print(row)
	print()