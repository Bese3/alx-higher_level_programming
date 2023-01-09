-- displays the top 3 of cities temperature during
-- July and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM (SELECT *  FROM temperatures WHERE
    month BETWEEN 7 AND 8) AS result GROUP BY result.city ORDER BY avg_temp DESC
    LIMIT 3 ;
