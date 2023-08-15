-- showing top 3 city from july - aug
SELECT city, AVG(value) AS avg_tmp FROM (
	SELECT * FROM temperatures 
	WHERE month BETWEEN 7 AND 8) AS tmp
GROUP BY tmp.city ORDER BY (avg_tmp) DESC LIMIT 3;
