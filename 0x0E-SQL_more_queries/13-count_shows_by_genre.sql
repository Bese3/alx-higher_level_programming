-- ists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres LEFT JOIN
    tv_show_genres tsg ON tv_genres.id = tsg.genre_id
    WHERE tsg.genre_id IS NOT NULL GROUP BY name ORDER BY number_of_shows DESC;
