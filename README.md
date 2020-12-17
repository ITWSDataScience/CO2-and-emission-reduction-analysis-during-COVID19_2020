# Team6_2020

## Data Science Final Project:

### System requirements:

- Python 3
    - Must have the third-party library `pandas` installed.
- PostgreSQL

To setup the database and load in the data:
1. Download `data_preprocessing.py`, `co2_mm_mlo.txt`, `co2_weekly_mlo.csv`, `tempDaily.csv`, `schema.sql`, & `db-setup.sql` and place them into the same folder.
2. Run `data_preprocessing.py` to process the data&mdash;3 new files ending in `_db.csv` will appear.
3. Run `db-setup.sql` to create the database.
4. Run `schema.sql`.

### Metadata:

**When was the data gathered?** Dec. 12, 2020  
**How was the data gathered?** Downloaded from the [references](#References) below.  
**Where is the data stored?** The `data` folder of the repository, which is subsequently loaded into a PostgreSQL database (can be accessed by doing the precedures above).  
**Who are the data keepers?**  
- Joe Halasz
- Kevin Kim
- Kevin Pan
- Travis Peterson
- Gregory Saini
- Giri Srinivasan
- Wilson Wong

### References:

1) Monthly global CO2 emissions: https://www.esrl.noaa.gov/gmd/ccgg/trends/ 
2) Global Carbon Dioxide level from 2020: https://climate.nasa.gov/vital-signs/carbon-dioxide/
3) Temperature Monthly for US: https://www.usclimatedata.com/climate/new-york/united-states/3202
4) Temperature Daily for various countries/the world: https://carbonmonitor.org
    - Click on the table icon to download the .csv dataset
