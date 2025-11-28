-- Temperatures
SELECT city,AVG(value) as 'avg_temp' 
FROM temperatures 
WHERE month = 7 OR MONTH = 8 TOP 3
GROUP BY city  
ORDER BY AVG(value) DESC;
