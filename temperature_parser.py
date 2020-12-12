import csv
import pandas


if __name__ == "__main__":

    # Transpose data, Set index to the first column
    dataTable = pandas.read_csv(
        'tempDaily.csv', header=None, low_memory=False, skiprows=[0], index_col=0).T

    # Filter and leave only US data
    dataTable = dataTable[dataTable['country'] == "United States"]

    # Drop columns before 2018
    dataTable = pandas.concat([
        dataTable.loc[:, :'datetime'], dataTable.loc[:, '2018-01-01':]], axis=1)

    print(dataTable)
