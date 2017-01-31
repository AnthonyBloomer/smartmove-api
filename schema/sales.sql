INSERT INTO smartmove_data_warehouse.dim_date (day, month, year) 
SELECT DAY(date_time), MONTH(date_time), YEAR(date_time) 
FROM smartmove.properties 
WHERE sale_type = 1;

INSERT INTO smartmove_data_warehouse.dim_property (address, county_id, country_id, description) 
SELECT address, county_id, country_id, description 
FROM smartmove.properties 
WHERE sale_type = 1;

INSERT INTO smartmove_data_warehouse.fact_sales (date_id, property_id, price) 
SELECT id, id, price 
FROM smartmove.properties 
WHERE sale_type = 1;
