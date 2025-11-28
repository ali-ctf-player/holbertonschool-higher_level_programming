-- 103

SELECT tv_shows.title,SUM(rate) AS 'rating' 
FROM tv_shows 
INNER JOIN tv_show_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY tv_shows.title
ORDER BY SUM(rate) DESC;


