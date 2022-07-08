-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS s
ON t.id = s.genre_id

INNER JOIN tv_shows AS g
ON t.id = s.genre_id
WHERE g.name = "Comedy"
ORDER BY t.title;