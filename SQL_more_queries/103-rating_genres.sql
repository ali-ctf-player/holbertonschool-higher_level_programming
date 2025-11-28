-- 103

SELECT tv_genres.name,SUM(rate) AS 'rating' 
FROM tv_genres 
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_show_genres.show_id
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name 
ORDER BY SUM(rate) DESC;
