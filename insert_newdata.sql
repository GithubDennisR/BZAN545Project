COPY bzan545newdata
FROM 'C:\\Temp\\bzan545newdata.csv' WITH (format csv, header true, delimiter ',');
INSERT INTO bzan545masterdata
SELECT * FROM bzan545newdata;

/*truncate table bzan545masterdata*/
/*select * from bzan545masterdata*/
/*select * from bzan545newdata*/