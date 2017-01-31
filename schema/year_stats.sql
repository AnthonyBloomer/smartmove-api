DELIMITER //

CREATE PROCEDURE county() 
BEGIN
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE _id VARCHAR(40);
  DECLARE _year INT(11);
  DECLARE cur CURSOR FOR SELECT id FROM smartmove.counties;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;
  SET _year = 2010;
  OPEN cur;
  testLoop: LOOP
    FETCH cur INTO _id;
    IF done THEN
      LEAVE testLoop;
    END IF;
    WHILE _year <= 2016 DO
    	CALL insert_year_stats(_id, _year);
    	SET _year = _year + 1;
    END WHILE;
    SET _year = 2010;
  END LOOP testLoop;

  CLOSE cur;
END

//

DELIMITER //

CREATE PROCEDURE insert_year_stats(IN id VARCHAR(20), IN year INT(11)) 
BEGIN
  INSERT INTO smartmove_data_warehouse.fact_year (year, county_id, total_number_of_sales, average_sale_price, max_sale_price, min_sale_price)	
  SELECT year(date_time), county_id, COUNT(price), AVG(price), MAX(price), MIN(price)
  FROM smartmove.properties
  WHERE sale_type = 1
  AND county_id = id
  AND year(date_time) = year
  GROUP BY year(date_time);
END

//

CALL county()
