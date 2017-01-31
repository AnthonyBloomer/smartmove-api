DELIMITER //

CREATE PROCEDURE towns() 
BEGIN
  DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE _id VARCHAR(30);
  DECLARE cur CURSOR FOR SELECT town_name FROM smartmove.towns;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;
  OPEN cur;
  testLoop: LOOP
    FETCH cur INTO _id;
    IF done THEN
      LEAVE testLoop;
    END IF;
    CALL insert_town_stats(_id);
  END LOOP testLoop;

  CLOSE cur;
END

//

DELIMITER //

CREATE PROCEDURE insert_town_stats(IN _town VARCHAR(40)) 
BEGIN
  INSERT INTO smartmove_data_warehouse.fact_town (town_name, total_number_of_sales, average_sale_price, max_sale_price, min_sale_price)
  SELECT * FROM
    (SELECT _town) AS t, 
    (SELECT COUNT(*) AS total_number_of_sales, ROUND(AVG(price), 2) AS average_sale_price, MAX(price), MIN(price)
    FROM smartmove.properties AS p 
    WHERE address LIKE CONCAT('%', _town,'%') AND sale_type = 1) AS s;
END
//

CALL towns()

