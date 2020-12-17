CREATE SCHEMA ProjectSchema;

CREATE TABLE ProjectSchema.co2_mm_mlo(
    entry_num INT NOT NULL,
    year INT,
    month INT,
    decimal FLOAT,
    average FlOAT,
    ndays INT,
    PRIMARY KEY (entry_num)
);


CREATE TABLE ProjectSchema.co2_weekly 
(
    entry_num INT NOT NULL,
    year INT,
    month INT,
    decimal FLOAT,
    average FlOAT,
    ndays INT,
    PRIMARY KEY (entry_num)
);

CREATE TABLE ProjectSchema.temperature
(
   city VARCHAR(255) NOT NULL,
   latitude VARCHAR(255),
   longitude VARCHAR(255),
   year INT,
   month INT,
   day INT,
   teperature FLOAT,
   PRIMARY KEY (city,year,month,day)
);

\copy ProjectSchema.co2_mm_mlo FROM 'data/co2_mm_db.csv' WITH (FORMAT CSV, HEADER true, NULL '');
\copy ProjectSchema.co2_weekly FROM 'data/co2_weekly_db.csv' WITH (FORMAT CSV, HEADER true, NULL ''); 
\copy ProjectSchema.temperature FROM 'data/temperature_db.csv' WITH (FORMAT CSV, HEADER true, NULL '');
