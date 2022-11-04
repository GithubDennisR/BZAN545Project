DROP PROCEDURE IF EXISTS sp_insert_newdata;

TRUNCATE TABLE bzan545masterdata;

CREATE PROCEDURE sp_insert_newdata()
AS
    $$ 
    COPY bzan545masterdata
    FROM 'C:\\Temp\\bzan545masterdata.csv' WITH (format csv, header true, delimiter ',');
    $$
LANGUAGE SQL;

CALL sp_insert_newdata();