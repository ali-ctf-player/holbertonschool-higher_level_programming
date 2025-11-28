-- Temperatures
SELECT TOP 3 city,AVG(value) as 'avg_temp' 
FROM temperatures 
WHERE month = 7 OR MONTH = 8 
GROUP BY city  
ORDER BY AVG(value) DESC;
