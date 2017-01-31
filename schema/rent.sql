DELIMITER //

CREATE PROCEDURE counties() 
BEGIN
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE _id VARCHAR(40);
  DECLARE cur CURSOR FOR SELECT id FROM smartmove.counties;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;
  OPEN cur;
  testLoop: LOOP
    FETCH cur INTO _id;
    IF done THEN
      LEAVE testLoop;
    END IF;
    CALL insert_rent_prices(_id);
  END LOOP testLoop;

  CLOSE cur;
END

//

DELIMITER //

CREATE PROCEDURE insert_rent_prices(IN id VARCHAR(20)) 
BEGIN
  INSERT INTO smartmove_data_warehouse.fact_rent (county_id, total_number_of_sales, average_sale_price, max_price, min_price)	
  SELECT county_id, COUNT(*) AS total_number_of_sales, ROUND(AVG(price), 2) AS average_sale_price, MAX(price), MIN(price)
  FROM smartmove.properties AS p
  WHERE county_id = id
  AND sale_type = 4;
END

//

CALL counties()
