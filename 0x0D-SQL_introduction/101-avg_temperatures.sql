-- average temperature value by city
SELECT city, AVG(value) AS avg_tmp FROM temperatures
GROUP  BY (CITY) ORDER BY (AVG(value)) DESC;
