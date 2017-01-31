INSERT INTO fact_country (country_id, total_number_of_sales, average_sale_price)
SELECT country_id, COUNT(*), ROUND(AVG(price), 2)
FROM smartmove.properties
WHERE country_id = 1
AND sale_type = 1
