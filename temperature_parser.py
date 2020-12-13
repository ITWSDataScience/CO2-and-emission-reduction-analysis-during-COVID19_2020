import csv
import pandas


class TempData:
    def __init__(self, city, latitude, longitude, date, temperature):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.date = date  # YYYY-MM-DD
        self.temperature = temperature  # Celcius


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
