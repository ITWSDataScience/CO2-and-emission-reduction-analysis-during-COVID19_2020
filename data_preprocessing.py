import csv 
import pandas as pd

def co2_mm_mlo():
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
    

def co2_weekly():
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
    
    '''
    # print data (remove this when finished)
    for row in data:
    	print(row)
    	print()
    '''
        
    categories = ['entry_num', 'year', 'month', 'decimal', 'average', 'ndays']
    outdata = []
    for row in data:
        outdata.append(row.to_list())
    
    #print(outdata[0])
    f = pd.DataFrame(outdata, columns = categories)
    f.to_csv('data/co2_weekly_db.csv',index=False)


def temperature():
    class TempData:
        def __init__(self, city, latitude, longitude, date, temperature):
            self.city = city
            self.latitude = latitude
            self.longitude = longitude
            self.date = date  # YYYY-MM-DD
            self.temperature = temperature  # Celcius
            
        def to_list(self):
            month_day_year = self.date.split('-')
            if(len(month_day_year) != 3):
                return
            month = month_day_year[1]
            day = month_day_year[2]
            year = month_day_year[0]
            returned_list = []
            returned_list.append(self.city)
            returned_list.append(self.latitude)
            returned_list.append(self.longitude)
            returned_list.append(year)
            returned_list.append(month)
            returned_list.append(day)
            returned_list.append(self.temperature)
            return returned_list
    
    
    
    # Transpose data, Set index to the first column
    dataTable = pd.read_csv(
        'tempDaily.csv', header=None, low_memory=False, skiprows=[0], index_col=0).T

    # Filter and leave only US data
    dataTable = dataTable[dataTable['country'] == "United States"]

    # Drop columns before 2018
    dataTable = pd.concat([
        dataTable.loc[:, :'datetime'], dataTable.loc[:, '2018-01-01':]], axis=1)

    # Datatable here is the filtered data as a dataframe if you want
    # From here I will be assorting them into the TempData class format
    # like the other parser that we have

    dataSet = []
    # loop through each rows
    for index, row in dataTable.iterrows():
        # loop through each columns starting from dates
        # name would be the YYYY-MM-DD format and data would be temperature value
        for name, data in row.loc['datetime':].iteritems():
            tempDataObject = TempData(city=row['city'], latitude=row['lat'],
                                      longitude=row['lng'], date=name, temperature=data)
            # If you want to see all classes printed uncomment below
            # print(tempDataObject.__dict__)
            dataSet.append(tempDataObject)

    
    categories = ['city', 'latitude', 'longitude', 'year', 'month', 'day', 'temperature']
    outdata = []
    for i in range(1,int(len(dataSet))):
        list_val = dataSet[i].to_list()
        if (list_val != None):
            outdata.append(dataSet[i].to_list())

    #print(outdata[4039])
    f = pd.DataFrame(outdata, columns = categories)
    f.to_csv('data/temperature_db.csv',index=False)


if __name__ == "__main__":
    co2_mm_mlo()
    co2_weekly()
    temperature()