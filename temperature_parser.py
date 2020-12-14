import csv
import pandas


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

if __name__ == "__main__":

    # Transpose data, Set index to the first column
    dataTable = pandas.read_csv(
        'tempDaily.csv', header=None, low_memory=False, skiprows=[0], index_col=0).T

    # Filter and leave only US data
    dataTable = dataTable[dataTable['country'] == "United States"]

    # Drop columns before 2018
    dataTable = pandas.concat([
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
    f = pandas.DataFrame(outdata, columns = categories)
    f.to_csv('data/temperature_db.csv',index=False)
