/*CREATE OR REPLACE PROCEDURE sp_insert_newdata(salesdate date, 
                                              productid int, 
                                              region varchar(1), 
                                              freeship int, 
                                              discount real, 
                                              itemssold int)
AS
    $$ 
        INSERT INTO bzan545masterdata(salesdate,
                                      productid, 
                                      region, 
                                      freeship, 
                                      discount, 
                                      itemssold)
        VALUES (salesdate,
                productid, 
                region, 
                freeship, 
                discount, 
                itemssold);
    $$
LANGUAGE SQL;

CALL public.sp_insert_newdata(VARIADIC bzan545newdata.salesdate,
                       VARIADIC bzan545newdata.productid, 
                       VARIADIC bzan545newdata.region, 
                       VARIADIC bzan545newdata.freeship, 
                       VARIADIC bzan545newdata.discount, 
                       VARIADIC bzan545newdata.itemssold);*/

select * from information_schema.routines where routine_type <> 'FUNCTION';