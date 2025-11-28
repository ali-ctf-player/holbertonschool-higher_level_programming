-- Comedy
SELECT tv_shows.title 
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
FROM tv_shows
WHERE tv_shows.title = 'Comedy';
